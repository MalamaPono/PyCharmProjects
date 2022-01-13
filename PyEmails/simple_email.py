import smtplib
from email.message import EmailMessage
# Now to actually send the message we use the help of the smtplib in python. This uses the standard
# Simple Mail Transfer Protocol (SMTP) that allows different computers to send emails to each other.

password = 'rstaccqtruorfkem'
sender = 'mpono000@gmail.com'

message = EmailMessage()
message['Subject'] = "First Email"
message['From'] = sender
message['To'] = 'mpono000@gmail.com'
message.set_content('Yes it worked!')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail_server:
    mail_server.login(sender, password)
    mail_server.send_message(message)