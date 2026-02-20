import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

class InfraModule:
    """Advanced Infrastructure Mapping using Amass and Subfinder."""
    
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.all_subdomains_file = os.path.join(output_dir, f"{target}_full_recon.txt")

    def run_amass(self):
        """Runs OWASP Amass for deep discovery."""
        print(f"[*] Starting Amass Deep Recon for {self.target}...")
        try:
            command = ["amass", "enum", "-d", self.target, "-passive", "-silent"]
            
            # Check for local config.ini
            if os.path.exists("config.ini"):
                command.extend(["-config", "config.ini"])
                print("[*] Info: Using local Amass config.ini with API keys.")

            result = subprocess.run(command, capture_output=True, text=True)
            subs = result.stdout.splitlines()
            print(f"[+] Amass found {len(subs)} subdomains.")
            return subs
        except FileNotFoundError:
            return []

    def run_subfinder(self):
        """Runs Subfinder for fast discovery."""
        print(f"[*] Starting Subfinder for {self.target}...")
        try:
            command = ["subfinder", "-d", self.target, "-silent"]
            result = subprocess.run(command, capture_output=True, text=True)
            subs = result.stdout.splitlines()
            print(f"[+] Subfinder found {len(subs)} subdomains.")
            return subs
        except FileNotFoundError:
            return []

    def full_recon(self):
        """Combines results from multiple tools running in parallel."""
        print("[*] Phase 1: Infrastructure Mapping (Parallel)")
        
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_amass = executor.submit(self.run_amass)
            future_subfinder = executor.submit(self.run_subfinder)
            
            amass_subs = future_amass.result()
            subfinder_subs = future_subfinder.result()
        
        # Merge and dedup
        total_subs = list(set(amass_subs + subfinder_subs))
        
        with open(self.all_subdomains_file, "w") as f:
            for sub in total_subs:
                f.write(f"{sub}\n")
        
        print(f"[+] Recon complete. Total unique subdomains: {len(total_subs)}")
        return self.all_subdomains_file
