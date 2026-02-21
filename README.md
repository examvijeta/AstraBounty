# 🌌 AstraBounty: The God Mode Bounty Framework

**AstraBounty** is a fully autonomous, 2026-ready reconnaissance and vulnerability discovery framework. It is designed to find what others miss by going deeper and wider without manual intervention.

---

## ✨ OmniMode Features (Extreme Power)

- **🌌 OmniMode (ULTIMATE):** The "Auto-Hack" button. Recon -> Intelligence -> Vulnerability Analysis.
- **🔱 God Mode:** Historic data scraping from Wayback Machine to find leaked keys.
- **🕷️ Advanced Spidering:** Deep crawling and JS intelligence via Katana.
- **☢️ Autonomous Vuln Scan:** Nuclei & Dalfox integration for high-impact bugs.
- **🔔 Real-time Alerts:** Integrated Discord/Telegram notifications.
- **📊 Visual Dashboard:** Modern HTML report for quick triage.

---

## 🚀 Get Started

### 1. Installation
```bash
git clone https://github.com/examvijeta/AstraBounty.git
cd AstraBounty
pip install -r requirements.txt
```

### 🌌 2. OmniMode: Fully Autonomous
Run the ultimate scan with deep recon and automated vulnerability discovery.
```bash
python astrabounty.py -d target.com --omni --tg-token "BOT" --tg-chat-id "ID"
```

### 🔱 3. God Mode: Historic Secrets
```bash
python astrabounty.py -d target.com --god-mode
```

---

## ⚙️ Configuration & Compliance

### Amass API Keys (Deep Recon)
Add your keys to `config.ini` for maximum discovery:
```ini
[datasources.Shodan]
apikey = YOUR_KEY
```

### Compliance Headers (Robinhood etc.)
Stay legal by identifying yourself to the target:
```bash
python astrabounty.py -d target.com --h1-user "gaurav_hacker" --email "gaurav@email.com"
```

---

## 🔗 Credits & Tooling
Built on top of the world's best security tools:
- `Amass` & `Subfinder` (Infra)
- `Httpx` (Discovery)
- `Katana` (Spider)
- `Nuclei` & `Dalfox` (Autonomous Vulns)
- `FFUF` (Fuzzing)

🚀 **Happy Hunting with AstraBounty!**
