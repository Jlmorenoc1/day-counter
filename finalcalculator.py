from datetime import date, datetime

def difdays(date1, date2):
    return(date2 - date1).days
y1=int(input("Year1:"))
m1=int(input("Month1:"))
d1=int(input("Day1:"))
y2=int(input("Year2:"))
m2=int(input("Month2:"))
d2=int(input("Day2:"))
date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)
print(difdays(date1, date2), "days")