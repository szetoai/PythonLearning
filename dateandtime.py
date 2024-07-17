import datetime
now = datetime.datetime.now()
timestamp = now.timestamp()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

past = datetime.date(2020, 5, 1)
future = datetime.date(2028, 5, 1)
print(past.year, future.year)
print(future - past)
morning = datetime.time(5, 55, 1)
print(datetime.timedelta(weeks=1, days=10, hours=1))
