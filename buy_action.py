import util


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
        util.restartOrder()

def _is_valid_route(route_request):
    route_lower_case = route_request.lower()
    valid_routes = ["red","green","blue"]

    if route_lower_case in valid_routes:
        return True
    else:
        return False
