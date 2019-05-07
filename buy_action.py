import util
from datetime import date, datetime
import date_class as DC
import ticket as Tix
import buy_action as Buy

def get_bus_route():
    route = input("Select a route: Red, Green, or Blue: ")
    if is_valid_route(route):
        return route
    else:
        print("Please enter a valid bus route.\n")
        util._restartOrder()

def is_valid_route(route_request):
    route_lower_case = route_request.lower()
    valid_routes = ["red","green","blue"]
    if route_lower_case in valid_routes:
        return True
    else:
        return False

def get_month():
    month = input("Select a month (1-12): ")
    if DC.is_valid_month(month):
        return month
    else:
        print("Please enter a valid month\n")
        util._restartOrder()

def get_date(month):
    date = input("Select a date (1-31): ")
    if DC.is_valid_date(date,month):
        return date
    else:
        print("Please enter a valid date\n")
        util._restartOrder()

def get_ticket_count():
    ticket_input = input("Number of Tickets (1-4): ")
    try:
        ticket_count = util.safe_int_conversion(ticket_input)
    except ValueError:
        print("Invalid input.\n")

    if Tix.is_valid_number_of_tickets(ticket_count):
        return ticket_count
    else:
        print("Sorry, maximum ticket purchase is 4!\n")
        util._restartOrder()

def complete_ticket_purchase(route_and_date_pair, number_of_tickets, ticket_records):
    pass
