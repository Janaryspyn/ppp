import re

file = open('row.txt')
test = file.read()
reg = r"_([a-z])"
new = re.sub(reg, '\g<1>'.upper(), test)

print(new)
