import re
file = open('row.txt')
test = file.read()
check = re.compile('[A-Z][a-z]+')
print(check.findall(test))
