import requests

class Notifier:
    """Sends real-time alerts to Discord or Telegram."""

    def __init__(self, webhook_url=None, telegram_token=None, telegram_chat_id=None):
        self.webhook_url = webhook_url
        self.tg_token = telegram_token
        self.tg_chat_id = telegram_chat_id

    def send_discord(self, message):
        if not self.webhook_url: return
        data = {"content": f"🚀 **AstraBounty Alert**\n{message}"}
        try:
            requests.post(self.webhook_url, json=data)
        except:
            pass

    def send_telegram(self, message):
        if not (self.tg_token and self.tg_chat_id): return
        url = f"https://api.telegram.org/bot{self.tg_token}/sendMessage"
        data = {"chat_id": self.tg_chat_id, "text": f"🚀 AstraBounty Alert\n{message}"}
        try:
            requests.post(url, json=data)
        except:
            pass

    def send_document(self, file_path):
        """Sends a file/document to Telegram."""
        if not (self.tg_token and self.tg_chat_id): return
        if not os.path.exists(file_path): return
        
        url = f"https://api.telegram.org/bot{self.tg_token}/sendDocument"
        try:
            with open(file_path, "rb") as f:
                requests.post(url, data={"chat_id": self.tg_chat_id}, files={"document": f})
        except Exception as e:
            print(f"[!] Telegram File Send Error: {e}")

    def send_error(self, error_msg):
        """Sends error logs to configured channels."""
        msg = f"❌ ERROR: {error_msg}"
        self.send_discord(msg)
        self.send_telegram(msg)
