import os
from datetime import date, time, datetime, timedelta
import datetime

awal = input().split(" ")

d1 = int(awal[0])
m1 = int(awal[1])
t1 = int(awal[2])

f_date = date(t1, m1, d1)
l_date = f_date + datetime.timedelta(days=-50)
formatdate = l_date.strftime("%d-%m-%Y")

os.system(f"git commit --date='{formatdate} 12:12:00' -m \"message\"")

print(formatdate)




