file = open("row.txt", "r")
count = 0
content = file.read()
spl = content.split("\n")
for i in spl:
    #if i:
        count+=1
print(count)
