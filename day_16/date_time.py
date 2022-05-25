import datetime
from sqlite3 import Timestamp
from time import strftime, strptime
print(dir(datetime))
from datetime import datetime
now = datetime.now()
print(now)   
day=now.day
print(day)
month=now.month
print(month)
timestamp=now.timestamp()
print(timestamp)
#Formatting Date Output Using strftime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
#Using date from datetime
from datetime import date
d=date(2022, 5 ,25)
print(d)
today=date.today()
print("year",today.year)
print("month",today.month)
print("day",today.day)
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
today = date(year=2022, month=5, day=25)
new_year = date(year=2023, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)
#Difference Between Two Points in Time Using timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import date ,time
current=now.strftime("%d %m %y %H %M ")
print(current)
time_stamp=now.timestamp()
print(timestamp)
from datetime import datetime
today_is=" 5 December, 2019"
today_object=datetime.strptime(today_is, "%d %B, %Y")
print(today_object)
#Calculate the time difference between now and new year.
time_now=date(year=2022,month=5,day=25)
new_year=date(year=2023,month=1,day=1)
print(new_year-time_now)
