import argparse
import os
import datetime
from modules.infra import InfraModule
from modules.spider import SpiderModule
from modules.fuzzer import FuzzerModule
from modules.dashboard import DashboardModule
from modules.utils import check_tools
from modules.history import HistoryModule
from modules.secrets import SecretScraper
from modules.notifier import Notifier
from modules.vulnerability import VulnerabilityModule
import subprocess

def main():
    parser = argparse.ArgumentParser(description="AstraBounty - Professional Bug Bounty Framework")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", default="astra_results", help="Output directory")
    parser.add_argument("--deep", action="store_true", help="Enable deep recon using Amass")
    parser.add_argument("--god-mode", action="store_true", help="Enable extreme-power features (history, secret hunting)")
    parser.add_argument("--omni", action="store_true", help="FULLY AUTONOMOUS: Recon -> Discovery -> Vuln Scan -> Reporting")
    parser.add_argument("--webhook", help="Discord webhook URL for alerts")
    parser.add_argument("--tg-token", help="Telegram Bot API Token")
    parser.add_argument("--tg-chat-id", help="Telegram Chat ID")
    parser.add_argument("--h1-user", help="HackerOne Username (for custom headers)")
    parser.add_argument("--email", help="Test Account Email (for custom headers)")

    args = parser.parse_args()
    target = args.domain
    output_dir = os.path.join(args.output, target)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n🚀 [AstraBounty] Launching Mission: {target}")
    if args.omni: print("🌌 OMNIMODE ENABLED: Fully Autonomous Hacking in progress...")
    elif args.god_mode: print("🔱 GOD MODE ENABLED: Unleashing extreme power...")
    
    # 0. Health Check
    required_tools = ["amass", "subfinder", "httpx", "katana", "ffuf", "nuclei", "dalfox", "jsluice"]
    check_tools(required_tools)

    start_time = datetime.datetime.now()
    notifier = Notifier(
        webhook_url=args.webhook, 
        telegram_token=args.tg_token, 
        telegram_chat_id=args.tg_chat_id
    )

    # 1. Infrastructure Mapping
    infra = InfraModule(target, output_dir)
    recon_file = infra.full_recon()

    # 2. Historic Intelligence (God Mode / Omni)
    historic_urls_file = None
    if args.god_mode or args.omni:
        history = HistoryModule(target, output_dir)
        historic_urls_file = history.fetch_wayback()

    # 3. Live Host Discovery (httpx)
    print("\n[*] Phase 2: Live Host Discovery (httpx)")
    live_hosts_file = os.path.join(output_dir, "live_hosts.txt")
    live_hosts_count = 0
    try:
        command = ["httpx", "-l", recon_file, "-silent", "-o", live_hosts_file]
        if args.h1_user: command.extend(["-H", f"X-Bug-Bounty: {args.h1_user}"])
        if args.email: command.extend(["-H", f"X-Test-Account-Email: {args.email}"])
        
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
    spider.run_katana(h1_user=args.h1_user, email=args.email)

    # 5. Secret & Intelligence Hunting (God Mode / Omni)
    secrets_count = 0
    if args.god_mode or args.omni:
        print("\n[*] Phase 4: Secret Hunting & Historic Analysis")
        scraper = SecretScraper(output_dir)
        if os.path.exists(spider.endpoints_file): scraper.scan_file(spider.endpoints_file)
        if historic_urls_file and os.path.exists(historic_urls_file): scraper.scan_file(historic_urls_file)
        
        if os.path.exists(scraper.secrets_file):
            with open(scraper.secrets_file, "r") as f:
                secrets_count = len(f.readlines())
            alert_msg = f"🚨 CRITICAL: Found {secrets_count} secrets for {target}!"
            notifier.send_discord(alert_msg)
            notifier.send_telegram(alert_msg)

    # 6. Autonomous Vulnerability Scanning (OmniMode)
    critical_count = 0
    if args.omni:
        print("\n[*] Phase 5: Autonomous Vulnerability Discovery (OmniMode)")
        vuln = VulnerabilityModule(target, output_dir)
        
        # Scan hosts and endpoints for vulns
        vuln_file = vuln.run_nuclei(live_hosts_file, h1_user=args.h1_user, email=args.email)
        xss_file = vuln.run_dalfox(spider.endpoints_file)
        
        if vuln_file and os.path.exists(vuln_file):
            with open(vuln_file, "r") as f:
                lines = f.readlines()
                critical_count = len(lines)
                if critical_count > 0:
                    notifier.send_discord(f"☢️ VULN FOUND: {critical_count} critical/high bugs detected on {target}!")
                    notifier.send_telegram(f"☢️ VULN FOUND: {critical_count} bugs on {target}!")

    # Calculate final stats
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
        "critical_count": critical_count,
        "recon_summary": ""
    }

    if os.path.exists(recon_file):
        with open(recon_file, "r") as f:
            lines = f.readlines()
            stats["subdomains_count"] = len(lines)
            stats["recon_summary"] = "".join(lines[:10]) + ("\n..." if len(lines) > 10 else "")

    # 7. Visual Reporting
    dash = DashboardModule(target, output_dir)
    dash.generate(stats)

    # 8. Automated File Exfiltration (Telegram)
    if args.tg_token and args.tg_chat_id:
        print("\n[*] Exfiltrating results to Telegram...")
        notifier.send_telegram(f"🎨 Mission Dashboard for {target} is ready!")
        notifier.send_document(dash.dashboard_file)
        
        # Send other important findings
        if args.omni:
            if os.path.exists(vuln.nuclei_file): notifier.send_document(vuln.nuclei_file)
            if os.path.exists(vuln.xss_file): notifier.send_document(vuln.xss_file)
        
        if os.path.exists(os.path.join(output_dir, "discovered_secrets.txt")):
            notifier.send_document(os.path.join(output_dir, "discovered_secrets.txt"))

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n✅ [AstraBounty] Autonomous Mission Completed in {duration}")
    print(f"[+] Final Intelligence Report: {dash.dashboard_file}")
    if args.tg_token: print("[+] Results sent to your Telegram chat! 📱")

if __name__ == "__main__":
    main()
