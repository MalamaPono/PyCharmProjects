from googleapiclient.discovery import build
import requests
import json
# Get channel id from any youtube video link
# https://commentpicker.com/youtube-channel-id.php

# getting statistics of certain youtube channel from its channel_id
api_key = 'AIzaSyAARWd4u9zkHEIhst5pLp59BIqa51m3Izg'
youtube = build('youtube','v3',developerKey=api_key)
# meet kevin channelid
channel_id = 'UCUvvj5lwue7PspotMDjk5UA'
request = youtube.channels().list(part='statistics',id=channel_id)
response = request.execute()
print(response)
