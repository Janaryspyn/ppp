from datetime import datetime
date_1 = input()
date_2 = input()
date1 = datetime.strptime(date_1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_2, "%Y-%m-%d %H:%M:%S")
print(int((date2 - date1).total_seconds()))
