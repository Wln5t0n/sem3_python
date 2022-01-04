import time
import datetime

print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))

"""
~/Desktop/sem3_a/python ❯ python3 Q6.py                             5s 15:21:15
Current date and time:  2022-01-04 15:24:54.036954
Current year:  2022
Month of year:  January
Week number of the year:  01
Weekday of the week:  2

"""
