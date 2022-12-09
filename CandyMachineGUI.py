from tkinter import *

# Function for Cancel button in 2nd window
def Cancel():
    return StartProgram()

# Function for Okay button in 3rd window
def Okay():
    return StartProgram()

# Function for Okay button in Candy
def Okay1():
    
    # Create the 3rd window
    window = Tk()
    window.title("Thank you, Come Again!!!")
    window.geometry("600x400+10+20")

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window
    Label(window, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

    window.mainloop()

# Function for Okay button in Chips
def Okay2():
    
    # Create the 3rd window
    window = Tk()
    window.title("Thank you, Come Again!!!")
    window.geometry("600x400+10+20")

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window
    Label(window, text = 'Please pick up your Chips and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

    window.mainloop()

# Function for Okay button in Gum
def Okay3():
    
    # Create the 3rd window
    window = Tk()
    window.title("Thank you, Come Again!!!")
    window.geometry("600x400+10+20")

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window
    Label(window, text = 'Please pick up your Gum and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

    window.mainloop()

# Function for Okay button in Cookies
def Okay4():
    
    # Create the 3rd window
    window = Tk()
    window.title("Thank you, Come Again!!!")
    window.geometry("600x400+10+20")

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window
    Label(window, text = 'Please pick up your Cookies and enjoy!!!', font=' Helvetica 10').pack(side=TOP)
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)

    window.mainloop()

# Function for Candy button
def Candy():
   
    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window 
    window = Tk()
    window.title("Candy")
    window.geometry("600x400+10+20")   

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window, text = 'To buy Candy, please insert 10 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Entry(window, textvariable = Payment,width=60,).pack(pady = 10)

    # Creating the Ok and Cancel button
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay1).place(x = 180, y = 105)
    Button(window,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window.mainloop()

# Function for Chips button
def Chips():
   
    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window 
    window = Tk()
    window.title("Chips")
    window.geometry("600x400+10+20")   

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window, text = 'To buy Chips, please insert 50 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Entry(window, textvariable = Payment,width=60,).pack(pady = 10)

    # Creating the Ok and Cancel button
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay2).place(x = 180, y = 105)
    Button(window,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window.mainloop()

# Function for Gum button
def Gum():
   
    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window 
    window = Tk()
    window.title("Gum")
    window.geometry("600x400+10+20")   

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window, text = 'To buy Gum, please insert 25 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Entry(window, textvariable = Payment,width=60,).pack(pady = 10)

    # Creating the Ok and Cancel button
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay3).place(x = 180, y = 105)
    Button(window,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window.mainloop()

# Function for Gum button
def Cookies():

    # Creating integer variable
    Payment = IntVar()

    # Creating 2nd window
    
    window = Tk()
    window.title("Cookies")
    window.geometry("600x400+10+20")   

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window, text = 'To buy Cookies, please insert 90 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Entry(window, textvariable = Payment,width=60,).pack(pady = 10)

    # Creating the Ok and Cancel button
    Button(window,width= 10, text="Okay",font="Helveica 10", command = Okay4).place(x = 180, y = 105)
    Button(window,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window.mainloop()

# Function for Exit button
def Exit():

    # Create the 2nd window
    window = Tk()
    window.title("Thank you, Come Again!!!")
    window.geometry("600x400+10+20")

    # Blank space
    canvas = Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label and Button for 3rd window
    Label(window, text = 'Thank you for you purchase!!', font=' Helvetica 10').pack(side=TOP, pady = 10)
    Label(window, text = "***** Cris' Candy Machine *****", font=' Helvetica 10').pack(side=TOP)

    window.mainloop()

# Function to start the program again
def StartProgram():
    # Creating the 1st window
    window = Tk()
    window.title("Cris Candy Machine")
    window.geometry("600x400+10+20")

    # Blank space
    canvas= Canvas(window, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10)

    # For the shop name
    Button(window, width= 60, text="WELCOME TO CRIS' SWEET CANDY SHOP", font=('Helvetica 10 bold'), fg = 'red').pack(side=TOP, pady = 5)

    # Label for the Instruction
    Label(window, text = 'To make a selection, Click on the Product Button Below:', font=' Helvetica 10').pack(side=TOP, pady = 20)

    # Buttons
    Button(window,width= 45, text="Candy",font="Helveica 10", command = Candy).pack(side=TOP, pady = 3)
    Button(window,width= 45, text="Chips",font="Helveica 10", command = Chips).pack(side=TOP, pady = 3)
    Button(window,width= 45, text="Gum",font="Helveica 10", command = Gum).pack(side=TOP, pady = 3)
    Button(window,width= 45, text="Cookies",font="Helveica 10", command = Cookies).pack(side=TOP, pady = 3)
    Button(window,width= 45, text="Exit",font="Helveica 10", command = Exit).pack(side=TOP, pady = 3)

    window.mainloop()

# Creating the 1st window
window = Tk()
window.title("Cris Candy Machine")
window.geometry("600x400+10+20")

# Blank space
canvas= Canvas(width= 500, height= 10)
canvas.pack(side = TOP, pady = 10)

# For the shop name
Button(window, width= 60, text="WELCOME TO CRIS' SWEET CANDY SHOP", font=('Helvetica 10 bold'), fg = 'red').pack(side=TOP, pady = 5)

# Label for the Instruction
Label(text = 'To make a selection, Click on the Product Button Below:', font=' Helvetica 10').pack(side=TOP, pady = 20)

# Buttons
Button(window,width= 45, text="Candy",font="Helveica 10", command = Candy).pack(side=TOP, pady = 3)
Button(window,width= 45, text="Chips",font="Helveica 10", command = Chips).pack(side=TOP, pady = 3)
Button(window,width= 45, text="Gum",font="Helveica 10", command = Gum).pack(side=TOP, pady = 3)
Button(window,width= 45, text="Cookies",font="Helveica 10", command = Cookies).pack(side=TOP, pady = 3)
Button(window,width= 45, text="Exit",font="Helveica 10", command = Exit).pack(side=TOP, pady = 3)

window.mainloop()