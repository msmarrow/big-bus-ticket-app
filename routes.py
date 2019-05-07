

def route_capacity_check(request, number_of_tickets, ledger):
    count = 0
    for i in ledger:
        if i[0] == request:
            count +=1
            #can't sell tickets if route is at capacity for the day
            if i[1] + number_of_tickets > get_max_capacity(i[0][0]):
                print("Type `help` or `?` to return to main menu.\n")
                return "No Capacity"
            #otherwise, the sale is successful
            else:
                i[1] += number_of_tickets
                return ledger
'''
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
'''


def get_max_capacity(route):
    if route.lower() == "blue":
        return 2*89
    elif route.lower() == "green":
        return 4*89
    elif route.lower() == "red":
        return 5*89
