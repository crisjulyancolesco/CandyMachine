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

# Dispenser class

    # Initializing the Parameter both with default value of 50
    # If the parameter is less than 0, it will be assigned as 50
    def __init__(self, NumberOfItems = 50, CostOfItems = 50):
        if NumberOfItems < 0:
            self.NumberOfItems = 50
        else:
            self.NumberOfItems = NumberOfItems
        if CostOfItems < 0:
            self.CostOfItems = 50
        else:
            self.CostOfItems = CostOfItems
    
    # returns the number of a particular product
    def GetCount(self):
        return self.NumberOfItems

    # returms the cost of a product
    def GetProductCost(self):
        return self.CostOfItems

    # when the product is sold, the product in dispenser is reduced by 1
    def MakeSale(self):
        self.NumberOfItems -= 1
