# File: routes.py
# Author: Mahjeed Marrow
# Description: checks bus route
# capacity and updates bus record-keeping

import ticket as tix
import buy_action as Buy

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

def update_bus_capacity(ledger_entry, route_ledger):
    for route in route_ledger:
        if ledger_entry == route[0]:
            route[1] -= 1
    return route_ledger

def get_max_capacity(route):
    if route.lower() == "blue":
        return 2*89
    elif route.lower() == "green":
        return 4*89
    elif route.lower() == "red":
        return 5*89

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
