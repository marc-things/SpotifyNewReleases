import os
import smtplib

email = 'test@email'
password = 'test_password'
file = open('releases.txt', 'r')
data = file.read()

def send_email():
    with smtplib.SMTP('localhost', 1025) as smtp:

        subject = 'New Music Friday'
        body = data

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email, 'user@email.com', msg)
