# ☁️ Google Cloud Platform (GCP) Free Tier Guide

Google Cloud offers an **"Always Free"** tier which is great for beginners, though less powerful than Oracle. It will also ask for a credit/debit card for verification.

## 🚀 What you get for FREE
*   **Virtual Machine:** 1 Free `e2-micro` instance per month.
*   **Resources:** ~2 GB RAM and 2 vCPUs (Shared).
*   **Storage:** 30 GB of Standard persistent disk.
*   **Region:** Must be in `us-west1`, `us-central1`, or `us-east1`.

---

## 🛠️ Step-by-Step Setup

### 1. Sign Up
1. Go to [cloud.google.com/free](https://cloud.google.com/free/).
2. Click **"Get started for free"**.
3. Sign in with your Google account.
4. Fill in your details. **Verification:** You will need to add a card. They might charge ₹1-₹2 and refund it instantly.

### 2. Create your VPS (Compute Engine)
1. Once in the Dashboard, go to **Compute Engine > VM Instances**.
2. Click **Create Instance**.
3. **Name:** `astrabounty-vps`
4. **Region:** Select `us-central1 (Iowa)`.
5. **Machine Configuration:** 
    *   Series: `E2`
    *   Machine Type: `e2-micro` (Look for the "Free tier eligible" badge).
6. **Boot Disk:** Click Change, select `Ubuntu 22.04 LTS` and set size to `30 GB`.
7. **Firewall:** Check both "Allow HTTP traffic" and "Allow HTTPS traffic".
8. Click **Create**.

### 3. Setup AstraBounty on the VPS
Once the VM is running, click the **SSH** button to open the terminal and run:

```bash
# Update and install Python/Git
sudo apt update && sudo apt install -y python3-pip git

# Clone AstraBounty
git clone https://github.com/examvijeta/AstraBounty.git
cd AstraBounty
pip install -r requirements.txt

# Install Go tools (essential for AstraBounty)
sudo apt install -y golang
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc

# Install specific tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

---

## ⚠️ Important Notes
*   **Card Requirement:** GCP is very strict. If you don't have an international-enabled card, it might fail.
*   **Monitoring Costs:** Keep an eye on the "Billing" section to ensure you stay within the free limits.
*   **Performance:** `e2-micro` is small. If you find it slow, avoid running too many tools in parallel inside `astrabounty.py`.
