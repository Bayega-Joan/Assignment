import calendar

""""
NAME: BAYEGA JOAN EMMILY
REG NO:16/U/4289/EVE
STUDENT NUMBER: 21600500
"""
print("This program tells you the day you were born")
dy = int(input("PLease input the date you were born: "))
mth = int(input(("Please input the month u were born: ")))
yr= int(input("Please type in the year:"))

dt = calendar.weekday(yr, mth, dy)
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("You were born on ", Days[dt])
input("Press Enter to exit")
