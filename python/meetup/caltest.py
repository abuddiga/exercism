from datetime import date
import calendar

year = 2015
month = 2

first_of_month_day, days_in_month = calendar.monthrange(year, month)

print first_of_month_day
print days_in_month