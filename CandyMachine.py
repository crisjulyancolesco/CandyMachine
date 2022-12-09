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
class Dispenser:

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
    
    # Returns the number of a particular product
    def GetCount(self):
        return self.NumberOfItems

    # Returns the cost of a product
    def GetProductCost(self):
        return self.CostOfItems

    # When the product is sold, the product in dispenser is reduced by 1
    def MakeSale(self):
        self.NumberOfItems -= 1

# Main Program class
# This will start the program and, this is where all operations of the program is in
class MainProgram:
    
    # Shows the choices the user can choose
    def ShowSelection(self):
        global UserInput
        print("**** Welcome to Cris' Candy Shop ****")
        print("To select an item enter:")
        print("""
        1 for Candy
        2 for Chips
        3 for Gum
        4 for Cookies
        0 to View Balance
        9 to Exit""")        
        UserInput = int(input("Enter your choice: "))
    
    # The main operations of the program
    def SellProduct(self, Product, CRegister):
        try:
            ItemNum = Product.GetCount()
            ItemCost = Product.GetProductCost()
            if ItemNum:
                print("The product is still available.")
                print(f"The cost of the product is {ItemCost}")
                Pay = int(input("Enter amount: "))
                print(f"Amount received is {Pay}")
                Change = Pay - ItemCost

                if Change >= 0:
                    print(f"Your change is {Change}")
                    print("Thank you for buying! Please Come Again")
                    CRegister.AcceptAmount(ItemCost)
                    Product.MakeSale()
                else:
                    print("The amount you have is not enough.")
                    print(f"You need {ItemCost - Pay} cents more.")
                    return
            else:
                print("*Sold Out*")
                print("The product is not available.")

        except ValueError:
            print("*Error*")
            print("The amount you have inputted can't be accepted.")  
            print("Amount should only be an integer.")      
    
    # Calls the operations based on user input
    def Choice(self):
        Cashier = CashRegister()
        Candy = Dispenser()
        Chip =  Dispenser()
        Gum =  Dispenser()
        Cookies = Dispenser()

        while True:
            self.ShowSelection()

            if UserInput == 1:
                self.SellProduct(Candy, Cashier)

            elif UserInput == 2:
                self.SellProduct(Chip, Cashier)

            elif UserInput == 3:
                self.SellProduct(Gum, Cashier)

            elif UserInput == 4:
                self.SellProduct(Cookies, Cashier)

            elif UserInput == 0:
                print(f'Your current balance is {Cashier.CurrentBalance()}.')

            elif UserInput == 9:
                break

            else:
                print("Invalid Input")
                print("Please Try Again.")
                continue
        

StartProgram = MainProgram()
StartProgram.Choice()