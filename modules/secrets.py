import re
import os

class SecretScraper:
    """Scans URLs and files for sensitive secrets (API Keys, Tokens)."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.secrets_file = os.path.join(output_dir, "discovered_secrets.txt")
        # Common high-value patterns
        self.patterns = {
            "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
            "AWS Access Key": r"AKIA[0-9A-Z]{16}",
            "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
            "GitHub Token": r"gh[pous]_[a-zA-Z0-9]{36}",
            "Generic Secret": r"(?i)(secret|password|auth|api_key|token)[=:'\"]+([0-9a-zA-Z]{10,64})",
            "Firebase URL": r"https://[a-zA-Z0-9-]+\.firebaseio\.com"
        }

    def scan_file(self, file_path):
        """Scans a text file for secrets."""
        if not os.path.exists(file_path):
            return

        findings = []
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for name, pattern in self.patterns.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        findings.append(f"[{name}] {match.group(0)} (Found in: {os.path.basename(file_path)})")
            
            if findings:
                with open(self.secrets_file, "a", encoding="utf-8") as f:
                    for find in findings:
                        f.write(f"{find}\n")
                print(f"[+] Found {len(findings)} potential secrets in {os.path.basename(file_path)}!")
        except Exception as e:
            print(f"[!] Error scanning {file_path}: {e}")
