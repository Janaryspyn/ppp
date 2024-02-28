import re
file = open('row.text')
test = file.read()
reg = r"[ ,.]"
replace = ':'
new = re.sub(reg, replace, test)
print(new)