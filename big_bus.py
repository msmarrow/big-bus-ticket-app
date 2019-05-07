# File: big_bus.py

import cmd
import buy_action as buy
from datetime import date, datetime

#get seating capacity
def max_cap(route):
    if route.lower() == "blue":
        return 3
    elif route.lower() == "green":
        return 4*89
    elif route.lower() == "red":
        return 5*89

#check for discount
def day_chk(month, dat, year=2019):
    try:
        weekday = date(year,int(month),int(dat)).weekday()
        if weekday > 3:
            return "high"
        else:
            return "low"
    except ValueError:
        print("Invalid Date Given")

class Shell(cmd.Cmd):
    intro = "\nWelcome to Big Bus!\nType `help` or `?` to view options.\n"
    prompt = '> '
    event = None

    def do_quit(self, arg):
        return True

    def do_buy(self, args):
        #ticket price
        LO_PRICE = 10
        HI_PRICE = 15

        #unique id
        tix_id = len(tix) + 1

        #counter
        count = 0

        print("Tickets may only be purchased up to 10 days in advance.\n")

        #get user input
        route = get_route()
        month = input("Select a month (1-12): ")
        date  = input("Select a date (1-31): ")
        num_tix = int(input("How many tickets would you like (1-4): "))

        if not is_valid_number_of_tickets(num_tix):
            print("Sorry, maximum ticket purchase is 4!\n")
            Shell().cmdloop()

        #formatted date
        if len(month) == 1:
            month = "0" + month

        if len(date) == 1:
            date = "0" + date

        cal = "{}-{}-2019".format(month,date)
        combo = [route.lower(),cal]

        for i in busdata:
            if i[0] == combo:
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

            #give user option to view all tickets sold to this point
            view = input("Would you like to view all tickets sold? (Y or N): ")
            if view.lower() == 'y':
                print(tix)

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

class Date():
    def __init__(self,month,date,year):
        self.month = month
        self.date = date
        self.year = year

    def __repr__(self):
        return (self.month, self.date, self.year)

if __name__ == '__main__':
    #contains data
    busdata = []
    tix = []

    Shell().cmdloop()
