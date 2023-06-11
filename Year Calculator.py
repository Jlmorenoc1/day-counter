from datetime import datetime
y= (datetime.now().strftime("%Y"))
x = input("what is the year you want?\n")
if int(x) - int(y) > 0:
    print(int(x) - int(y));
elif int(x) - int(y) < 0:
    print(int(y) - int(x));
