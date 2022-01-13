#! /usr/bin/env python3

import os
import requests

keys = ["name","weight","description"]
path = os.path.expanduser('~') + '/supplier-data/descriptions/'
for filename in os.listdir(path):
    dic = {}
    with open(os.path.join(path,filename)) as file:
        index = 0
        for line in file:
            line = line.strip()
            if line == '':
                continue
            if keys[index] == 'weight':
                line = int(line[:line.find(' ')])
            dic[keys[index]] = line
            index += 1
    number = filename[0:3]
    dic['image_name'] = number + '.jpeg'
    requests.post('http://34.69.61.201/fruits/',json=dic)
