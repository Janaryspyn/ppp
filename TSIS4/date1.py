import datetime
x = datetime.datetime.now()
x = x.strftime("%d")
r = int(x) - 5
print(r)