# Importing tkinter
from tkinter import *

# Creating the window
window1 = Tk()
window1.title("Cris Candy Machine")
window1.geometry("600x400+10+20")

# Functions for each buttons
def Candy():

    # Creating string variable
    StrVar = StringVar()

    # Creating new window with label
    window2 = Tk()
    window2.title("Candy")
    window2.geometry("600x400+10+20")

    def Cancel():
        window1.mainloop()

    def Okay():
        window3 = Tk()
        window3.title("Candy")
        window3.geometry("600x400+10+20")

        def Okay2():
            return # not yet finished

        canvas = Canvas(window3, width= 500, height= 10)
        canvas.pack(side = TOP, pady = 10) 

        Label(window3, text = 'Please pick up your Candy and enjoy!!!', font=' Helvetica 10').pack(side=TOP)

        Button(window3,width= 10, text="Okay",font="Helveica 10", command = Okay2).place(x = 180, y = 105)

        window3.mainloop()

    # Blank space
    canvas = Canvas(window2, width= 500, height= 10)
    canvas.pack(side = TOP, pady = 10) 

    # Label for the instruction
    Label(window2, text = 'To buy Candy, please insert 10 cents:', font=' Helvetica 10').pack(side=TOP)

    # Creating the frame where the user can type
    Entry(window2, textvariable = StrVar,width=60).pack(pady = 10)

    # Creating the Ok and Cancel button
    Button(window2,width= 10, text="Okay",font="Helveica 10", command = Okay).place(x = 180, y = 105)
    Button(window2,width= 10, text="Cancel",font="Helveica 10", command = Cancel).place(x = 320, y = 105)

    window2.mainloop()
# Blank space
canvas= Canvas(width= 500, height= 10)
canvas.pack(side = TOP, pady = 10)

# For the shop name
Button(window1, width= 60, text="WELCOME TO CRIS' SWEET CANDY SHOP", font=('Helvetica 10 bold'), fg = 'red').pack(side=TOP, pady = 5)

# Label for the Instruction
Label(text = 'To make a selection, Click on the Product Button Below:', font=' Helvetica 10').pack(side=TOP, pady = 20)

# Buttons
Button(window1,width= 45, text="Candy",font="Helveica 10", command = Candy).pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Chips",font="Helveica 10").pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Gum",font="Helveica 10").pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Cookies",font="Helveica 10").pack(side=TOP, pady = 3)
Button(window1,width= 45, text="Exit",font="Helveica 10").pack(side=TOP, pady = 3)

window1.mainloop()