### DATES ###

from datetime import datetime 

now = datetime.now()

def prin_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

prin_date(now)

year_2024 = datetime(2024, 12, 3)

prin_date(year_2024)

from datetime import time

current__time = time(21, 20, 0)

print(current__time.hour)
print(current__time.minute)
print(current__time.second)

from datetime import date

current__date = date.today()

print(current__date.year)
print(current__date.month)
print(current__date.day)

current__date = date(2025,11,12)

print(current__date.year)
print(current__date.month)
print(current__date.day)


current__date = date(current__date.year, current__date.month + 1, current__date.day)

print(current__date.month)

diff = year_2024 - now    
print(diff)
diff = year_2024.date() - current__date
print(diff)

from datetime import timedelta

start_delta = timedelta(200, 100, 100, weeks = 10)
end_delta = timedelta(300, 100, 100, weeks = 13)

print(start_delta)
print(end_delta)


print(start_delta + end_delta)
print(start_delta - end_delta)
print(start_delta / end_delta)








 