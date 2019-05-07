# File: ticket.py
# Author: Mahjeed Marrow
# Description: class representing ticket object
# and functions that validate ticket data
import date_class as DC
import ticket as Tix
import routes as Rts
import util

class Ticket():
    def __init__(self,date,route,id,price):
        self.date = date
        self.route = route
        self.id = id
        self.price = price

    def __repr__(self):
        return "TICKET ID: {}, DATE: {}, ROUTE: {}, PRICE: ${}".format(self.id,self.date,self.route,self.price)

#------------------------
def is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False

def create_ticket(date, route, number_of_tickets, ticket_records):
    ticket_prices = get_ticket_prices(date, number_of_tickets)
    ticket_id = len(ticket_records) + 1
    for i in range(number_of_tickets):
        new_ticket= Ticket(date, route, ticket_id, ticket_prices)
        Tix.update_ticket_records(new_ticket, ticket_records)
        ticket_id += 1
    return ticket_records

def update_ticket_records(ticket, ticket_records):
    ticket_records.append(ticket)

def remove_ticket_from_records(ticket_id, ticket_records, route_ledger):
    count = 0
    for ticket in ticket_records:
        if ticket_id == ticket.id:
            count += 1
            ticket_route = ticket.route
            ticket_date = ticket.date
            ticket_records.remove(ticket)
            print("Refund Successful. Type `help` or `?` to return to main menu.\n")

    ledger_entry = [ticket_route,ticket_date]
    Rts.update_bus_capacity(ledger_entry, route_ledger)

    if count == 0:
        print("ID Not Found. Type `help` or `?` to return to main menu.\n")
    return ticket_records

def check_for_discount(number_of_tickets):
    if number_of_tickets == 4:
        return True
    else:
        return False

def get_ticket_prices(date, number_of_tickets):
    LOW_PRICE  = 10
    HIGH_PRICE = 15
    ticket_month = DC.parse_date_string(date)[0]
    ticket_date = DC.parse_date_string(date)[1]

    if check_for_discount(number_of_tickets):
        if DC.is_high_price_day(ticket_month, ticket_date):
            return HIGH_PRICE * 0.9
        else:
            return LOW_PRICE * 0.9
    else:
        if DC.is_high_price_day(ticket_month, ticket_date):
            return HIGH_PRICE
        else:
            return LOW_PRICE

def get_ticket_id():
    ticket_id = input("Enter ID of ticket you would like to refund: ")
    return util.safe_int_conversion(ticket_id)
