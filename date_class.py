# File: date_class.py
# Author: Mahjeed Marrow
# Description: class representing date object
# and functions that validate date input
from datetime import date, datetime
import util

class Date():
    '''string representation of a date object'''
    def __init__(self,month,date,year):
        self.month = month
        self.date = date
        self.year = year

    def __repr__(self):
        return (self.month, self.date, self.year)

# -------------------------------
# Begin Date validation functions
# -------------------------------
def _is_valid_month(month_request):
    requested_month = util.safe_int_conversion(month_request)
    current_month = date.today().month
    if current_month == 12:
        next_month = 1
    else:
        next_month = current_month + 1

    if requested_month == current_month:
        return True
    elif requested_month == next_month:
        return True
    else:
        return False

def _is_valid_date(date_request, month, year=2019):
    input_date = util.safe_int_conversion(date_request)
    todays_date = date(year, date.today().month, date.today().day)

    try:
        requested_date = date(year, month, input_date)
    except ValueError:
        print("Invalid Date Given.\n")
        return False
        #util._restartOrder()

    timespan_between_dates = requested_date - todays_date
    if timespan_between_dates.days > 10:
        return False
    elif timespan_between_dates.days < 0:
        return False
    else:
        return True
