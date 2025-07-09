# monitor/checker.py
import requests
import logging

def check_url_health(url):
    try:
        response = requests.get(url, timeout=10)
        code = response.status_code

        if 200 <= code < 300:
            msg = f"[{code}] UP - Success for {url}"
        elif 300 <= code < 400:
            msg = f"[{code}] Redirected for {url}"
        elif 400 <= code < 500:
            msg = f"[{code}] Client Error - Not Found or Unauthorized for {url}"
        elif 500 <= code < 600:
            msg = f"[{code}] Server Error for {url}"
        else:
            msg = f"[{code}] Unknown Status for {url}"

        print(msg)
        logging.info(msg)
        return True if code < 400 else False

    except requests.exceptions.ConnectTimeout:
        msg = f"[TIMEOUT] Connection too long for {url}"
    except requests.exceptions.ConnectionError:
        msg = f"[DOWN] Connection failed for {url}"
    except requests.exceptions.RequestException as e:
        msg = f"[ERROR] {url} - {str(e)}"

    print(msg)
    logging.error(msg)
    return False
