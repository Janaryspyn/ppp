import re

file = open('row.txt')
test = file.read()
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', test)
print(result)