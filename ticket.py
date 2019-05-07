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

#------------------------
def is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False

def create_ticket(date, route, ticket_records):
    pass

def update_ticket_records(number_of_tickets, ticket_records):
    pass

def check_for_discount(month, dat, year=2019):
    pass
    '''
    if num_tix == 4:
        if day_chk(month, date) == "low":
            price = LO_PRICE*.9
        else:
            price = HI_PRICE*.9
    else:
        if day_chk(month,date) == "low":
            price = LO_PRICE
        else:
            price = HI_PRICE
'''

def get_ticket_prices(number_of_tickets):
    LOW_PRICE  = 10
    HIGH_PRICE = 15


'''
    try:
        weekday = date(year,int(month),int(dat)).weekday()
        if weekday > 3:
            return "high"
        else:
            return "low"
    except ValueError:
        print("Invalid Date Given")
'''
