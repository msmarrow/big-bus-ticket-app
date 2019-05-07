# File: routes.py
# Author: Mahjeed Marrow
# Description: checks bus route
# capacity and updates bus record-keeping
import ticket as tix

def route_capacity_check(route_and_date_pair, number_of_tickets, route_ledger, ticket_records):
    count = 0
    for i in route_ledger:
        if i[0] == route_and_date_pair:
            count +=1
            if i[1] + number_of_tickets > get_max_capacity(i[0][0]):
                print("Type `help` or `?` to return to main menu.\n")
                return "No Capacity"
            #otherwise, the sale is successful
            else:
                i[1] += number_of_tickets

    if count == 0:
        route_ledger.append([route_and_date_pair,number_of_tickets])

    Buy.complete_ticket_purchase(route_and_date_pair, number_of_tickets, ticket_records)
    return route_ledger


'''

for i in range(num_tix):
    tick = Ticket(cal,route,tix_id,price)
    tix.append(tick)
    tix_id += 1

'''


def get_max_capacity(route):
    if route.lower() == "blue":
        return 2*89
    elif route.lower() == "green":
        return 4*89
    elif route.lower() == "red":
        return 5*89
