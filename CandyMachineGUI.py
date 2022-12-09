# Importing tkinter
from tkinter import *

# Creating the window
window = Tk()
window.title('Cris Candy Machine')
window.geometry("600x400+10+20")

# Canvas for blank space
canvas= Canvas(width= 500, height= 10)
canvas.pack(side = TOP, pady = 10)

# Canvas for the shop name
canvas= Canvas(width= 500, height= 25, bg="white", highlightthickness=0.5, highlightbackground="black")
canvas.create_text(250, 15, text="WELCOME TO CRIS' SWEET CANDY SHOP", fill="red", font=('Helvetica 10 bold'))
canvas.pack(side = TOP, pady = 10)

# Label for the Instruction
Label(text = 'To make a selection, Click on the Product Button Below:', font=' Helvetica 10').pack(side=TOP, pady = 10)

window.mainloop()