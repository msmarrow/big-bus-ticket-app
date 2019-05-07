import routes
from datetime import date, datetime
import date_class

def get_bus_report(bus_data):
    count = 0
    todays_date = datetime.today().strftime('%m-%d-%Y')
    queried_route = routes.get_bus_route()

    for entry in bus_data:
        route_name = entry[0][0]
        if queried_route.lower() == route_name:
            date = entry[0][1]
            if date == todays_date:
                count += entry[1]
    print("\nROUTE REPORT: TICKETS SOLD FOR {} ROUTE ON {}: {}\n".format(queried_route.upper(),todays_date,count))

def get_ticket_report(bus_data):
    count = 0
    queried_month = date_class.get_month()
    queried_date = date_class.get_date(queried_month)
    formatted_date = date_class.format_date(queried_month, queried_date)

    for entry in bus_data:
        date = entry[0][1]
        if date == formatted_date:
            count += entry[1]

    print("\nTICKET REPORT: TICKETS SOLD FOR ALL ROUTES ON {}: {}\n".format(formatted_date,count))
