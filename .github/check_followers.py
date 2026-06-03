import requests
import json
import os
import smtplib
from email.mime.text import MIMEText

USERNAME = "jrsousa2"

# THE GH API TOKEN I CREATED
TOKEN = os.environ["GH_TOKEN"]

# EMAIL ADRESS
EMAIL_USER = os.environ["GMAIL_APP_SMTP_EMAIL"]
EMAIL_TO = os.environ["GMAIL_APP_SMTP_EMAIL"]

# EMAIL PWD
EMAIL_PASS = os.environ["GMAIL_APP_SMTP_PASSWORD"]
EMAIL_PASS = EMAIL_PASS.replace(" ", "")

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

url = f"https://api.github.com/users/{USERNAME}/followers"
resp = requests.get(url, headers=headers)
# CHECK STATUS FIST 
resp.raise_for_status()

followers = sorted([f["login"] for f in resp.json()])

# load old followers
try:
    with open("followers.json", "r") as f:
        old_followers = json.load(f)
except FileNotFoundError:
    old_followers = []


new_followers = list(set(followers) - set(old_followers))

def send_email(new_list):
    body = "New GitHub follower(s):\n\n" + "\n".join(new_list)

    msg = MIMEText(body)
    msg["Subject"] = "GitHub New Follower Alert"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())

if new_followers:
    print("New followers:", new_followers)
    send_email(new_followers)

# save current state
with open("followers.json", "w") as f:
    json.dump(followers, f)