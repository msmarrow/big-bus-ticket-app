# File: big_bus.py

import cmd
import buy_action as Buy
import ticket as Tix
import routes as Rts
from datetime import date, datetime

busdata = []
tix = []

class Shell(cmd.Cmd):
    intro = "\nWelcome to Big Bus!\nType `help` or `?` to view options.\n"
    prompt = '> '
    event = None

    def do_quit(self, arg):
        return True

    def do_buy_ticket(self, args):
        print("Note: Tickets may only be purchased up to 10 days in advance.\n")
        LO_PRICE = 10
        HI_PRICE = 15
        count = 0

        bus_route = Buy.get_bus_route()
        month = Buy.get_month()
        date = Buy.get_date(month)
        number_of_tickets = Buy.get_ticket_count()
        calendar_entry = DC.format_date(month,date)

        route_and_date_pair = [route.lower(),calendar_entry]
        route_capacity_check(route_and_date_pair, number_of_tickets, busdata, tix)

        print("Type `help` or `?` to return to main menu.\n")

    def do_refund_ticket(self, args):
        id = input("Enter ID of ticket you would like to refund: ")
        count = 0
        for i in tix:
            if int(id) == i.id:
                count += 1
                tix.remove(i)
                print(tix)
                print("Refund Successful. Type `help` or `?` to return to main menu.\n")

        if count == 0:
            print("ID Not Found. Type `help` or `?` to return to main menu.\n")

    #bus report
    def do_bus_report(self, args):
        count = 0
        today = datetime.today().strftime('%m-%d-%Y')
        route = input("Enter Route you would like a report on (Red, Green, Blue): ")
        for i in busdata:
            r2 = i[0][0]
            if route.lower() == r2:
                date = i[0][1]
                if date == today:
                    count = i[1]
        # print results
        print("\nROUTE REPORT: TICKETS SOLD FOR {} ROUTE ON {}: {}\n".format(route.upper(),today,count))
        print("Type `help` or `?` to return to main menu.\n")

    #ticket report
    def do_ticket_report(self, args):
        count = 0
        month = input("Select a month (1-12): ")
        date  = input("Select a date (1-31): ")

        if len(month) == 1:
            month = "0" + month

        if len(date) == 1:
            date = "0" + date

        cal = "{}-{}-2019".format(month,date)

        for i in busdata:
            d2 = i[0][1]
            if d2 == cal:
                count += i[1]

        # print results
        print("\nTICKET REPORT: TICKETS SOLD FOR ALL ROUTES ON {}: {}\n".format(cal,count))
        print("Type `help` or `?` to return to main menu.\n")

if __name__ == '__main__':
    #contains data

    Shell().cmdloop()
