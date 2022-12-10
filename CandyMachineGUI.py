from tkinter import *

# Function for Candy button -----------------------------------------------------------------------------------------------------------------
def Candy():

    # Creating 2nd window
    window1.destroy()
    window2 = Tk()
    window2.title("Candy")
    window2.geometry("600x400+10+20")  

    # Function for Cancel button in 2nd window
    def Cancel():
        window2.destroy()

    # Function for Okay button in Candy
    def Okay1():
        
        # Create the 3rd window
        window2.destroy()
        window3 = Tk()
        window3.title("Thank you, Come Again!!!")
        window3.geometry("600x400+10+20")

        # Function for Okay button in 3rd window
        def Okay():
            window3.destroy()
            
        # Blank space
        canvas = Canvas(window3, width= 500, height= 10)
        canvas.pack(side = TOP, pady = 10) 

        # Label and Button for 3rd window
        Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
        Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

        window3.mainloop()

    # Blank space
    canvas = Canvas(window2, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window2, text = 'To buy Candy, please insert 10 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Pay = Entry(window2,width=60,)
    Pay.pack(pady = 10)

    # Check if the user input the right cost needed
    def Proceed():
        a = int(Pay.get())

        # If the user input exact amount
        if a == 10:
            return Okay1()

        # If the user input more than the exact amount
        elif a >= 10:
            # Create the 3rd window
            window2.destroy()
            window3 = Tk()
            window3.title("Thank you, Come Again!!!")
            window3.geometry("600x400+10+20")

            # Function for Okay button in 3rd window
            def Okay():
                window3.destroy()
                
            # Blank space
            canvas = Canvas(window3, width= 500, height= 10)
            canvas.pack(side = TOP, pady = 10) 

            # Calculate the Change
            Base = int(10)
            Label(window3, text = f'Your change is {a - Base} cents.', font=' Helvetica 10').pack(side=TOP, pady=5)
           
            # Label and Button for 3rd window
            Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
            Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

            window3.mainloop()
            
    # Creating the Ok and Cancel button
    Button(window2,width= 10, text="Okay",font="Helveica 10", command = Proceed).place(x = 180, y = 105)
    Button(window2,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window2.mainloop()

# Function for Chips button -----------------------------------------------------------------------------------------------------------------
def Chips():
   
    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window2
    window1.destroy()
    window2 = Tk()
    window2.title("Chips")
    window2.geometry("600x400+10+20")   

    # Function for Cancel button in 2nd window
    def Cancel():
        window2.destroy()

    # Function for Okay button in Chips
    def Okay2():
        
        # Create the 3rd window2
        window2.destroy()
        window3 = Tk()
        window3.title("Thank you, Come Again!!!")
        window3.geometry("600x400+10+20")

        # Function for Okay button in 3rd window
        def Okay():
            window3.destroy()

        # Blank space
        canvas = Canvas(window3, width= 500, height= 10)
        canvas.pack(side = TOP, pady = 10) 

        # Label and Button for 3rd window
        Label(window3, text = 'Please pick up your Chips and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
        Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

        window3.mainloop()

    # Blank space
    canvas = Canvas(window2, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window2, text = 'To buy Chips, please insert 50 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Pay = Entry(window2, textvariable = Payment,width=60,)
    Pay.pack(pady = 10)

    # Check if the user input the right cost needed
    def Proceed():
        a = int(Pay.get())

        # If the user input exact amount
        if a == 50:
            return Okay2()

        # If the user input more than the exact amount
        elif a >= 50:
            # Create the 3rd window
            window2.destroy()
            window3 = Tk()
            window3.title("Thank you, Come Again!!!")
            window3.geometry("600x400+10+20")

            # Function for Okay button in 3rd window
            def Okay():
                window3.destroy()
                
            # Blank space
            canvas = Canvas(window3, width= 500, height= 10)
            canvas.pack(side = TOP, pady = 10) 

            # Calculate the Change
            Base = int(50)
            Label(window3, text = f'Your change is {a - Base} cents.', font=' Helvetica 10').pack(side=TOP, pady=5)
           
            # Label and Button for 3rd window
            Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
            Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

            window3.mainloop()
            
    # Creating the Ok and Cancel button
    Button(window2,width= 10, text="Okay",font="Helveica 10", command = Proceed).place(x = 180, y = 105)
    Button(window2,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window2.mainloop()

# Function for Gum button -----------------------------------------------------------------------------------------------------------------
def Gum():
   
    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window
    window1.destroy()
    window2 = Tk()
    window2.title("Gum")
    window2.geometry("600x400+10+20")   

    # Function for Cancel button in 2nd window
    def Cancel():
        window2.destroy()

    # Function for Okay button in Gum
    def Okay3():
        
        # Create the 3rd window
        window2.destroy()
        window3 = Tk()
        window3.title("Thank you, Come Again!!!")
        window3.geometry("600x400+10+20")

        # Function for Okay button in 3rd window
        def Okay():
            window3.destroy()

        # Blank space
        canvas = Canvas(window3, width= 500, height= 10)
        canvas.pack(side = TOP, pady = 10) 

        # Label and Button for 3rd window
        Label(window3, text = 'Please pick up your Gum and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
        Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

        window3.mainloop()

    # Blank space
    canvas = Canvas(window2, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window2, text = 'To buy Gum, please insert 25 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Pay = Entry(window2, textvariable = Payment,width=60,)
    Pay.pack(pady = 10)

    # Check if the user input the right cost needed
    def Proceed():
        a = int(Pay.get())

        # If the user input exact amount
        if a == 25:
            return Okay3()

        # If the user input more than the exact amount
        elif a >= 25:
            # Create the 3rd window
            window2.destroy()
            window3 = Tk()
            window3.title("Thank you, Come Again!!!")
            window3.geometry("600x400+10+20")

            # Function for Okay button in 3rd window
            def Okay():
                window3.destroy()
                
            # Blank space
            canvas = Canvas(window3, width= 500, height= 10)
            canvas.pack(side = TOP, pady = 10) 

            # Calculate the Change
            Base = int(25)
            Label(window3, text = f'Your change is {a - Base} cents.', font=' Helvetica 10').pack(side=TOP, pady=5)
           
            # Label and Button for 3rd window
            Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
            Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

            window3.mainloop()

    # Creating the Ok and Cancel button
    Button(window2,width= 10, text="Okay",font="Helveica 10", command = Proceed).place(x = 180, y = 105)
    Button(window2,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window2.mainloop()

# Function for Gum button -----------------------------------------------------------------------------------------------------------------
def Cookies():

    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window
    window1.destroy()
    window2 = Tk()
    window2.title("Cookies")
    window2.geometry("600x400+10+20")

    # Function for Cancel button in 2nd window
    def Cancel():
        window2.destroy()

    # Function for Okay button in Cookies
    def Okay4():
        
        # Create the 3rd window2
        window2.destroy()
        window3 = Tk()
        window3.title("Thank you, Come Again!!!")
        window3.geometry("600x400+10+20")

        # Function for Okay button in 3rd window
        def Okay():
            window3.destroy()

        # Blank space
        canvas = Canvas(window3, width= 500, height= 10)
        canvas.pack(side = TOP, pady = 10) 

        # Label and Button for 3rd window
        Label(window3, text = 'Please pick up your Cookies and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
        Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

        window3.mainloop()

    # Blank space
    canvas = Canvas(window2, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window2, text = 'To buy Cookies, please insert 90 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Pay = Entry(window2, textvariable = Payment,width=60,)
    Pay.pack(pady = 10)

    # Check if the user input the right cost needed
    def Proceed():
        a = int(Pay.get())

        # If the user input exact amount
        if a == 90:
            return Okay4()

        # If the user input more than the exact amount
        elif a >= 90:
            # Create the 3rd window
            window2.destroy()
            window3 = Tk()
            window3.title("Thank you, Come Again!!!")
            window3.geometry("600x400+10+20")

            # Function for Okay button in 3rd window
            def Okay():
                window3.destroy()
                
            # Blank space
            canvas = Canvas(window3, width= 500, height= 10)
            canvas.pack(side = TOP, pady = 10) 

            # Calculate the Change
            Base = int(90)
            Label(window3, text = f'Your change is {a - Base} cents.', font=' Helvetica 10').pack(side=TOP, pady=5)
           
            # Label and Button for 3rd window
            Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
            Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

            window3.mainloop()
           
    # Creating the Ok and Cancel button
    Button(window2,width= 10, text="Okay",font="Helveica 10", command = Proceed).place(x = 180, y = 105)
    Button(window2,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window2.mainloop()

# Function for Exit button -----------------------------------------------------------------------------------------------------------------
def Exit():

    # Create the 2nd window
    window1.destroy()
    window4 = Tk()
    window4.title("Thank you, Come Again!!!")
    window4.geometry("600x400+10+20")

    #Close the window
    def Close():
        window4.destroy()

    # Blank space
    canvas = Canvas(window4, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window2
    Label(window4, text = 'Thank you for you purchase!!', font=' Helvetica 10').pack(side=TOP, pady = 10)
    Label(window4, text = "***** Cris' Candy Machine *****", font=' Helvetica 10').pack(side=TOP)

    # Creating the Exit button
    Button(window4,width= 10, text="Exit",font="Helveica 10", command = Close).place(x = 250, y = 120)

    window4.mainloop()

# Creating the 1st window
window1 = Tk()
window1.title("Cris Candy Machine")
window1.geometry("600x400+10+20")

# Blank space
canvas= Canvas(window1, width= 500, height= 10)
canvas.pack(side = TOP, pady = 10)

# For the shop name
Button(window1, width= 60, text="WELCOME TO CRIS' SWEET CANDY SHOP", font=('Helvetica 10 bold'), fg = 'red').pack(side=TOP, pady = 5)

# Label for the Instruction
Label(text = 'To make a selection, Click on the Product Button Below:', font=' Helvetica 10').pack(side=TOP, pady = 20)

# Buttons
Button(window1,width= 45, text="Candy",font="Helveica 10", command = Candy).pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Chips",font="Helveica 10", command = Chips).pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Gum",font="Helveica 10", command = Gum).pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Cookies",font="Helveica 10", command = Cookies).pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Exit",font="Helveica 10", command = Exit).pack(side=TOP, pady = 3)

window1.mainloop()