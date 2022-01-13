# Keep in mind that requests module is different from urllib request module.
# The requests module has different methods like .text to get the data from the response
# where as request module in urllib uses the .read() method to get the data from a response object.

# assignment 2
import urllib.request, urllib.error, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# The data in this API is info about different college universities in the United States. Enter one, and get some info about it.
service_url = "http://py4e-data.dr-chuck.net/json?"
while True:
    address = input("Enter - ")

    full_url = service_url + urllib.parse.urlencode({'address': address, 'key' : 42})
    html = urllib.request.urlopen(full_url,context=ctx)
    data = html.read()

    print("Recieved",len(data),"characters")

    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if 'status' not in json_data or json_data['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id = json_data["results"][0]["place_id"]
    print(place_id)

# loads takes in a json string and returns python object. load takes in a file in json format and returns python object
# dumps takes in a python object and returns a json string. dump takes in a python object and writes directly on the
# file passed in. "s" just means string in this case. 

# # assignment 1
# import urllib.request, urllib.error, urllib.error
# import json
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input("Enter - ")
# html = urllib.request.urlopen(url,context=ctx)
# data = html.read()
#
# json_data = json.loads(data)
#
# comments_list = json_data["comments"]
#
# sum = 0
# for comment in comments_list:
#     sum += comment["count"]
#
# print("The sum of all numbers in this file was",sum)