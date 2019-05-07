import util
from datetime import date, datetime

def _is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False

def _get_bus_route():
    route = input("Select a route: Red, Green, or Blue: ")
    if _is_valid_route(route):
        return route
    else:
        print("Please enter a valid bus route.\n")
        util._restartOrder()

def _is_valid_route(route_request):
    route_lower_case = route_request.lower()
    valid_routes = ["red","green","blue"]
    if route_lower_case in valid_routes:
        return True
    else:
        return False

def _get_month():
    month = input("Select a month (1-12): ")
    if _is_valid_month(month):
        return month
    else:
        print("Please enter a valid month\n")
        util._restartOrder()

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
