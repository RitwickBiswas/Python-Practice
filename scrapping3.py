import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
pos = int(input("Position of link: "))
pos = pos-1
rep = int(input("How many times to repeat: "))


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
url = tags[pos].get('href',None)
n=0
while n < rep:
    n = n + 1
    print ('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos].get('href', None)