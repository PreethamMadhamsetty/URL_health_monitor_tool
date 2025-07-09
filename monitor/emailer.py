# monitor/emailer.py
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import logging

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS", "").split(",")

def send_email_alert(down_urls):
    if not down_urls:
        return

    subject = "🚨 URL Health Alert"
    body = "The following URLs are DOWN:\n\n" + "\n".join(down_urls)

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = ", ".join(EMAIL_RECIPIENTS)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("[EMAIL SENT] Alert sent.")
        logging.info("Alert email sent.")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        logging.error(f"Email send failed: {e}")
