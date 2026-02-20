from modules.infra import InfraModule
from modules.spider import SpiderModule
from modules.fuzzer import FuzzerModule
from modules.dashboard import DashboardModule
from modules.utils import check_tools
from modules.history import HistoryModule
from modules.secrets import SecretScraper
from modules.notifier import Notifier
import subprocess

def main():
    parser = argparse.ArgumentParser(description="AstraBounty - Professional Bug Bounty Framework")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", default="astra_results", help="Output directory")
    parser.add_argument("--deep", action="store_true", help="Enable deep recon using Amass")
    parser.add_argument("--god-mode", action="store_true", help="Enable extreme-power features (history, secret hunting)")
    parser.add_argument("--webhook", help="Discord/Telegram webhook/token for alerts")

    args = parser.parse_args()
    target = args.domain
    output_dir = os.path.join(args.output, target)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n🚀 [AstraBounty] Launching Mission: {target}")
    if args.god_mode: print("🔱 GOD MODE ENABLED: Unleashing extreme power...")
    
    # 0. Health Check
    required_tools = ["amass", "subfinder", "httpx", "katana", "ffuf"]
    check_tools(required_tools)

    start_time = datetime.datetime.now()
    notifier = Notifier(webhook_url=args.webhook)

    # 1. Infrastructure Mapping
    infra = InfraModule(target, output_dir)
    recon_file = infra.full_recon()

    # 2. Historic Intelligence (God Mode)
    historic_urls_file = None
    if args.god_mode:
        history = HistoryModule(target, output_dir)
        historic_urls_file = history.fetch_wayback()

    # 3. Live Host Discovery (httpx)
    print("\n[*] Phase 2: Live Host Discovery (httpx)")
    live_hosts_file = os.path.join(output_dir, "live_hosts.txt")
    live_hosts_count = 0
    try:
        command = ["httpx", "-l", recon_file, "-silent", "-o", live_hosts_file]
        subprocess.run(command)
        if os.path.exists(live_hosts_file):
            with open(live_hosts_file, "r") as f:
                live_hosts_count = len(f.readlines())
        print(f"[+] Found {live_hosts_count} live hosts.")
    except Exception as e:
        print(f"[!] Httpx error: {e}")

    # 4. Advanced Spidering (Katana)
    print("\n[*] Phase 3: Advanced Spidering (Katana)")
    spider = SpiderModule(live_hosts_file, output_dir)
    spider.run_katana()

    # 5. Secret & Intelligence Hunting (God Mode)
    secrets_count = 0
    if args.god_mode:
        print("\n[*] Phase 4: Secret Hunting & Historic Analysis")
        scraper = SecretScraper(output_dir)
        # Scan discovered endpoints and historic URLs
        if os.path.exists(spider.endpoints_file): scraper.scan_file(spider.endpoints_file)
        if historic_urls_file and os.path.exists(historic_urls_file): scraper.scan_file(historic_urls_file)
        
        if os.path.exists(scraper.secrets_file):
            with open(scraper.secrets_file, "r") as f:
                secrets_count = len(f.readlines())
            notifier.send_discord(f"🚨 CRITICAL: Found {secrets_count} secrets for {target}!")

    # Calculate real stats
    endpoints_count = 0
    if os.path.exists(spider.endpoints_file):
        with open(spider.endpoints_file, "r") as f:
            endpoints_count = len(f.readlines())

    stats = {
        "date": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "subdomains_count": 0,
        "live_hosts_count": live_hosts_count,
        "endpoints_count": endpoints_count,
        "secrets_count": secrets_count,
        "critical_count": 0,
        "recon_summary": ""
    }

    if os.path.exists(recon_file):
        with open(recon_file, "r") as f:
            lines = f.readlines()
            stats["subdomains_count"] = len(lines)
            stats["recon_summary"] = "".join(lines[:10]) + ("\n..." if len(lines) > 10 else "")

    # 6. Visual Reporting
    dash = DashboardModule(target, output_dir)
    dash.generate(stats)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"\n✅ [AstraBounty] Mission Completed in {duration}")
    print(f"[+] Final Dashboard: {dash.dashboard_file}\n")

if __name__ == "__main__":
    main()
