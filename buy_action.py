import util
from datetime import date, datetime
import date_class as DC
import ticket as Tix
import buy_action as Buy

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
    date =  route_and_date_pair[1]
    route = route_and_date_pair[0]

    Tix.create_ticket(date, route, number_of_tickets, ticket_records)
    print("Purchase Completed!")
    return ticket_records
