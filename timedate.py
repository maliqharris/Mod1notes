from datetime import datetime, timedelta

now = datetime.now()
print("Current time", now)

tommorow = now + timedelta(days=1)
print("Tommorow:", tommorow)