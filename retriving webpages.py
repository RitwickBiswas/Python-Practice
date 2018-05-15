import urllib.request, urllib.parse,urllib.error
file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in file:
    words = line.decode().strip()
    print(line.decode().strip())
    for word in words:
        count[word] = count.get(word,0)+1
print(count)