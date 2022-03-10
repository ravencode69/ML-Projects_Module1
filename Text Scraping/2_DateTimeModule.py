import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(2002, 7, 2)  # birthday is object
print(birthday)

# .days to only give the number of days and not time
total_days_alive = (today-birthday).days
print(total_days_alive)

# add no of days to todays
tdelta = datetime.timedelta(days=40)
print(tdelta+today)

print(today.weekday())
print(today.month)

print(today.day)
# datetime.time( h, m, s, ms)
# datetime.date( Y, M, D)
# datetime.datetime(Y,M,D,h,m,s,ms)

# add 10 hours since current day
hourdelta = datetime.timedelta(hours=40)
print(datetime.datetime.now()+hourdelta)

# T I M E   Z O N E    A W A R E
datetime_today = (datetime.datetime.now(tz=pytz.UTC))
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

# for tz in pytz.all_timezones:
#     print(tz)

# string fomatting in datetime

print(datetime_pacific.strftime('%B %d, %Y'))

print(datetime.datetime.strptime('March 08, 2020', '%B %d, %Y'))
