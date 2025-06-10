import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

print(now)
print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=3, day=27, hour=4)
print(date_of_birth)
