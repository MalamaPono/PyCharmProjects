
# this script opens the youtube video whenever one of you favorite youtubers who you choose,
# uploads a video.

from urllib import request
import json
from selenium import webdriver
import time

def look_for_new_video():
    api_key = "AIzaSyD0LtC4Z-pBY-UBTXyks56e7aUisf2Nl8I"
    channel_id ='UC1qPz83jepTv3znHZqLEc'
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelid={}$part=snippet,id&order=date&maxResults=1'.format(api_key,channel_id)
    inp = request.urlopen(url)
    response = json.load(inp)

    print(response)

    vidID = response['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json','r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            PATH = '/Users/malamapono/chromedriver'
            driver = webdriver.Chrome(PATH)
            driver.get(base_video_url + vidID)
            video_exists = True

    if video_exists:
        with open('videoid.json','w') as json_file:
            data = {'videoId':vidID}
            json.dump(data,json_file)

try:
    while True:
        look_for_new_video()
        time.sleep(20)
except KeyboardInterrupt:
    print('stopping the search')





