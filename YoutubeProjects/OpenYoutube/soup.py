# Finding the youtube links for our search query with the help of the powerful beautiful soup library
# that parses the html that is returned with out search query and extracts only specific links that we want
# currently this soup version doesn't work because of some bug with beautiful soup not being able to retrieve
# all the links from our youtube search.


import requests
import webbrowser as web
from bs4 import BeautifulSoup

class App:

    def __init__(self):
        self.search_url = 'https://www.youtube.com/results?search_query='
        self.y_url = 'https://www.youtube.com'
        self.list = []

    def connect(self,search):
        try:
            search = search.replace(" ", "+")
            response = requests.get(self.search_url+search)
            soup = BeautifulSoup(response.content,'html.parser')
            links = soup.find_all('a',href=True)
            for link in links:
                if link['href'].startswith('/watch'):
                    self.list.append(self.y_url + link['href'])

        except Exception as e:
            print("ERROR: ",e)

    def open_web(self):
        web.open(self.list[0])
        self.list.clear()

app = App()

while True:
    name = input("Video Name: ")
    if name == 'q':
        break
    else:
        app.connect(name)
        app.open_web()

