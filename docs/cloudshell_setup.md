# 🐚 Google Cloud Shell Setup (No Sudo)

Google Cloud Shell is a restricted environment where you do NOT have `sudo` access. However, you can still install all AstraBounty tools using **Go** and **Python User Mode**.

## 🛠️ Installation Steps

### 1. Update PATH Environment
Run this first so your terminal can "find" the tools after you install them:
```bash
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc
```

### 2. Install Bug Bounty Tools (No Sudo Required)
Run these commands one by one to install the engine components:

```bash
# Install Subfinder (Infrastructure)
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Install Httpx (Live Host Discovery)
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Install Katana (Spidering)
go install -v github.com/projectdiscovery/katana/cmd/katana@latest

# Install Nuclei (Vulnerability Scanner)
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Install Dalfox (XSS Scanner)
go install -v github.com/hahwul/dalfox/v2@latest

# Install JSLuice (JS Intelligence)
go install -v github.com/bishopfox/jsluice/cmd/jsluice@latest
```

### 3. Install Python Dependencies
```bash
cd AstraBounty
pip install -r requirements.txt
```

---

## ✅ Verify Installation
Check if the tools are working by running:
```bash
subfinder -version
httpx -version
nuclei -version
```

If you see a version number, you are ready to launch **OmniMode**! 🚀🛡️💻🦾
