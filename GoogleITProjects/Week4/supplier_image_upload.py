#!/usr/bin/env python3
import os

import requests

# This example shows how a file can be uploaded using
# The Python Requests module

path = os.path.expanduser('~') + '/supplier-data/images/'
url = "http://localhost/upload/"
for filename in os.listdir(path):
    if filename == 'README' or filename == "LICENSE":
        continue
    with open(os.path.join(path,filename), 'rb') as opened:
        r = requests.post(url, files={'file': opened})