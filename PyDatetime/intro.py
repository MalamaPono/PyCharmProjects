import datetime

# naive dates and times: Don't have enough information to determine things like timezones or daylight savings time
# making them much easter to deal with
# aware dates and times: Do have enough information to determine their timezones and keep track of daylight savings
# time. This makes them a little more difficult to keep track of and understand.

# ----------------------------------------------------------------------------------------------------
# NAIVE DATES AND TIMES:
# ----------------------------------------------------------------------------------------------------
# DATES: Years, Months, and Days
# year, month, date for this simple date creator without leading zeros
date = datetime.date(2016,7,24)

# to get today's date
today = date.today()
print(today.year)
print(today.month)
print(today.day)

# to get the day of the week
today.weekday()   #Monday - 0 Sunday - 6
today.isoweekday()  #Monday -1 Sunday - 7

# timedeltas are for doing operations on dates like adding a week, finding how far two dates are apart, and more
# They are used to specify a length of time that you can use to operate with other dates.
# adding or subtracting timedelta to a date results in another date.
tdelta =  datetime.timedelta(days=7)
print(today + tdelta)
print(today - tdelta)

# adding or subtracting two dates results in a timedelta, a object that represents the difference in time
my_birthday = datetime.date(2022,7,18)
till_my_birthday = my_birthday - today
print(till_my_birthday)
print(till_my_birthday.total_seconds())
# total_seconds converts the length of time to all seconds

# ----------------------------------------------------------------------------------------------------
# TIMES: Hours, Minutes, Seconds, Microseconds
time = datetime.time(9,30,45,100000)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

# ----------------------------------------------------------------------------------------------------
# DATES and TIMES MIXED TOGETHER
# year, month, day, hour, minute, second, microsecond
date_and_time = datetime.datetime(2016,7,26,12,30,45,100000)
print(date_and_time.date()) #to get only the date
print(date_and_time.time()) #to get only the time

# same rules with timedeltas still apply for datetimes. Timedeltas only apply for datetimes and dates, but
# don't actually work for times by itself
tdelta2 = datetime.timedelta(hours=12)
print(date_and_time+tdelta2)
# ----------------------------------------------------------------------------------------------------
# Key Differences of These:
dt_today = datetime.datetime.today() #returns the current local time without a timezone
dt_now = datetime.datetime.now() #gives the option to enter a timezone as a parameter, if no timezone entered, then it is equivalent to the line above.
dt_utcnow = datetime.datetime.utcnow() #returns time in utc. However, is still not timezone aware, we must explicity do that

# ----------------------------------------------------------------------------------------------------
# AWARE DATES AND TIMES:
# pytz useful module that makes it simple to work with timezones and daylight savings

import pytz
# datetime.datetime parameters are optional so you can do things like leave off the milliseconds parameter,
# but then you would have to use keyword arguments
dt = datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
# These lines above and below are exactly the same and creates a datetime of the current time
# in utc timezone that is timezone aware
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# converting timezones
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

for tz in pytz.all_timezones:
    if tz.startswith('US'):
        print(tz)

hi_tmz = pytz.timezone('US/Hawaii')

# converting naive datetime into timezone aware datetime
dt = datetime.datetime.now()
dt = hi_tmz.localize(dt)
# This dt is now timezone aware with its timezone set to Hawaii Standard time
print(dt)

# now since dt is timezone aware we can convert its date into a differnt timezone
dt_east = dt.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

# ----------------------------------------------------------------------------------------------------
# DIFFERENT WAYS TO STORE DATETIMES AND PASS THEM AROUND
# the best practice is to display and keep datetimes in string formats such
# as isoformat (international standard)
dt = datetime.datetime.now(tz=pytz.timezone('US/Hawaii'))
print(dt)
# print(dt.isoformat())

# convert date to str
str_date = dt.strftime('%B %d, %Y %H:%M:%S.%f')

# convert str to date. strptime always converts the str_date to the utc timezone so keep that in mind
dt2 = datetime.datetime.strptime(str_date,'%B %d, %Y %H:%M:%S.%f')
dt3 = hi_tmz.localize(dt2)
print(dt3)
print(dt == dt3)
# success












