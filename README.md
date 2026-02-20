# 🚀 AstraBounty Framework

**AstraBounty** is a powerful, 2026-ready reconnaissance and vulnerability discovery framework designed for professional Bug Bounty hunters and Penetration Testers. It automates the most time-consuming phases of security research, providing a surgical and comprehensive attack surface analysis.

---

## ✨ Key Features

- **🌐 Infrastructure Mapping (v2.0):** Deep DNS enumeration integrating OWASP Amass and Subfinder to discover hidden subdomains.
- **🕷️ Advanced Spidering:** Leverages ProjectDiscovery's Katana for deep crawling, JS file extraction, and endpoint discovery.
- **🔍 API & Parameter Hunting:** Integrated Ffuf and Arjun for ultra-fast directory brute-forcing and hidden parameter discovery.
- **📊 Interactive Visual Dashboard:** Generates a modern, dark-themed HTML dashboard to visualize the attack surface and vulnerabilities instantly.
- **⚡ High Performance:** Multi-threaded orchestration written in Python for maximum speed.

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
git clone https://github.com/examvijeta/bug-bounty.git
cd bug-bounty
pip install -r requirements.txt
```

---

## 🚀 Usage

Run a deep mission against any authorized target:

```bash
python astrabounty.py -d target-domain.com --deep
```

### Command Line Options:
- `-d`, `--domain`: Target domain to scan (Required).
- `-o`, `--output`: Directory to save results (Default: `astra_results`).
- `--deep`: Enable intensive recon mode using Amass.

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
