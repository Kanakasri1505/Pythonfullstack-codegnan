'''
### DATE AND TIME

-->Python provides the built-in datetime module to work with date and time....

import datetime


import datetime
today=datetime.date.today()
print(today) #date

now=datetime.datetime.now()
print(now) #time


import datetime
now=datetime.datetime.now()
print(f"year : {now.year}")
print(f"month : {now.month}")
print(f"day : {now.day}")
print(f"hour : {now.hour}")
print(f"minute : {now.minute}")
print(f"second : {now.second}")

Formatting date and time
--->strftime() is used to format date and time
->%d --> day
->%m --> month
->%Y --> year
->%H -->hours
->%M -->minutes
->%S -->seconds

import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H:%M:%S"))

#diff between two dates
import datetime
date_1=datetime.date(2026,6,1)
date_2=datetime.date(2027,6,15)
diff=date_2-date_1
print(diff)


--->timedelta()

import datetime
today=datetime.date.today()
future=today+datetime.timedelta(days = 7)
print(future)

-->weekday() returns 0 if its a weekday and 1 if its weekend
import datetime
day= datetime.date.today()
print(day.weekday())

-->ctime() is used to check the  day month date and year in a single line

import datetime
day= datetime.date.today()
print(day.ctime())

##to get a particular month calendar

import calendar
import datetime

today=datetime.date.today()
month=today.month
year=today.year
print(calendar.month(year,month))

only calendar----

import calendar

year=2025
month=1
print(calendar.month(year,month))

##whole year

import calendar

print(calendar.calendar(2026))

##leap year
'''
import calendar
print(calendar.isleap(2027))


