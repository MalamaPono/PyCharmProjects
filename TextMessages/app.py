import ssl

PROVIDERS = {
    "AT&T": {"sms": "txt.att.net", "mms": "mms.att.net", "mms_support": True},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "mms": "myboostmobile.com",
        "mms_support": True,
    },
    "C-Spire": {"sms": "cspire1.com", "mms_support": False},
    "Cricket Wireless": {
        "sms": "sms.cricketwireless.net ",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
    },
    "Consumer Cellular": {"sms": "mailmymobile.net", "mms_support": False},
    "Google Project Fi": {"sms": "msg.fi.google.com", "mms_support": True},
    "Metro PCS": {"sms": "mymetropcs.com", "mms_support": True},
    "Mint Mobile": {"sms": "mailmymobile.net", "mms_support": False},
    "Page Plus": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "mms_support": False,
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "mms": "pm.sprint.com",
        "mms_support": True,
    },
    "Straight Talk": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "T-Mobile": {"sms": "tmomail.net", "mms_support": True},
    "Ting": {"sms": "message.ting.com", "mms_support": False},
    "Tracfone": {"sms": "", "mms": "mmst5.tracfone.com", "mms_support": True},
    "U.S. Cellular": {
        "sms": "email.uscc.net",
        "mms": "mms.uscc.net",
        "mms_support": True,
    },
    "Verizon": {"sms": "vtext.com", "mms": "vzwpix.com", "mms_support": True},
    "Virgin Mobile": {
        "sms": "vmobl.com",
        "mms": "vmpix.com",
        "mms_support": True,
    },
    "Xfinity Mobile": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
}

import smtplib
from email.message import EmailMessage
import os.path
import mimetypes

def send_email(sender,phone,carrier,subject,body,password,amount):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = phone + '@' + PROVIDERS[carrier]['sms']
    message.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ssl.create_default_context()) as mail_server:
        mail_server.login(sender, password)
        for i in range(amount):
            mail_server.send_message(message)

# media includes photos or videos
def send_media(sender,phone,carrier,subject,body,password,amount,attachment_paths):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    # this is cause T-Mobile sends multimedia through the same sms portal. Doesn't have specific mms portal
    if carrier != 'T-Mobile':
        message['To'] = phone + '@' + PROVIDERS[carrier]['mms']
    else:
        message['To'] = phone + '@' + PROVIDERS[carrier]['sms']
    message.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ssl.create_default_context()) as mail_server:
        mail_server.login(sender, password)
        for i in range(amount):
            mail_server.send_message(message)

    if attachment_paths != None:
        for file in attachment_paths:
            mime_type, _ = mimetypes.guess_type(file)

            index = mime_type.index('/')
            mime = mime_type[:index]
            subtype = mime_type[index+1:]

            with open(file, 'rb') as attachment:
                message.add_attachment(attachment.read(),maintype=mime,subtype=subtype,filename=os.path.basename(file))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as mail_server:
        mail_server.login(sender, password)
        for i in range(amount):
            mail_server.send_message(message)

sender = 'yougothackedbro69420@gmail.com'
phone = '8087455820'
carrier = 'T-Mobile'
subject = ''

body = "I will break your phone"
password = 'cjbisuagsddckabb'
amount = 1
attachment_paths = ['/Users/malamapono/Desktop/einstein.jpg']

# send_email(sender,phone,carrier,subject,body,password,amount)
send_media(sender,phone,carrier,subject,body,password,amount,attachment_paths)


# mpono app password - rstaccqtruorfkem
# hacked app password - cjbisuagsddckabb