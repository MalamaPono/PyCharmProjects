# This is from Corey Schafer's Web Scraping video with Beautiful Soup and Requests
# When parsing the html, most html parsers will work the same as long as it is good html,
# however, if it is bad html, different parsers will fill in the blanks differently. In this project we
# are using the lxml html parser.

# The goal of this project is to extract the title, paragraph explanation, and embedded video link for
# each article on Corey's website. Then print all these out and write them out to a csv file.

from bs4 import BeautifulSoup
import requests
import re
import csv

response = requests.get('http://coreyms.com')
html = response.text
soup = BeautifulSoup(html,'html.parser')

articles = soup.find_all('article')

file = open('data.csv','w')
writer = csv.writer(file)
writer.writerow(['headline','summary','video_link'])

for article in articles:
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content').p.text
    print(summary)

    video_url = article.find('iframe',class_='youtube-player')
    if video_url == None:
        continue
    video_url = video_url.get('src')
    pattern = r"/embed/(.+?)\?"
    vid_id = re.search(pattern,video_url).group(1)
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    print()

    row = [headline, summary, yt_link]
    writer.writerow(row)

file.close()