#!/usr/bin/env python3

import os
import reports
import datetime
import emails

def process_data():
    # path = os.path.expanduser('~') + '/supplier-data/descriptions/'
    path = 'supplier-data/descriptions'
    keys = ['name','weight','description']
    dics = []
    for filename in os.listdir(path):
        index = 0
        dic = {}
        with open(os.path.join(path, filename)) as file:
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                dic[keys[index]] = line
                if index == 2:
                    dic[keys[index]] = '<br/>'
                index += 1
        dics.append(dic)
    return dics

def main():
    dics = process_data()
    paragraph = ""
    for dic in dics:
        for key,value in dic.items():
            if key == 'name':
                paragraph+='name: ' + value + '<br/>'
            if key == 'weight':
                paragraph += 'weight: '+value + '<br/>'
            if key == 'description':
                paragraph += '<br/>'

    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    title = "Processed Update on " + timestampStr + "<br/><br/>"
    reports.generate_report('processed.pdf', title, paragraph)

    sender = 'mpono000@gmail.com'
    reciever = 'mpono000@gmail.com'
    title = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    password = 'rstaccqtruorfkem'

    email = emails.generate(sender, reciever, title, body,'processed.pdf')
    emails.send_email(email,sender,password)

if __name__ == "__main__":
    main()
