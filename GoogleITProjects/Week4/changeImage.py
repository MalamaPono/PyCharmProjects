#!/usr/bin/env python3
import os
from PIL import Image

path = os.path.expanduser('~') + '/supplier-data/images/'
for filename in os.listdir(path):
    if filename == 'README' or filename == "LICENSE":
        continue
    img = Image.open(os.path.join(path,filename))
    os.remove(os.path.join(path,filename))
    new_img = img.convert("RGB").resize((600,400))
    print(os.path.join(path,os.path.basename(filename)[:3] + '.jpeg'))
    new_img.save(os.path.join(path,os.path.basename(filename)[:3] + '.jpeg'))

