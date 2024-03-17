import datetime

year = int(input("Enter any year: "))
month = int(input("Enter any month: "))
date = int(input("Enter any date: "))

x = datetime.date(year, month, date)
print("You have entered the date:", x)

print(x, "is", x.strftime("%A"))