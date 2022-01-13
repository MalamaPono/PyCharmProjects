from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generateEmail(sender, receiver, subject, body, attachment_paths=None):
    message = EmailMessage()

    message['From'] = sender
    message["To"] = receiver
    # to send to multiple emails here, just enter a python list of emails here or enter a string with commas
    # separating each different email
    message['Subject'] = subject
    message.set_content(body)

    # add an attachment like an image, pdf, word document, video, csv, and more.
    # If you know the type of the attachment, look on mimetypes documentation to add the mimetype and the subtype.
    # If not use the mimetypes guess_type method of the attachment.

    # attach all the attachments
    if attachment_paths != None:
        for file in attachment_paths:
            mime_type, _ = mimetypes.guess_type(file)

            index = mime_type.index('/')
            mime = mime_type[:index]
            subtype = mime_type[index+1:]

            with open(file, 'rb') as attachment:
                message.add_attachment(attachment.read(),maintype=mime,subtype=subtype,filename=os.path.basename(file))

    return message

def sendEmail(message,sender,password):
    # send the message we made
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail_server:
        mail_server.login(sender, password)
        mail_server.send_message(message)


sender = 'mpono000@gmail.com'
password = 'rstaccqtruorfkem'
subject = 'Greetings, I have an attachment to show you'
body = """Aloha kumu,
            Can i change my schedule? Also, take a lott at my attachment."""
file_paths = ['example.png', '/Users/malamapono/Desktop/tiger.jpg']

email = generateEmail(sender,sender,subject,body,file_paths)
sendEmail(email,sender,password)