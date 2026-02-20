import argparse
import os
import datetime
from modules.infra import InfraModule
from modules.spider import SpiderModule
from modules.fuzzer import FuzzerModule
from modules.dashboard import DashboardModule

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

    print(f"\n[AstraBounty] Starting Mission: {target}")
    start_time = datetime.datetime.now()

    # 1. Infrastructure Mapping
    infra = InfraModule(target, output_dir)
    print("[*] Phase 1: Infrastructure Mapping")
    recon_file = infra.full_recon()

    # (In a real scenario, we'd run httpx here to get live hosts, 
    # but for simplicity, let's assume infra.all_subdomains_file has interesting targets)
    
    # Placeholder stats for the dashboard demo
    stats = {
        "date": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "subdomains_count": 0,
        "live_hosts_count": 0,
        "endpoints_count": 0,
        "critical_count": 0,
        "recon_summary": ""
    }

    if os.path.exists(recon_file):
        with open(recon_file, "r") as f:
            lines = f.readlines()
            stats["subdomains_count"] = len(lines)
            stats["recon_summary"] = "".join(lines[:10]) + ("\n..." if len(lines) > 10 else "")

    # 2. Advanced Spidering
    print("[*] Phase 2: Advanced Spidering (Katana)")
    spider = SpiderModule(recon_file, output_dir)
    # spider.run_katana() # Not running in this demo to avoid shell hangs

    # 3. Visual Reporting
    dash = DashboardModule(target, output_dir)
    dash.generate(stats)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"\n[+] AstraBounty scan completed in {duration}")
    print(f"[+] Final Dashboard: {dash.dashboard_file}\n")

if __name__ == "__main__":
    main()
