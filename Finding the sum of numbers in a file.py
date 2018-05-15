import re
file = open("data.txt")
num = []
for line in file:
    line = line.rstrip()
    ext = re.findall("([0-9]+)",line)
    if len(ext) < 1:
        continue
    for i in range(len(ext)):
        number = float(ext[i])
        num.append(number)
print(sum(num))

