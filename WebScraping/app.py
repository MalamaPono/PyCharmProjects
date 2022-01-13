from selenium import webdriver
import pandas as pd
import requests
import json

api_key = 'AIzaSyAARWd4u9zkHEIhst5pLp59BIqa51m3Izg'
part = 'statistics'
video_id = 'Fp8msa5uYsc'
url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}'
json_url = requests.get(url)
data = json.loads(json_url.text)
print(json.dumps(data,indent=2))

