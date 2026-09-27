# Date & Time Module

from datetime import *
import calendar
import time
from turtledemo.clock import current_day

now = datetime.now()
print(now)
print(now.time())
print(now.year)
print(now.month)
print(now.date())
d = date(2027, 5, 27)
print(d)
a=now.strftime("%d-%m-%Y")
print(a)
d1 = date(2028,5,27)

d2= date(2028,6,27)

print("MY BIRTHDAY",d1,"\nYOUNG-SIS BIRTHDAY",d2)

today = date.today()
print("TODAY: ",today)
fut=today+timedelta(days=6)
print('After 6 Days: ',fut)

birth=date(2006,5,27)
current=date.today()
age=today.year-birth.year
print(f'You are {age} years old')
d1 = date(2006,5,27)

d2 = date(2013,6,27)

print(d1 < d2)
print(calendar.month(2006,5))
print(calendar.calendar(2013,))
print(time.time())


print('start')
time.sleep(5)
print('Stop')
start = time.time()

for i in range(100000):
    pass

end = time.time()

print(end - start)