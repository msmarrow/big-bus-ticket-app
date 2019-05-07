
def is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False

def get_bus_route_request():
    return input("Select a route: Red, Green, or Blue: ")

def is_valid_route(route_request):
    route_lower_case = route_request.lower()
    valid_routes = ["red","green","blue"]

    if route_lower_case in valid_routes:
        return True
    else:
        return False
