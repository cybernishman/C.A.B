from slack_sdk import WebClient
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Slack token from environment
slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

def send_quiz_question():
    quiz_questions = [
        {
            "question": "What should you do if you receive an email from an unknown source?",
            "options": ["A) Open it immediately", "B) Click all links", "C) Verify sender and be cautious", "D) Forward to everyone"],
            "answer": "C"
        },
        {
            "question": "What is the safest way to manage your passwords?",
            "options": ["A) Write them down", "B) Use same password everywhere", "C) Use a password manager", "D) Share with a friend"],
            "answer": "C"
        },
        {
            "question": "What is phishing?",
            "options": ["A) A type of fishing", "B) A cyberattack to steal sensitive information", "C) A harmless email", "D) A secure way to communicate"],
            "answer": "B"
        },
        {
            "question": "What should you do if you suspect a website is fake?",
            "options": ["A) Enter your credentials to check", "B) Close the website immediately", "C) Report it to IT", "D) Both B and C"],
            "answer": "D"
        },
        {
            "question": "What is two-factor authentication (2FA)?",
            "options": ["A) A single password", "B) A backup password", "C) An additional layer of security", "D) A type of malware"],
            "answer": "C"
        },
        {
            "question": "What is the best way to secure your Wi-Fi network?",
            "options": ["A) Use a strong password", "B) Leave it open for guests", "C) Use default settings", "D) Disable encryption"],
            "answer": "A"
        },
        {
            "question": "What is ransomware?",
            "options": ["A) A type of antivirus", "B) A type of malware that demands payment", "C) A secure file-sharing tool", "D) A password manager"],
            "answer": "B"
        },
        {
            "question": "How often should you update your software?",
            "options": ["A) Never", "B) Only when prompted", "C) Regularly to apply security patches", "D) Once a year"],
            "answer": "C"
        },
        {
            "question": "What is the purpose of a firewall?",
            "options": ["A) To block all internet traffic", "B) To monitor and control incoming/outgoing traffic", "C) To speed up your internet", "D) To store passwords"],
            "answer": "B"
        },
        {
            "question": "What should you do if you lose your work laptop?",
            "options": ["A) Ignore it", "B) Report it immediately", "C) Try to track it yourself", "D) Buy a new one"],
            "answer": "B"
        },
        {
            "question": "What is a VPN used for?",
            "options": ["A) To browse the internet faster", "B) To create a secure connection over the internet", "C) To block ads", "D) To download files"],
            "answer": "B"
        },
        {
            "question": "What is social engineering?",
            "options": ["A) A type of malware", "B) Manipulating people to reveal confidential information", "C) A secure way to share data", "D) A type of encryption"],
            "answer": "B"
        },
        {
            "question": "What is the best practice for creating a strong password?",
            "options": ["A) Use your name and birthdate", "B) Use a mix of letters, numbers, and symbols", "C) Use 'password123'", "D) Use the same password everywhere"],
            "answer": "B"
        },
        {
            "question": "What should you do if you receive a suspicious link?",
            "options": ["A) Click it to check", "B) Ignore it", "C) Verify its source before clicking", "D) Forward it to others"],
            "answer": "C"
        },
        {
            "question": "What is the primary goal of cybersecurity?",
            "options": ["A) To annoy hackers", "B) To protect sensitive information", "C) To slow down computers", "D) To block all internet access"],
            "answer": "B"
        }
    ]
    
    quiz = random.choice(quiz_questions)
    options_text = "\n".join(quiz["options"])
    
    message = f"🛡️ *Cybersecurity Quiz Question:* \n\n{quiz['question']}\n\n{options_text}\n\n*(Reply with A, B, C, or D)*"
    try:
        client.chat_postMessage(channel='#general', text=message)
    except Exception as e:
        print(f"Error sending quiz: {e}")
