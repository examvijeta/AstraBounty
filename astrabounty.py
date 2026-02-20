import argparse
import os
import datetime
from modules.infra import InfraModule
from modules.spider import SpiderModule
from modules.fuzzer import FuzzerModule
from modules.dashboard import DashboardModule
from modules.utils import check_tools
import subprocess

def main():
    parser = argparse.ArgumentParser(description="AstraBounty - Professional Bug Bounty Framework")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", default="astra_results", help="Output directory")
    parser.add_argument("--deep", action="store_true", help="Enable deep recon using Amass")

    args = parser.parse_args()
    target = args.domain
    output_dir = os.path.join(args.output, target)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n🚀 [AstraBounty] Launching Mission: {target}")
    
    # 0. Health Check
    required_tools = ["amass", "subfinder", "httpx", "katana", "ffuf"]
    check_tools(required_tools)

    start_time = datetime.datetime.now()

    # 1. Infrastructure Mapping
    infra = InfraModule(target, output_dir)
    recon_file = infra.full_recon()

    # 2. Live Host Discovery (httpx)
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

    # 3. Advanced Spidering (Katana)
    print("\n[*] Phase 3: Advanced Spidering (Katana)")
    spider = SpiderModule(live_hosts_file, output_dir)
    spider.run_katana()

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
        "critical_count": 0, # Placeholder for Nuclei integration in next version
        "recon_summary": ""
    }

    if os.path.exists(recon_file):
        with open(recon_file, "r") as f:
            lines = f.readlines()
            stats["subdomains_count"] = len(lines)
            stats["recon_summary"] = "".join(lines[:10]) + ("\n..." if len(lines) > 10 else "")

    # 4. Visual Reporting
    dash = DashboardModule(target, output_dir)
    dash.generate(stats)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"\n✅ [AstraBounty] Mission Completed in {duration}")
    print(f"[+] Final Dashboard: {dash.dashboard_file}\n")

if __name__ == "__main__":
    main()
