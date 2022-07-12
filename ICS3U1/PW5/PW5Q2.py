# Author: Gavin Xiong
# Date: 2022/04/28
# Purpose: Create a domino class.
# ____________________________________________________
from tkinter import *
import random

# Author: Gavin Xiong
# Date: 2022/04/28
# Purpose: Create a domino class.
# ____________________________________________________________________
# DATA ELEMENTS
# Value - Value of the domino.
# Size - Size in pixels of each square in a domino.
# Orientation -  Horizontal or vertical orientation.
# faceUp - Whether the domino is face up or face down.
# --------------------------------------------------
# METHODS
# __init__ - Initialize the object of the class.
# __str__ - Converts the data elements in a string.
# getValue - Gets the value of the domino from the user.
# setValue - Sets a valid value for the domino.
# getPosInt - Assists getValue.
# flip - Switches the values of the domino.
# setOrientation - Sets a valid orientation for the domino.
# setSize - Sets a valid size for the domino.
# setFace - Sets a valid faceup status for the domino.
# randomize - Randomizes the value of the domino.
# drawDomino - Draws the domino.
# drawHalfDomin - Draws half a domino.
# drawMultidot - Draws the dots on a domino.
# drawDot - Draws a single dot.
# ---------------------------------------------------
class Domino:
    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Initialize the object of the class.
    # Parameters: value, size, orientation and faceUp status.
    # Output: N/A
    def __init__(self, value = 0, size = 30, orientation="horizontal", faceUp = True):
        self.value = value
        self.size = size
        self.orientation = orientation
        self.faceUp = faceUp

        # Checking for valid numbers.
        if str(value).isdigit():
            value = int(value)
            if (value >= 0 and value <= 66):
                if (value // 10 > 6) or (value % 10 > 6):
                    self.value = 0
                else:
                    self.value = value
            else:
                self.value = 0
        else:
            self.value = 0

        if str(size).isdigit():
            size = int(size)
            if (self.size >= 0 and self.size <= 100):
                self.size = size
            else:
                self.size = 0
        else:
            self.size = 0

        if str(orientation) == "horizontal" or str(orientation) == "vertical":
            self.orientation = str(orientation)
        else:
            self.orientation = "horizontal"

        self.diameter = size // 5
        self.gap = self.diameter // 2

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Convert data elements into a string.
    # Parameters: None
    # Output: The data elements.
    def __str__(self):
        value = self.value
        size = self.size
        orientation = self.orientation

        tempStr = f"Domino with value {value}, size {size}, and {orientation} orientation."
        return tempStr

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Get value from user.
    # Parameters: N/A
    # Output: The user input.
    def getValue(self):
        return self.getPosInt("value", 0, 66)
    
    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Change the value data element.
    # Parameters: Value of the domino.
    # Output: N/A
    def setValue(self, value):
        if (value // 10 > 6) or (value % 10 > 6):
            self.value = 0
        else:
            self.value = value

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Assist other methods with getting user input.
    # Parameters: prompt, low and high ranges.
    # Output: User input
    def getPosInt(self, prompt, low, high):
        tempPrompt = f"Please enter the {prompt} of the domino which is between \
            {low} and {high} inclusive: "
        strInput = input(tempPrompt)

        loopCheck = True
        while loopCheck:
            if strInput.isdecimal():
                intInput = int(strInput)
                if intInput >= low and intInput <= high:
                    if prompt == "value" and ((intInput // 10) > 6 or (intInput % 10) > 6):
                        print("The digits in the input cannot exceed 6.")
                    else:
                        loopCheck = False
                else:
                    print(f"The number was not within the range {low} and {high}")
            else:
                print("The input was not a valid number.")
        return intInput
    
    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Flip the values
    # Parameters: N/A
    # Output: N/A
    def flip(self):
        value1 = self.value // 10
        value2 = self.value % 10
        self.value = value2 * 10 + value1

    # Author: Gavin Xiong
    # Date: 2022/04/28
    # Purpose: Change the orientation
    # Parameters: Orientation
    # Output: N/A
    def setOrientation(self, orientation):
        if str(orientation) == "horizontal" or str(orientation) == "vertical":
            self.orientation = str(orientation)
        else:
            self.orientation = 0
    
    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Change the size.
    # Parameters: Size
    # Output: N/A
    def setSize(self, size):
        if str(size).isdecimal:
            if size >= 30 and size <= 100:
                self.size = size
                self.diameter = size / 5
                self.gap = self.diameter / 2
            else:
                self.size = 30
                self.diameter = size / 5
                self.gap = self.diameter / 2
        else:
            self.size = 30
            self.diameter = size / 5
            self.gap = self.diameter / 2

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: change faceUp status
    # Parameters: new FaceUp
    # Output: N/A
    def setFace(self, faceUp):
        if type(faceUp) == bool:
            self.faceUp = faceUp
        else:
            self.faceUp = True

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Randomize current values.
    # Parameters: N/A
    # Output: N/A
    def randomize(self):
        value1 = random.randint(0,6)
        value2 = random.randint(0,6)
        self.value = value2*10 + value1

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Draw a domino.
    # Parameters: canvas, x and y.
    # Output: N/A
    def drawDomino(self, canvas, x=20, y=20):
        dot1 = self.value // 10
        dot2 = self.value % 10
        widthOffset = 1
        lineOffset = self.size//10

        if self.size % 2 == 0:
            widthOffset += 1

        if self.faceUp:
            if self.orientation == "horizontal":
                self.drawHalfDomino(canvas, x, y, dot1)
                canvas.create_line(x+self.size, y+lineOffset, x+self.size, y+self.size-lineOffset, fill="white", width=widthOffset)
                self.drawHalfDomino(canvas, x+self.size, y, dot2)   
            elif self.orientation == "vertical":
                self.drawHalfDomino(canvas, x, y, dot1)
                canvas.create_line(x+lineOffset, y+self.size, x+self.size-lineOffset, y+self.size, fill="white", width=widthOffset)
                self.drawHalfDomino(canvas, x, y+self.size, dot2)
        else:
            if self.orientation == "horizontal":
                canvas.create_rectangle(x, y, x+self.size*2, y+self.size, fill="black")
            elif self.orientation == "vertical":
                canvas.create_rectangle(x, y, x+self.size, y+self.size*2, fill="black")

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Assist drawDomino by drawing half a domino.
    # Parameters: canvas, x, y and value of dots.
    # Output: None
    def drawHalfDomino(self, canvas, x, y, value):  
        canvas.create_rectangle(x, y, x+self.size, y+self.size, fill="black")
        self.drawMultiDot(canvas, x, y, value)

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Assist drawHalfDomino by drawing dots.
    # Parameters: canvas, x, y and number of dots.
    # Output: None
    def drawMultiDot(self, canvas, x, y, dots):
        dotValue1     = [5]
        dotValue2     = [1, 9]
        dotValue3     = [1, 5, 9]
        dotValue4     = [1, 3, 7, 9]
        dotValue5     = [1, 3, 5, 7, 9]
        dotValue6     = [1, 3, 4, 6, 7, 9]
        dotValueSpec2 = [3, 7]
        dotValueSpec3 = [3, 5, 7]
        dotValueSpec6 = [1, 2, 3, 7, 8, 9]
        if dots == 1:
            for dot in dotValue1:
                self.drawDot(canvas, x, y, dot)
        elif dots == 2:
            if self.orientation == "vertical":
                for dot in dotValue2:
                    self.drawDot(canvas, x, y, dot)
            else:
                for dot in dotValueSpec2:
                    self.drawDot(canvas, x, y, dot)
        elif dots == 3:
            if self.orientation == "vertical":
                for dot in dotValue3:
                    self.drawDot(canvas, x, y, dot)
            else:
                for dot in dotValueSpec3:
                    self.drawDot(canvas, x, y, dot)
        elif dots == 4:
            for dot in dotValue4:
                self.drawDot(canvas, x, y, dot)
        elif dots == 5:
            for dot in dotValue5:
                self.drawDot(canvas, x, y, dot)
        elif dots == 6:
            if self.orientation == "vertical":
                for dot in dotValue6:
                    self.drawDot(canvas, x, y, dot)
            else:
                for dot in dotValueSpec6:
                    self.drawDot(canvas, x, y, dot)

    # Author: Gavin Xiong
    # Date: 2022/04/29
    # Purpose: Assist draw multiDot
    # Parameters: canvas, x, y and position
    # Output: Nothing 
    def drawDot(self, canvas, x, y, position):
        relativePosition = position % 3

        if relativePosition == 0:
            relativePosition = 3

        if position >= 0 and position <= 3:
            xInitial = x+self.gap*relativePosition+self.diameter*(relativePosition-1)
            yInitial = y+self.gap
            xOffset = xInitial+self.diameter
            yOffset = yInitial+self.diameter
            canvas.create_oval(xInitial, yInitial, xOffset, yOffset, fill="white", outline="")
        
        if position >= 4 and position <= 6:
            xInitial = x+self.gap*relativePosition+self.diameter*(relativePosition-1)
            yInitial = y+self.gap*2+self.diameter
            xOffset = xInitial+self.diameter
            yOffset = yInitial+self.diameter
            canvas.create_oval(xInitial, yInitial, xOffset, yOffset, fill="white", outline="")
        
        if position >= 7 and position <= 9:
            xInitial = x+self.gap*relativePosition+self.diameter*(relativePosition-1)
            yInitial = y+self.gap*3+self.diameter*2
            xOffset = xInitial+self.diameter
            yOffset = yInitial+self.diameter
            canvas.create_oval(xInitial, yInitial, xOffset, yOffset, fill="white", outline="")

# SUBPROGRAMS
# Author: Gavin Xiong
# Date: 2022/04/29
# Purpose: Adds keybind functionality.
# Parameters: Binded event
# Output: N/A
def keyPressed(event):
    char = event.char
    if char == "d":
        domino = Domino()
        domino.setSize(sizeVar.get())
        domino.setValue(valueVar1.get()*10+valueVar2.get())
        canvas.delete("all")
        domino.drawDomino(canvas, 20, 20)

        domino.flip()
        domino.drawDomino(canvas, 20, 150)

        domino.flip()
        domino.setOrientation("vertical")
        domino.drawDomino(canvas, 250, 20)

        domino.setFace(False)
        domino.setOrientation("horizontal")
        domino.drawDomino(canvas, 20, 290)

    elif char == "x":
        window.destroy()

# MAIN
window = Tk()
window.geometry("490x700")
labelTitle = Label(window, text="Domino Class Demonstration", font=("Segoe UI", 20, "bold"), justify=CENTER)
labelInfo = Label(window, text="'D' to draw and 'X' to exit.", font=("Segoe UI", 15), justify=CENTER)

canvas = Canvas(window,width=450, height=440)
canvas.focus_set()
canvas.bind("<Key>", keyPressed)
canvas.config(bg="white")

labelInfoSize = Label(window, text="Size", font=("Segoe UI", 15))
sizeVar = IntVar()
sizeVar.set(100)
slider1 = Scale(window, orient="horizontal", variable=sizeVar, from_=30, to=100, length=250)

labelInfoValue1 = Label(window, text="Value 1", font=("Segoe UI", 15))
valueVar1 = IntVar()
valueVar1.set(0)
slider2 = Scale(window, orient="horizontal", variable=valueVar1, from_=0, to=6, length=250)

labelInfoValue2 = Label(window, text="Value 2", font=("Segoe UI", 15))
valueVar2 = IntVar()
sizeVar.set(0)
slider3 = Scale(window, orient="horizontal", variable=valueVar2, from_=0, to=6, length=250)

labelTitle.grid(row=0, column=0, columnspan=2, padx=1)
labelInfo.grid(row=1, column=0, columnspan=2, padx=1)
canvas.grid(row=2, column=0, columnspan=2, padx=15, sticky=(N,S,W,E))

labelInfoSize.grid(row=3, column=0)
labelInfoValue1.grid(row=4, column=0)
labelInfoValue2.grid(row=5, column=0)
slider1.grid(row=3, column=1, sticky=(W))
slider2.grid(row=4, column=1, sticky=(W))
slider3.grid(row=5, column=1, sticky=(W))

mainloop()
