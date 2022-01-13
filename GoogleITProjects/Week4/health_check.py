#!/usr/bin/env python3

import socket
import shutil
import psutil
import os
import emails

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost== "127.0.0.1"

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_available_memory():
    """available memory in linux-instance, in byte"""
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    # converting to megabytes
    return total > 500

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80

to_be_checked = {
    check_cpu_usage(): "CPU usage is over 80%",
    check_disk_usage("/"): "Available disk space is less than 20%",
    check_available_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}


error = False
error_message=  ""
for action, message in to_be_checked.items():
    if not action:
        error_message = message
        error = True
    else:
        error = False

    # If error is true, send the email with the error
    if error:
        try:
            sender = "mpono000@gmail.com"
            receiver = "mpono000@gmail.com"
            subject = "Error - {}".format(error_message)
            body = "Please check your system and resolve the issue as soon as possible"
            password = 'rstaccqtruorfkem'
            message = emails.generate_error_report(sender, receiver, subject, body)
            emails.send_email(message,sender,password)
        except NameError:
            pass