# 🔱 Amass Configuration Guide (Deep Recon)

Adding a config file to Amass is like giving your toolkit **X-ray vision**. By default, Amass uses public sources, but with API keys, it can tap into massive premium databases for free.

## 🚀 Benefits of Amass Config

1.  **More Subdomains:** Access private databases like Shodan, SecurityTrails, Censys, etc.
2.  **Higher Accuracy:** Verified data from paid providers (often has free tiers).
3.  **Discovery of IP Spaces:** Find entire server ranges (CIDRs) owned by a company.
4.  **Avoid Rate Limiting:** Using your own API keys ensures you don't get blocked by aggressive global rate limits.

---

## 🛠️ Setup Instructions

### 1. Create the Config Directory
On Linux/VPS:
```bash
mkdir -p ~/.config/amass/
```
On Windows:
Create a folder at `C:\Users\YourUser\AppData\Roaming\amass\`

### 2. Create the `config.ini` File
Download the [Official Template](https://github.com/owasp-amass/amass/blob/master/examples/config.ini) or create a simple one like this:

```ini
# ~/.config/amass/config.ini

# How long to wait for each data source
timeout = 15

[datasources]
# Paste your API keys here
[datasources.Shodan]
apikey = YOUR_SHODAN_KEY

[datasources.SecurityTrails]
apikey = YOUR_SECURITYTRAILS_KEY

[datasources.Censys]
id = YOUR_CENSYS_ID
secret = YOUR_CENSYS_SECRET

[datasources.BinaryEdge]
apikey = YOUR_BINARYEDGE_KEY
```

---

## 🔑 Where to get FREE API Keys?

You don't need to pay. These providers have generous **Free Tiers**:

| Provider | Why use it? | Get it here |
| --- | --- | --- |
| **Shodan** | Finds open ports and services | [shodan.io](https://www.shodan.io/) |
| **SecurityTrails** | Best for historic DNS recon | [securitytrails.com](https://securitytrails.com/) |
| **Censys** | Deep IP search | [censys.io](https://censys.io/) |
| **BinaryEdge** | Scans the entire internet | [binaryedge.io](https://www.binaryedge.io/) |
| **AlienVault** | Global threat intelligence | [otx.alienvault.com](https://otx.alienvault.com/) |

---

## 🏃 How to use with AstraBounty

Once the file is at `~/.config/amass/config.ini`, AstraBounty will automatically use it when you run:

```bash
python astrabounty.py -d target.com --deep
```
Amass will detect the config file and unleash the power of all your integrated API keys!
