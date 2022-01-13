from email.message import EmailMessage
import os.path
import smtplib

message = EmailMessage()

sender = 'mpono000@gmail.com'
password = 'rstaccqtruorfkem'

message['From'] = sender
message["To"] = 'mpono000@gmail.com'
# to send to multiple emails here, just enter a python list of emails here or enter a string with commas
# separating each different email
message['Subject'] = 'Greetings, I have an html email'

message.set_content("""This is a plain text email that is only triggered if the receiver 
of this email has html emails turned off""")

message.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""",subtype='html')


# send the message we made
with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail_server:
    mail_server.login(sender, password)
    mail_server.send_message(message)