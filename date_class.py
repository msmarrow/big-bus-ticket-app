# File: date_class.py
# Author: Mahjeed Marrow
# Description: functions validating date input
# and doing basic string formatting
from datetime import date, datetime
import util

def is_valid_month(month_request):
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

def is_valid_date(date_request, month, year=2019):
    input_date = util.safe_int_conversion(date_request)
    input_month = util.safe_int_conversion(month)
    todays_date = date(year, date.today().month, date.today().day)

    try:
        requested_date = date(year, input_month, input_date)
    except ValueError:
        return False

    timespan_between_dates = requested_date - todays_date
    if timespan_between_dates.days > 10:
        print("Tickets may only be purchased up to 10 days in advance.\n")
        return False
    elif timespan_between_dates.days < 0:
        print("Tour has already occured.\n")
        return False
    else:
        return True

def format_date(month, date, year=2019):
    if len(month) == 1:
        month = "0" + month

    if len(date) == 1:
        date = "0" + date

    return "{}-{}-2019".format(month,date)
