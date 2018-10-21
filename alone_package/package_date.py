'''
时间日期
'''

from datetime import datetime


now = datetime.now()
# 2018-10-21 14:30:25.410863
print(now)


dt = datetime(2017,1,29)
# 2017-01-29 00:00:00
print(dt)


timestamp = dt.timestamp()
# 1485619200.0
print(timestamp)

date = datetime.fromtimestamp(timestamp)
print(date)

utcdate = datetime.utcfromtimestamp(timestamp)
print(utcdate)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%Y-%m-%d %H:%M:%S'))


from datetime import timedelta

now = now + timedelta(hours=10)

print(now)

from datetime import timezone

utczone = timezone(timedelta(hours=10))

now = datetime.now()

print(now)

utczone_time = now.replace(tzinfo=utczone)

print(utczone_time)

