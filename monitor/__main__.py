# monitor/__main__.py
import logging
import os
from datetime import datetime
from .checker import check_url_health
from .emailer import send_email_alert

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    log_file = f"logs/url_health_{datetime.now().strftime('%Y-%m-%d')}.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def read_urls(file="urls.txt"):
    if not os.path.exists(file):
        print(f"[ERROR] File '{file}' not found.")
        return []
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    setup_logger()
    urls = read_urls()
    down_urls = []

    for url in urls:
        is_up = check_url_health(url)
        if not is_up:
            down_urls.append(url)

    if down_urls:
        send_email_alert(down_urls)

if __name__ == "__main__":
    main()
