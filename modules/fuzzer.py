import subprocess
import os

class FuzzerModule:
    """Advanced Fuzzing using Ffuf and Arjun."""

    def __init__(self, target_url, output_dir, wordlist="wordlist.txt"):
        self.target_url = target_url
        self.output_dir = output_dir
        self.wordlist = wordlist
        self.fuzz_output = os.path.join(output_dir, "fuzz_results.json")

    def run_ffuf(self):
        """Run directory fuzzing."""
        print(f"[*] Fuzzing directories on {self.target_url}...")
        try:
            # Basic ffuf command
            command = [
                "ffuf", 
                "-u", f"{self.target_url}/FUZZ", 
                "-w", self.wordlist,
                "-mc", "200,204,301,302,307,401,403",
                "-o", self.fuzz_output,
                "-of", "json"
            ]
            subprocess.run(command)
        except FileNotFoundError:
            print("[!] Ffuf not found.")

    def run_arjun(self):
        """Find hidden parameters using Arjun."""
        print(f"[*] Hunting hidden parameters on {self.target_url}...")
        try:
            command = ["arjun", "-u", self.target_url, "-oJ", os.path.join(self.output_dir, "params.json")]
            subprocess.run(command)
        except FileNotFoundError:
            print("[!] Arjun not found.")
