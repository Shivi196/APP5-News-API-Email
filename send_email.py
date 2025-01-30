import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    sender_email = "sharmabruno310@gmail.com"
    sender_password = os.getenv("PASSWORD")
    user_email = "sharmabruno310@gmail.com"

#     message = '''\
# Subject : Test Email
# In the context of secure communication, an SSL Context is a collection of settings and configurations that define the parameters for establishing a secure connection using SSL/TLS protocols.
# '''
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, message)

# For Setting up environment variable below are steps
# 1. Open terminal
# 2. type in touch ~/.zshrc; open ~/.zshrc
# 3. Write in zshrc file - export PASSWORD="ahbw faam tral qbgo"
# 4. Restart Pycharm and check again in console by typing import os nd then os.getenv("PASSWORD") it should show the value for it
# 5. for more info for this or windows os check Day23 last video of Ardit




