import telegram_send
from datetime import datetime, date

day1 = datetime.now().timetuple().tm_yday
x = int(input('day:'))
y = int(input('month:'))
z = int(input('year:'))
day2 = date(z, y, x).timetuple().tm_yday
diff = str(day2 - day1 + 1)
message = (diff + " days until your date!")
telegram_send.send(messages=[message])




