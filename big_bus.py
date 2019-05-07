# File: routes.py
# Author: Mahjeed Marrow
# Description: main application driver

import cmd
import buy_action as Buy
import refund_action as Rfnd
import ticket as Tix
import routes
import reports
import date_class
from datetime import date, datetime

bus_data = []
tickets_purchased = []

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

        bus_route = routes.get_bus_route()
        month = date_class.get_month()
        date = date_class.get_date(month)
        number_of_tickets = Tix.get_ticket_count()
        calendar_entry = date_class.format_date(month,date)

        route_and_date_pair = [bus_route.lower(),calendar_entry]
        routes.route_capacity_check(route_and_date_pair, number_of_tickets, bus_data, tickets_purchased)

        print("Type `help` or `?` to return to main menu.\n")

    def do_refund_ticket(self, args):
        ticket_id = Tix.get_ticket_id()
        Rfnd.issue_refund(ticket_id, bus_data, tickets_purchased)

    def do_bus_report(self, args):
        reports.get_bus_report(bus_data)
        print("Type `help` or `?` to return to main menu.\n")

    def do_ticket_report(self, args):
        reports.get_ticket_report(bus_data)
        print("Type `help` or `?` to return to main menu.\n")

if __name__ == '__main__':
    Shell().cmdloop()
