# Finding the youtube links for our search query with the help of regex to search the html returned

import webbrowser as web
from urllib import request
import re

class App:
    def __init__(self):
        self.search_url = 'https://www.youtube.com/results?search_query='
        self.y_url = 'https://www.youtube.com/watch?v='
        self.list = []

    def connect(self,search):
        try:
            search = search.replace(" ", "+")
            html = request.urlopen("https://www.youtube.com/results?search_query=" + search)
            self.list = re.findall(r"/watch\?v=(\S{11})", html.read().decode())

        except Exception as e:
            print("ERROR: ",e)

    def open_web(self):
        web.open(self.y_url + self.list[0])
        self.list.clear()

app = App()

while True:
    name = input("Video Name: ")
    if name == 'q':
        break
    else:
        app.connect(name)
        app.open_web()
