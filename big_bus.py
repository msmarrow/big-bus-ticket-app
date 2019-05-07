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

    def do_buy(self, args):
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

        for i in busdata:
            if i[0] == route_and_date_pair:
                count +=1
                #can't sell tickets if route is at capacity for the day
                if i[1] + num_tix > max_cap(route):
                    print("Sorry, not enough seats available on {} for the {} route\n".format(combo[1],route.title()))
                    print("Type `help` or `?` to return to main menu.\n")
                #otherwise, the sale is successful
                else:
                    i[1] += num_tix

                    #apply discount if 4 tickets are purchased
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

                    for i in range(num_tix):
                        tick = Ticket(cal,route,tix_id,price)
                        tix.append(tick)
                        tix_id += 1

                    print(tix)
                    #prompt user to return to main menu
                    print("Type `help` or `?` to return to main menu.\n")

        if count == 0:
            busdata.append([combo,num_tix])
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

            for i in range(num_tix):
                tick = Ticket(cal,route,tix_id,price)
                tix.append(tick)
                tix_id += 1

            print("Type `help` or `?` to return to main menu.\n")
        else:
            print("Type `help` or `?` to return to main menu.\n")

    def do_refund(self, args):
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
    def do_busRprt(self, args):
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
    def do_tixRprt(self, args):
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
