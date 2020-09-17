from datetime import date
from calendar import monthcalendar

getDayIndex = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
index = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, "last": -1}

class MeetupDayException(Exception):
    def __init__(self, message):
        print(message)

def meetup(year: int, month: int, week: str, day_of_week: str) -> 'date':
    monthDaysPerWeek = monthcalendar(year, month)
    dayIndex = getDayIndex.index(day_of_week)
    days = [week_days[dayIndex] for week_days in monthDaysPerWeek if week_days[dayIndex] > 0]

    if(week == 'teenth'):
        for d in days:
            if(d in range(13, 20)):
                return date(year, month, d)

    else:
        try:
            return date(year, month, days[index[week]])
        except IndexError:
            raise MeetupDayException("Selected day does not exist.")
