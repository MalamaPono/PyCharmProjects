# Keep in mind that requests module is different from urllib request module.
# The requests module has different methods like .text to get the data from the response
# where as request module in urllib uses the .read() method to get the data from a response object.

import xml.etree.ElementTree as ET
import urllib.request,urllib.error, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url,context=ctx)
data = html.read()
print('Processed',len(data), "characters")
tree = ET.fromstring(data)

comments_list = tree.findall('comments/comment')
comments_count = len(comments_list)
print("The number of comments was",comments_count)

sum = 0
for comment in comments_list:
    sum += float(comment.find('count').text)

print("The sum of the numbers in the xml file was",sum)


# data = '''<person>
#     <name>Chuck</name>
#     <phone type="intl">
#     +1 783 843 4739
#     </phone>
#     <email hide="yes"/>
# </person>'''
#
# # this method returns a tree of the xml script and all its different nodes and connections
# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:',tree.find('email').get('hide'))