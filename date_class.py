class Date():
    def __init__(self,month,date,year):
        self.month = month
        self.date = date
        self.year = year

    def __repr__(self):
        return (self.month, self.date, self.year)
