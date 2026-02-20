# 🚀 AstraBounty Framework

**AstraBounty** is a powerful, 2026-ready reconnaissance and vulnerability discovery framework designed for professional Bug Bounty hunters and Penetration Testers. It automates the most time-consuming phases of security research, providing a surgical and comprehensive attack surface analysis.

---

## ✨ Key Features

- **🌐 Infrastructure Mapping (v2.0):** Deep DNS enumeration integrating OWASP Amass and Subfinder to discover hidden subdomains.
- **🕷️ Advanced Spidering:** Leverages ProjectDiscovery's Katana for deep crawling, JS file extraction, and endpoint discovery.
- **🔍 API & Parameter Hunting:** Integrated Ffuf and Arjun for ultra-fast directory brute-forcing and hidden parameter discovery.
- **📊 Interactive Visual Dashboard:** Generates a modern, dark-themed HTML dashboard to visualize the attack surface and vulnerabilities instantly.
- **⚡ High Performance:** Multi-threaded orchestration written in Python.
- **🔱 God Mode (NEW):** Historic data scraping (Wayback) and automated Secret/API Key hunting.
- **🔔 Real-time Alerts:** Integrated Discord/Telegram notifications for critical findings.

---

## 🛠️ Installation

### 1. Prerequisites (External Tools)
AstraBounty relies on several high-performance security utilities. Ensure the following are installed and available in your PATH:

**Go Tools:**
```bash
# Subdomain Discovery
go install -v github.com/owasp-amass/amass/v3/...@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Spidering & Scanning
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Fuzzing
go install -v github.com/ffuf/ffuf@latest
```

### 2. Python Setup
Clone the repository and install the dependencies:
```bash
git clone https://github.com/examvijeta/AstraBounty.git
cd AstraBounty
pip install -r requirements.txt
```

---

---

## 🚀 Usage Guide & Examples

Run a mission using the features you need. Here are the most common scenarios:

### 1. Simple Recon (Fast)
Just find subdomains and check if they are live.
```bash
python astrabounty.py -d tesla.com
```

### 2. Deep Infrastructure Mapping
Use this to find subdomains that are hidden behind complex DNS layers (Requires Amass).
```bash
python astrabounty.py -d tesla.com --deep
```

### 3. God Mode: Extreme Intelligence
Fetch all historic URLs from the last 10 years and scan them for leaked API keys/secrets.
```bash
python astrabounty.py -d tesla.com --god-mode
```

### 4. Full Power with Real-time Alerts (Discord)
Run God Mode and get notified on Discord the moment a secret is found.
```bash
python astrabounty.py -d tesla.com --god-mode --webhook "https://discord.com/api/webhooks/your-id/your-token"
```

### 5. Full Power with Real-time Alerts (Telegram)
Get alerts on your Telegram phone.
```bash
python astrabounty.py -d tesla.com --god-mode --tg-token "123456:ABC-DEF" --tg-chat-id "987654321"
```

### 5. Custom Output Directory
Save your mission data in a specific folder.
```bash
python astrabounty.py -d tesla.com -o myscans/tesla_report
```

---

## ⚙️ Setup Instructions

### 1. Webhook Setup (Discord)
1. Open your Discord server and go to **Server Settings > Integrations**.
2. Click **Webhooks > New Webhook**.
3. Copy the **Webhook URL** and use it with the `--webhook` flag.

### 2. Webhook Setup (Telegram)
1. Message `@BotFather` on Telegram to create a bot and get your **API Token**.
2. Get your **Chat ID** using `@userinfobot`.
3. Use these with the `--tg-token` and `--tg-chat-id` flags.

### 3. Amass Config (For --deep)
To make the `--deep` mode even more powerful, add API keys (Shodan, SecurityTrails, etc.) to your Amass config:
- Create a file at `~/.config/amass/config.ini`.
- Follow the [Amass Official Guide](https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-configuration-file) to add keys.

---

## ⚙️ How It Works

AstraBounty follows a systematic 4-phase methodology:

1.  **Reconnaissance:** Maps the entire DNS infrastructure to find subdomains that others miss.
2.  **Surface Analysis:** Probes subdomains for live hosts and identifies technologies used.
3.  **Endpoint Discovery:** Deep-crawls applications to extract APIs, JS files, and hidden parameters.
4.  **Reporting:** Consolidates all data into an interactive HTML dashboard for easy analysis.

---

## 🛡️ Ethical Hacking Disclaimer

**AstraBounty** is created for ethical hacking and educational purposes only. Users must have explicit authorized permission via a Bug Bounty Program or written consent before scanning any target. The developers assume no liability for any misuse or damage caused by this tool.

---

**Built with ❤️ for the Security Community.**
