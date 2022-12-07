# Cash Register class
class CashRegister:

    # Initializing the Parameter with default value of 500
    # If the parameter is less than 0, it will be assigned as 500
    def __init__(self, CashOnHand = 500):
        if CashOnHand < 0:
            self.CashOnHand = 500
        else:
            self.CashOnHand = CashOnHand

    # Check the current balance
    def CurrentBalance(self):
        return self.CashOnHand
    
    # Add the amount paid to the parameter
    def AcceptAmount(self, AmountPaid):
        self.CashOnHand += AmountPaid
