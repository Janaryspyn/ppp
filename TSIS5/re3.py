import re
file = open('row.txt')
test = file.read()
check = re.compile('[a-z]+[_][a-z]+')
print(check.findall(test))

