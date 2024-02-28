import re

file = open('row.txt')
test = file.read()
res = re.findall('[A-Z][^A-Z]*', test)
print(res)