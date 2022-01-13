from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

url = input('Enter a url to start scraping links: ')
limit = int(input('Enter maximum amount of links: '))
queue = []
queue.append(url)
numLinks = 0

def findAllLinks(queue,numLinks,limit):
    if len(queue) < 0:
        print('ran out of links to search')
        return
    url = queue.pop(0)

    # checks if it is a valid working link
    response = None
    try:
        response = requests.get(url)
    except:
        return numLinks

    print(f'{numLinks}: {url}')
    numLinks += 1
    if numLinks == limit:
        return numLinks
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        queue.append(link.get('href'))

    return numLinks

print('Begin CRAWL')

while len(queue) > 0:
    numLinks = findAllLinks(queue,numLinks,limit)
    if numLinks == limit:
        break

print('Completed CRAWL')
