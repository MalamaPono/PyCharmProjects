# REGEX FINAL QWIKLABS ASSIGNMENT 3 WORKING WITH LOG FILES, REGEX, AND SYSTEM COMMANDS TO GENERATE
# AUTOMATIC REPORTS THAT ARE USEFUL:

#!/usr/bin/env python3
import re
import csv
error_messages = {}
user_entries = {}

with open('syslog.log') as file:
    for log in file:
        log = log.strip()
        if re.search('ERROR',log) != None:
            pattern = r'ERROR (.+) \((.+)\)'
            match_object = re.search(pattern, log)
            error_type = match_object.group(1)
            user = match_object.group(2)
            error_messages[error_type] = error_messages.get(error_type,0)+1
            user_entries[user] = user_entries.get(user,{})
            user_entries[user]['error'] = user_entries[user].get('error',0)+1
        # else its an info log
        else:
            pattern = r'INFO.+\((.+)\)'
            match_object = re.search(pattern,log)
            user = match_object.group(1)
            user_entries[user] = user_entries.get(user, {})
            user_entries[user]['info'] = user_entries[user].get('info', 0) + 1

error_messages = sorted(error_messages.items(),key=lambda item:item[1],reverse=True)
user_entries = sorted(user_entries.items())

with open('error_message.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(('Error','Count'))
    for error in error_messages:
        writer.writerow(error)

with open('user_statistics.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(("Username", "INFO", "ERROR"))
    for user in user_entries:
        data = []
        data.append(user[0])
        data.append(user[1].get('info',0))
        data.append(user[1].get('error',0))
        writer.writerow(data)



