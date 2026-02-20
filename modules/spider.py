import subprocess
import os

class SpiderModule:
    """Advanced Web Crawling and JS Analysis using Katana."""
    
    def __init__(self, input_file, output_dir):
        self.input_file = input_file
        self.output_dir = output_dir
        self.endpoints_file = os.path.join(output_dir, "discovered_endpoints.txt")
        self.js_files_file = os.path.join(output_dir, "js_files.txt")

    def run_katana(self, h1_user=None, email=None):
        """Crawl subdomains to find endpoints and JS files."""
        print(f"[*] Starting Katana Spidering on live hosts...")
        if not os.path.exists(self.input_file):
            print("[!] Live hosts file not found for spidering.")
            return

        try:
            # -jc: find JS files, -kf: find hidden fields, -d 5: depth
            command = [
                "katana", 
                "-l", self.input_file, 
                "-silent", 
                "-jc", 
                "-kf", "all",
                "-o", self.endpoints_file
            ]

            # Adding Custom Headers for compliance (e.g., HackerOne)
            if h1_user:
                command.extend(["-H", f"X-Bug-Bounty: {h1_user}"])
            if email:
                command.extend(["-H", f"X-Test-Account-Email: {email}"])

            subprocess.run(command, check=True)
            
            # Simple grep-like filter for JS files from the output
            if os.path.exists(self.endpoints_file):
                with open(self.endpoints_file, "r") as f, open(self.js_files_file, "w") as js_f:
                    for line in f:
                        if line.strip().endswith(".js"):
                            js_f.write(line)
            
            print(f"[+] Katana crawl complete. Endpoints found: {self.endpoints_file}")
        except FileNotFoundError:
            print("[!] Katana not found. Please install it.")
        except subprocess.CalledProcessError as e:
            print(f"[!] Katana error: {e}")
