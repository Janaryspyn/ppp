import re
file = open('row.text')
test = file.read()
result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', test).lower()
print(result)