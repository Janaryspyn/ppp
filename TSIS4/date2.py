from datetime import datetime, timedelta
x = datetime.now()
y = x - timedelta(days=1)
t = x + timedelta(days=1)

print(y.strftime("%c"))
print(x.strftime("%c"))
print(t.strftime("%c"))


