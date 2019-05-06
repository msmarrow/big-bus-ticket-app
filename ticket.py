class Ticket():
    def __init__(self,date,route,id,price):
        self.date = date
        self.route = route
        self.id = id
        self.price = price

    def __repr__(self):
        return "TICKET ID: {}, DATE: {}, ROUTE: {}, PRICE: ${}\n".format(self.id,self.date,self.route,self.price)
