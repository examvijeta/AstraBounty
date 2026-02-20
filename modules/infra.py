import subprocess
import os

class InfraModule:
    """Advanced Infrastructure Mapping using Amass and Subfinder."""
    
    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.all_subdomains_file = os.path.join(output_dir, f"{target}_full_recon.txt")

    def run_amass(self):
        """Runs OWASP Amass for deep discovery."""
        print(f"[*] Running Amass Deep Recon for {self.target} (this may take time)...")
        try:
            # Note: amass enum -d target
            command = ["amass", "enum", "-d", self.target, "-passive", "-silent"]
            result = subprocess.run(command, capture_output=True, text=True)
            return result.stdout.splitlines()
        except FileNotFoundError:
            print("[!] Amass not found. Skipping deep recon.")
            return []

    def run_subfinder(self):
        """Runs Subfinder for fast discovery."""
        print(f"[*] Running Subfinder for {self.target}...")
        try:
            command = ["subfinder", "-d", self.target, "-silent"]
            result = subprocess.run(command, capture_output=True, text=True)
            return result.stdout.splitlines()
        except FileNotFoundError:
            print("[!] Subfinder not found.")
            return []

    def full_recon(self):
        """Combines results from multiple tools."""
        amass_subs = self.run_amass()
        subfinder_subs = self.run_subfinder()
        
        # Merge and dedup
        total_subs = list(set(amass_subs + subfinder_subs))
        
        with open(self.all_subdomains_file, "w") as f:
            for sub in total_subs:
                f.write(f"{sub}\n")
        
        print(f"[+] Total unique subdomains discovered: {len(total_subs)}")
        return self.all_subdomains_file
