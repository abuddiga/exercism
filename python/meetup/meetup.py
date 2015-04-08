from datetime import date
import calendar


def meetup_day(year, month, day_of_week, which_week):



	first_of_month_day, days_in_month = calendar.monthrange(year, month)
	
	first_of_month_day += 1 # get to iso weekday

	days_dict = {'Monday' : 1,
				 'Tuesday' : 2,
				 'Wednesday' : 3,
				 'Thursday' : 4,
				 'Friday' : 5,
				 'Saturday' : 6,
				 'Sunday' : 7
	}

	day = days_dict[day_of_week]



	if which_week == "teenth":
		candi_date = day - first_of_month_day + 8 

		if 12 < candi_date < 20:
			return date(year, month, candi_date)
		elif 12 < candi_date + 7 < 20:
			return date(year, month, candi_date + 7)
		else:
			return date(year, month, candi_date + 14)
	
	elif which_week == "last":

		d = day - first_of_month_day + 29

		while d > days_in_month:
		 	d -= 7

		return date(year, month, d)
	else:
		which_week = int(which_week[0]) - 1

		
	first_week_date = day - first_of_month_day + 1

	if first_week_date < 1:
		first_week_date += 7

	meeting_day = 7 * which_week + first_week_date

	return date(year, month, meeting_day)