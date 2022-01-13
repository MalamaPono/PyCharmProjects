# Keep in mind that requests module is different from urllib request module.
# The requests module has different methods like .text to get the data from the response
# where as request module in urllib uses the .read() method to get the data from a response object.

from urllib import request, error, parse
import json
import ssl
import webbrowser

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

baseurl = "https://itunes.apple.com/search?"

# get all the data
params = {'term':'Ksi','media':'music'}
query = parse.urlencode(params)
url = baseurl+query
response = request.urlopen(url,context=ctx)
binary_data = response.read()

# string version of the data that is returned
# data = binary_data.decode()

# json.loads can take in a binary string (binary_data) or a regular unicode string (binary_data.decode())
# and it knows how to handle and parse both to return python data structures of the json data that it receives
data = json.loads(binary_data)
print(data)

webbrowser.open_new(url)


# function to only get song names
def getSongNames(params):
    song_names = []

    query = parse.urlencode(params)
    url = baseurl + query
    response = request.urlopen(url, context=ctx)
    binary_data = response.read()
    data = json.loads(binary_data.decode())
    track_info = data['results']

    for dic in track_info:
        song_names.append(dic['trackName'])

    return song_names