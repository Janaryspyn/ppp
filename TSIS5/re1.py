import re
file = open('row.txt')
test = file.read()
match = re.match(r'a[b]*', test)
if match:
    print("The file matches")
else:
    print("The file does not match")