
def is_valid_number_of_tickets(ticket_order_number):
    if ticket_order_number <= 4:
        return True
    else:
        return False

def get_bus_route():
    return input("Select a route: Red, Green, or Blue: ")
