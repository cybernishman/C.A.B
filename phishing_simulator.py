from slack_sdk import WebClient
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Slack token from environment
slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

def send_phishing_email():
    fake_emails = [
        "🚨 Your account has been compromised! Click here to reset your password: http://fake-link.com",
        "🎁 Congratulations! You've won a free iPhone. Claim it here: http://scam-link.com",
        "⚡ Immediate action required: Update your payment details: http://fraud-link.com"
    ]
    message = random.choice(fake_emails)
    try:
        client.chat_postMessage(channel='#general', text=f"[PHISHING SIMULATION] {message}")
    except Exception as e:
        print(f"Error sending phishing email: {e}")
