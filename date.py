from datetime import datetime, timedelta

#1 subtract 5 days from today
five_days_ago = datetime.now() - timedelta(days=5)
print("5 days ago:", five_days_ago)

#2 print yesterday, today, tomorrow
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3 drop microseconds from datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("Without microseconds:", no_microseconds)

#4 calculate difference between two dates in seconds
date1 = datetime(2024, 5, 1, 12, 0, 0)
date2 = datetime(2024, 5, 2, 12, 0, 0)
diff_seconds = int((date2 - date1).total_seconds())
print("Difference in seconds:", diff_seconds)
