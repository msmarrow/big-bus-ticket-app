import big_bus as BB

def _restartOrder():
    BB.Shell().cmdloop()

def safe_int_conversion(input):
    try:
        return int(input)
    except ValueError:
        print("Invalid input: {}\n".format(input))
        _restartOrder()
