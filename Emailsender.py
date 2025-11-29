import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "Your Email "
APP_PASSWORD = "App Passsword  from google "
RECIEVER = "Reciver email"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECIEVER
msg["Subject"] = "Welcome to the world of Python......."
msg.set_content("This email was shared by python code")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
