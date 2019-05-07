# File: buy_action.py
# Author: Mahjeed Marrow
# Description: handles ticket purchases

import ticket as Tix

def complete_ticket_purchase(route_and_date_pair, number_of_tickets, ticket_records):
    date =  route_and_date_pair[1]
    route = route_and_date_pair[0]

    Tix.create_ticket(date, route, number_of_tickets, ticket_records)
    print("Purchase Completed!")
    return ticket_records
