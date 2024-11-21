from datetime import datetime

year=input("please enter the year:")
month=input("please enter the month:")
day=input("please enter the day:")

age=datetime.now()-datetime(int(year),int(month),int(day))
age_in_day=age.days
age_in_year=age_in_day/364
print("you are about %s years old !" % int(age_in_year))