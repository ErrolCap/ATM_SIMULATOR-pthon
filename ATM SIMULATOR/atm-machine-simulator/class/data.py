class Data:
    def __init__(self, fname, mname, lname, sex,  pin, balance, cardNo):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.sex = sex
        self.pin = pin
        self.balance = balance
        self.cardNo  = cardNo

    def get_name(self):
        return ' {} {} {} ' .format (self.first_name, self.mid_name, self.surname)

