import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
parse = BeautifulSoup(html,'html.parser')

print(parse)

tags = parse('a') #Retrive all the anchor tags in a webpage, ie collect all the links within a webpage
for tag in tags:
    print(tag.get('href',None))