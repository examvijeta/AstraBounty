import os

class DashboardModule:
    """Generates a modern HTML dashboard for AstraBounty results."""

    def __init__(self, target, output_dir):
        self.target = target
        self.output_dir = output_dir
        self.dashboard_file = os.path.join(output_dir, "dashboard.html")

    def generate(self, stats):
        """Creates an HTML file with the scan results and statistics."""
        print(f"[*] Generating Visual Dashboard for {self.target}...")
        
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AstraBounty - {self.target}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }}
        .container {{ max-width: 1200px; margin: auto; }}
        .header {{ border-bottom: 2px solid #238636; padding-bottom: 10px; margin-bottom: 30px; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .stat-card {{ background: #161b22; padding: 20px; border-radius: 8px; border: 1px solid #30363d; text-align: center; }}
        .stat-value {{ font-size: 2em; color: #238636; font-weight: bold; }}
        .section {{ margin-bottom: 40px; }}
        h2 {{ color: #58a6ff; }}
        pre {{ background: #010409; padding: 15px; border-radius: 5px; overflow-x: auto; border: 1px solid #30363d; }}
        .footer {{ text-align: center; margin-top: 50px; font-size: 0.8em; color: #8b949e; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 AstraBounty Dashboard: {self.target}</h1>
            <p>Scan completed: {stats.get('date', 'N/A')}</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Subdomains</div>
                <div class="stat-value">{stats.get('subdomains_count', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Live Hosts</div>
                <div class="stat-value">{stats.get('live_hosts_count', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Endpoints</div>
                <div class="stat-value">{stats.get('endpoints_count', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Secrets Found</div>
                <div class="stat-value" style="color: #ff9d00;">{stats.get('secrets_count', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Critical Findings</div>
                <div class="stat-value" style="color: #da3633;">{stats.get('critical_count', 0)}</div>
            </div>
        </div>

        <div class="section">
            <h2>🔍 Discovered Attack Surface</h2>
            <p>Target infrastructure overview:</p>
            <pre>{stats.get('recon_summary', 'No recon data available.')}</pre>
        </div>

        <div class="footer">
            Built with AstraBounty &copy; 2026
        </div>
    </div>
</body>
</html>
"""
        with open(self.dashboard_file, "w") as f:
            f.write(html_template)
        
        print(f"[+] Dashboard ready at: {self.dashboard_file}")
        return self.dashboard_file
