# File: ticket.py
# Author: Mahjeed Marrow
# Description: class representing ticket object
# and functions that validate ticket data

class Ticket():
    def __init__(self,date,route,id,price):
        self.date = date
        self.route = route
        self.id = id
        self.price = price

    def __repr__(self):
        return "TICKET ID: {}, DATE: {}, ROUTE: {}, PRICE: ${}\n".format(self.id,self.date,self.route,self.price)

# -------------------------------
# Begin Ticket validation functions
# -------------------------------
def is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False
