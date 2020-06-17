import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

file = open('releases.txt')


def send_email(send_to_address):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = EmailMessage()
        msg['Subject'] = 'New Music Friday'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = send_to_address
        msg.set_content(file.read())
        smtp.send_message(msg)
