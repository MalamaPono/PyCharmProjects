# Keep in mind that requests module is different from urllib request module.
# The requests module has different methods like .text to get the data from the response
# where as request module in urllib uses the .read() method to get the data from a response object.

from urllib import request, error, parse
import webbrowser
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 'enter your api key here'

def retrieveImages(tag_string):
    baseurl = "https://api.flickr.com/services/rest/?"
    params_dic = {}
    params_dic['api_key'] = api_key
    params_dic['tags'] = tag_string
    params_dic['tag_mode'] = 'all'
    params_dic['method'] = 'flickr.photos.search'
    params_dic['per_page'] = 5
    params_dic['media'] = 'photos'
    params_dic['format'] = 'json'
    params_dic['nojsoncallback'] = 1

    query = parse.urlencode(params_dic)
    url = baseurl + query
    response = request.urlopen(url,context=ctx)
    binary_data = response.read()
    string_data = binary_data.decode()
    data = json.loads(binary_data)

    return data
