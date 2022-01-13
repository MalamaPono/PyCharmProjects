import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from requests_html import HTMLSession
import numpy as np
import time
import json

# Whenever I feel like it I could also go much further in this project by loading this song.csv
# data into a jupyter notebook to do things like average views or likes or comments for the top 40
# songs of this week and so much more. We will save that exploration for later.

def get_by_index(song):
    by_index = song.index('by')
    while (song[by_index - 1] != ' '):
        by_index = song.index('by', by_index + 1)

    return by_index

def get_song_info():
    url = 'https://top40weekly.com/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # remove all the br tags
    for e in soup.findAll('br'):
        e.extract()

    div_tag = soup.find_all('div', class_='x-text')[-2]
    p_tags = div_tag.find_all('p')

    text = ''
    for p_tag in p_tags:
        text += p_tag.text

    song_list = re.split(r'\d{1,2}\.', text)
    song_list = [song for song in song_list if song != '']
    song_list = [song.strip() for song in song_list]

    for idx, song in enumerate(song_list):
        if 'by' in song:
            by_index = song.index('by')
            while (song[by_index - 1] != ' '):
                by_index = song.index('by', by_index + 1)
            if '(' in song:
                if song.index('(') < by_index:
                    first_parenthesis_index = song.index('(')
                    song = song[:first_parenthesis_index - 1] + song[song.index(')') + 1:]
                    song_list[idx] = song
        else:
            song_list[idx] = 'NAN'

    song_names = []
    song_artists = []
    song_albums = []
    for song in song_list:
        if 'by' in song:
            song_names.append(song[:get_by_index(song) - 1].lower())
            if '(' in song:
                song_artists.append(song[get_by_index(song) + 3:song.index('(') - 1])
                song_albums.append(song[song.index('(') + 1:song.index(')', -1)])
            else:
                song_artists.append( song[get_by_index(song) + 3:])
                song_albums.append('NO ALBUM')
        else:
            song_names.append('NAN')
            song_artists.append('NAN')
            song_albums.append('NAN')
    # song_names = [song[:get_by_index(song) - 1].lower() for song in song_list]
    # song_artists = [song[get_by_index(song) + 3:song.index('(') - 1] if '(' in song else song[get_by_index(song) + 3:] for song in song_list]
    # song_albums = [song[song.index('(') + 1:song.index(')',-1)] if '(' in song else 'NO ALBUM' for song in song_list]

    return (song_names, song_artists, song_albums)

def get_song_df(song_names,song_artists,song_albums):
    dic = {'Name':song_names,'Artist':song_artists,'Album':song_albums}
    song_df = pd.DataFrame(dic)
    return song_df

def get_video_data(song_names):
    views = []
    likes = []
    comment_count = []
    date_published = []
    yt_links = []

    for song_name in song_names:
        if song_name == 'NAN':
            date_published.append(0)
            views.append(0)
            likes.append(0)
            comment_count.append(0)
            yt_links.append('NAN')
        else:
            song_name = '+'.join(song_name.split())
            if '&' in song_name:
                song_name = song_name.replace('&','and')
            search = 'https://www.google.com/search?source=lnms&tbm=vid&q=' + song_name

            PATH = '/Users/malamapono/chromedriver'
            wd = webdriver.Chrome(PATH)
            wd.get(search)
            video_element = wd.find_element(By.CLASS_NAME, 'ct3b9e')
            video_element.click()
            video_url = wd.current_url
            print(video_url)
            yt_links.append(video_url)
            wd.quit()

            api_key = 'AIzaSyAARWd4u9zkHEIhst5pLp59BIqa51m3Izg'
            parts = ['snippet','statistics']
            try:
                video_id = video_url[video_url.index('v=') + 2:]
                data_dic = {}
                for part in parts:
                    url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}'
                    json_url = requests.get(url)
                    data = json.loads(json_url.text)
                    data_dic[part] = data

                date = data_dic['snippet']['items'][0]['snippet']['publishedAt']
                view = data_dic['statistics']['items'][0]['statistics']['viewCount']
                like = data_dic['statistics']['items'][0]['statistics']['likeCount']
                comments = data_dic['statistics']['items'][0]['statistics']['commentCount']

                date_published.append(date)
                views.append(view)
                likes.append(like)
                comment_count.append(comments)
            except:
                date_published.append(0)
                views.append(0)
                likes.append(0)
                comment_count.append(0)
                print('Not a youtube link so adding 0 values')

    return (views, yt_links, likes, date_published, comment_count)

song_names,song_artists,song_albums = get_song_info()
song_df = get_song_df(song_names,song_artists,song_albums)

views, yt_links, likes, date_published, comment_count = get_video_data(song_names)
song_df['Views'] = views
song_df = song_df.fillna(0)
song_df['Views'] = song_df['Views'].astype(int)
song_df['Likes'] = likes
song_df['Comments'] = comment_count
song_df['Date Published'] = date_published
song_df['Link'] = yt_links

print(song_df)
song_df.to_csv('song.csv',index=None)