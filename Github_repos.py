import requests

from lxml import html

username = raw_input("Enter your username : ")

url = 'https://github.com/'+username+'?tab=repositories'
path = '//*[@id="user-repositories-list"]/ul/li/div[1]/h3/a'

response = requests.get(url)

byte_data = response.content

source_code = html.fromstring(byte_data)

tree = source_code.xpath(path)

if len(tree) == 0 :
	print ("Invlid Username ")

for i in tree:
	print i.text_content()
