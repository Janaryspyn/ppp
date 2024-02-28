import re
file = open('row.txt')
test = file.read()
check = re.match(r'a.*b$', test)
if check:
    print("The file matches")
else:
    print("The file does not match")