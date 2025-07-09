# 🔍 URL Health Monitor Tool
A lightweight Python-based tool to monitor the health of web application URLs. The tool checks status codes, logs results to a daily file, sends email alerts when URLs are down, and can be scheduled to run automatically every few minutes.
---
## 📌 Features

- ✅ Check the health of multiple URLs from a file
- 📋 Log results to a daily rotating log file
- 📧 Email alerts when URLs are down
- 🕒 Run every 5 minutes using Windows Task Scheduler
- 📦 Install and run as a Python CLI package

---

## 📂 Project Structure
url_health_monitor_tool/
├── monitor/
│ ├── logger.py
│ ├── mailer.py
│ ├── checker.py
│ └── main.py
├── urls.txt
├── requirements.txt
├── .gitignore
├── README.md
└── setup.py

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PreethamMadhamsetty/URL_health_monitor_tool.git
cd URL_health_monitor_tool

** ### 2. Install Dependencies **
pip install -r requirements.txt

** ###
