# 🔍 URL Health Monitor Tool

A Python-based tool to check the health of multiple URLs, log their status, and send email alerts when any are down. Designed for lightweight monitoring and suitable for real-time scheduling via Task Scheduler.

## 🛠️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/PreethamMadhamsetty/URL_health_monitor_tool.git
   cd URL_health_monitor_tool
   
2. **Install Dependencies**
It is recommended to create a virtual environment first
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

3. **Preparing Environment file**
   ```bash
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   EMAIL_RECIPIENTS=recipient1@gmail.com,recipient2@gmail.com
⚠️ If you're using Gmail with 2-step verification, generate an App Password from your Google account.

4. **Add URLs to monitor**
Add all target URLs (one per line) in the urls.txt file. Example:
   ```bash
   https://example.com
   https://github.com
   https://httpstat.us/404

5. **Run the tool manually**
To test the tool:
   ```bash
   python -m monitor

**Automating with Task Scheduler**
Create a .bat file (e.g., run_health_check.bat) with the following content:
   ```bash
   @echo off
   cd /d "C:\Path\To\Your\Project"
   call .venv\Scripts\activate.bat
   python -m monitor




