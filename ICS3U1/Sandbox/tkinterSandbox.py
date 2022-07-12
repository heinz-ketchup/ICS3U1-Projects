# Author: Gavin Xiong
# Date: 2022/03/25
# Purpose: Sandbox for GUIs

# Step 1
from tkinter import *

# Step 2 - create window or the form
myWindow = Tk()
# myWindow.resizable(0, 0)
myWindow.geometry("400x200")

objN = StringVar()
objR = StringVar()
objOutput = StringVar()

# Step 3 - create the widgets
widLabelN = Label(myWindow, text="Enter your value for N:" )
widLabelR = Label(myWindow, text="Enter your value for R:" )

widEntryN = Entry(myWindow, textvariable=objN)
widEntryR = Entry(myWindow, textvariable=objR)

# Unique Subs
def permButtonClicked():
    intX = 0
    strTempN = objN.get()
    strTempR = objR.get()
    objOutput.set("permButtonClicked clicked with %s and %s." % (strTempN, strTempR))
def combButtonClicked():
    intY = 0
    strTempN = objN.get()
    strTempR = objR.get()
    objOutput.set("combButtonClicked clicked with %s and %s." % (strTempN, strTempR))

widCalcPerm = Button(myWindow, text="Calculate Permutation", command=lambda:permButtonClicked())
widCalcComb = Button(myWindow, text="Calculate Combinations", command=lambda:combButtonClicked())
widLabelOutput = Label(myWindow,textvariable = objOutput)



# Step 4 - Position widgets.
widLabelN.grid(row=1, column=1)
widLabelR.grid(row=1, column=2)
widLabelOutput.grid(row = 7, column=1, columnspan=2)

widEntryN.grid(row=3, column=1)
widEntryR.grid(row=3, column=2)

widCalcPerm.grid(row=5, column=1)
widCalcComb.grid(row=5, column=2)

mainloop()