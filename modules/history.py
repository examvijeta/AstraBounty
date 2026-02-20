import requests
import os

class HistoryModule:
    """Fetches historic URLs from the Wayback Machine (archive.org)."""

    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.history_file = os.path.join(output_dir, "historic_urls.txt")

    def fetch_wayback(self):
        """Fetches URLs from Wayback Machine API."""
        print(f"[*] Fetching historic URLs for {self.target} from Wayback Machine...")
        url = f"http://web.archive.org/cdx/search/cdx?url=*.{self.target}/*&output=txt&fl=original&collapse=urlkey"
        
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                urls = response.text.splitlines()
                with open(self.history_file, "w", encoding="utf-8") as f:
                    for u in urls:
                        f.write(f"{u}\n")
                print(f"[+] Found {len(urls)} historic URLs.")
                return self.history_file
            else:
                print(f"[!] Wayback API returned status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"[!] Error fetching historic data: {e}")
            return None
