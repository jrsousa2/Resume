# THIS CODE IS A CLONE OF THE CODE UNDER REPO PYTHON
# THE DIFFERENCE IS THAT THIS ONE IS SCHEDULED ON GITHUB

import yfinance as yf
import smtplib
from email.message import EmailMessage
from os import environ

# YOUR E-MAIL
Email = environ["GMAIL_APP_SMTP_EMAIL"]

# E-MAIL ACCT PWD
APP_PASSWORD = environ["GMAIL_APP_SMTP_PASSWORD"]
APP_PASSWORD = APP_PASSWORD.replace(" ", "")

# TICKER SYMBOL
Ticker = environ["TICKER1_VALUE"] 
Target = float(environ["TICKER1_TARGET"])

# CODE
data = yf.Ticker(Ticker).history(period="1d")

if data.empty:
    raise RuntimeError("No price data returned")

price = data["Close"].iloc[-1]

if price > Target:
    msg = EmailMessage()
    msg.set_content(f"{Ticker} is above {Target}: {price}")
    msg["Subject"] = Ticker + " Stock Alert"
    msg["From"] = Email 
    msg["To"] = Email 

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(Email , APP_PASSWORD)
        s.send_message(msg)
else:
    print("\nPrice is not above target:",Target,"\n")        