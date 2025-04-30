from slack_sdk import WebClient 
import schedule
import time
import random
import os
from dotenv import load_dotenv

from phishing_simulator import send_phishing_email
from quiz_manager import send_quiz_question

# Load environment variables
load_dotenv()

# Get Slack token from .env
slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

def send_tip():
    tips = [
        "Tip 1: Always verify links before clicking!",
        "Tip 2: Use strong, unique passwords for each account!",
        "Tip 3: Don't connect to unknown Wi-Fi networks!",
        "Tip 4: Keep your software and apps up to date to patch security vulnerabilities!",
        "Tip 5: Enable two-factor authentication on your accounts!",
        "Tip 6: Be cautious about phishing emails or messages!",
        "Tip 7: Regularly back up your data to avoid losing important files!",
        "Tip 8: Use a VPN when browsing on public Wi-Fi!",
        "Tip 9: Secure your devices with a password or biometric authentication!",
        "Tip 10: Always log out of accounts when you're done, especially on shared devices!"
    ]
    message = random.choice(tips)
    try:
        client.chat_postMessage(channel='#general', text=message)
    except Exception as e:
        print(f"Error sending message: {e}")

# Scheduling
schedule.every().monday.at("10:00").do(send_tip)
schedule.every().wednesday.at("10:00").do(send_phishing_email)
schedule.every().friday.at("10:00").do(send_quiz_question)

while True:
    schedule.run_pending()
    time.sleep(1)