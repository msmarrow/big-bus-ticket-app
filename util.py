import big_bus as BB

def _restartOrder():
    BB.Shell().cmdloop()

# called if user attempts to buy a ticket more than 10
# days in advanced
def ten_day_error_message():
    print("Sorry, ... ")

    _restartOrder()
