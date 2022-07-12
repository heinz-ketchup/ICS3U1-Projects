# Author: Gavin Xiong
# Date: 2022/05/03
# Purpose: Create a domino hand demonstration.
# _______________________________________________________

from itertools import permutations
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
        widthOffset = 2
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


# Author: Gavin Xiong
# Date: 2022/05/09
# Purpose: Create a domino hand.
# ---------------------------------------------------
# DEPENDENCIES
# Domino Class
# Itertools
# --------------------------------------------------
# DATA ELEMENTS
# firstDomino
# secondDomino
# thirdDomino
# METHODS
# ---------------------------------------------------
# setSize - sets the size of all dominos.
# sort - sorts the dominos from smallest to largest.
# roll - rolls new values for the dominos.
# draw - draws the dominos in original positions.
# drawSorted - draws the dominos in sorted positions.
# getRun - gets the run and one of the possible orientations.
# generatePermutations - generate 48 lists to assist getRun
# drawRun - draws the dominos in the run positions.
# ---------------------------------------------------
class DominoHand:
    def __init__(self, canvasSize=30): 
        if (canvasSize >= 30 and canvasSize <= 100):
            self.firstDomino = Domino(size = canvasSize)
            self.secondDomino = Domino(size = canvasSize)
            self.thirdDomino = Domino(size = canvasSize)
            self.size = canvasSize
        else:
            canvasSize = 30
            self.firstDomino = Domino(size = canvasSize)
            self.secondDomino = Domino(size = canvasSize)
            self.thirdDomino = Domino(size = canvasSize)
            self.size = canvasSize

    def __str__(self):
        return f"{str(self.firstDomino.value).rjust(2, '0')} - {str(self.secondDomino.value).rjust(2, '0')} - {str(self.thirdDomino.value).rjust(2, '0')}"

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: set the size of the dominos.
    # Parameters: size of the dominos.
    # Output: N/A
    def setSize(self, newSize=50):
        if newSize >= 30 and newSize <= 100:
            self.size = newSize
            self.firstDomino = Domino(size = newSize)
            self.secondDomino = Domino(size = newSize)
            self.thirdDomino = Domino(size = newSize)
        else:
            newSize = 50
            self.size = newSize
            self.firstDomino = Domino(size = newSize)
            self.secondDomino = Domino(size = newSize)
            self.thirdDomino = Domino(size = newSize)

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: set the size of the dominos.
    # Parameters: size of the dominos.
    # Output: N/A
    def sort(self):
        largestDomino = max(self.firstDomino.value, self.secondDomino.value, self.thirdDomino.value)
        smallestDomino = min((self.firstDomino.value, self.secondDomino.value, self.thirdDomino.value))
        middleDomino = self.firstDomino.value+self.secondDomino.value+self.thirdDomino.value \
            -largestDomino-smallestDomino
        self.firstDomino.value = smallestDomino
        self.secondDomino.value = middleDomino
        self.thirdDomino.value = largestDomino

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: set the size of the dominos.
    # Parameters: size of the dominos.
    # Output: N/A
    def roll(self):
        self.firstDomino.randomize()
        self.secondDomino.randomize()
        self.thirdDomino.randomize()

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: Draws regular dominos.
    # Parameters: canvas, x, y
    # Output: N/A
    def draw(self, canvas, x, y):
        xOffset = self.size/2
        self.firstDomino.drawDomino(canvas, x, y)
        self.secondDomino.drawDomino(canvas, x+2*self.firstDomino.size+xOffset, y)
        self.thirdDomino.drawDomino(canvas, x+4*self.firstDomino.size+2*xOffset, y)

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: Draws sorted dominos.
    # Parameters: canvas, x, y
    # Output: N/A
    def drawSorted(self, canvas, x, y):
        tempFirst = self.firstDomino
        tempSecond = self.secondDomino
        tempThird = self.thirdDomino
        self.sort()

        xOffset = self.size/2
        self.firstDomino.drawDomino(canvas, x, y)
        self.secondDomino.drawDomino(canvas, x+2*self.firstDomino.size+xOffset, y)
        self.thirdDomino.drawDomino(canvas, x+4*self.firstDomino.size+2*xOffset, y)
        self.firstDomino = tempFirst
        self.secondDomino = tempSecond
        self.thirdDomino = tempThird

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: gets the run and the domino positions.
    # Parameters: N/A
    # Output: dataPackage - contains run and run dominos.
    def getRun(self):
        firstDomino = str(self.firstDomino.value).rjust(2, '0')
        secondDomino = str(self.secondDomino.value).rjust(2, '0')
        thirdDomino = str(self.thirdDomino.value).rjust(2, '0')
        largestRun = 0

        dominoList = [firstDomino, secondDomino, thirdDomino]
        listOfLists = self.generatePermutations(dominoList)
        largestList = dominoList
        for list1 in listOfLists:
            for list2 in list1:
                tempRun = 0
                if list2[1] == list2[2]:
                    tempRun += 1

                if list2[3] == list2[4]:
                    tempRun += 1

                if tempRun == 1:
                    tempRun = 2
                elif tempRun == 2:
                    tempRun = 3
                else:
                    tempRun = 0
                    
                if tempRun >= largestRun:
                    largestList = list2
                    largestRun = tempRun
        
        if largestList[0] == 0:
            largestList[0] = ""
        if largestList[2] == 0:
            largestList[2] = ""
        if largestList[4] == 0:
            largestList[4] = ""

        tempFirst = largestList[0] + largestList[1]
        tempSecond = largestList[2] + largestList[3]
        tempThird = largestList[4] + largestList[5]
        largestList.clear()
        largestList = [tempFirst, tempSecond, tempThird]
        dataPackage = [largestRun, largestList]

        return dataPackage
    
    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: generates 48 permutations of lists.
    # Parameters: dominoList which contains the values of all dominos.
    # Output: 48 lists.
    def generatePermutations(self, dominoList):
        domino1 = [dominoList[0], dominoList[0][::-1]]
        domino2 = [dominoList[1], dominoList[1][::-1]]
        domino3 = [dominoList[2], dominoList[2][::-1]]

        listOfLists1 = []
        for item1 in domino1:
            for item2 in domino2:
                for item3 in domino3:
                    tempList = []
                    tempList.append(item1)
                    tempList.append(item2)
                    tempList.append(item3)
                    listOfLists1.append(tempList)

        listOfLists2 = []
        for listItem in listOfLists1:
            listOfLists2.append(list(permutations(listItem)))

        for a1, list1 in enumerate(listOfLists2):
            for a2, list2 in enumerate(list1):
                listOfLists2[a1].pop(a2)                   # Converting tuple to list because tuple cannot be changed.
                listOfLists2[a1].insert(a2, list(list2))
                tempList = []
                for a3, list3 in enumerate(list2):
                    for string in list3:
                        for letter in string:
                            listOfLists2[a1][a2].append(letter)
                del listOfLists2[a1][a2][:3]

        return listOfLists2

    # Author: Gavin Xiong
    # Date: 2022/05/10
    # Purpose: Draws run dominos.
    # Parameters: canvas, x, y
    # Output: N/A
    def drawRun(self, canvas, x, y):
        dataPackage = self.getRun()
        tempFirst = self.firstDomino
        tempSecond = self.secondDomino
        tempThird = self.thirdDomino

        self.firstDomino.setValue(int(dataPackage[1][0]))
        self.secondDomino.setValue(int(dataPackage[1][1]))
        self.thirdDomino.setValue(int(dataPackage[1][2]))

        xOffset = self.size/2
        self.firstDomino.drawDomino(canvas, x, y)
        self.secondDomino.drawDomino(canvas, x+2*self.firstDomino.size+xOffset, y)
        self.thirdDomino.drawDomino(canvas, x+(4*self.firstDomino.size)+2*xOffset, y)        

        self.firstDomino = tempFirst
        self.secondDomino = tempSecond
        self.thirdDomino = tempThird

# MAIN
# SUBPROGRAMS       
# Author: Gavin Xiong
# Date: 2022/05/10
# Purpose: Adds keybind functionality.
# Parameters: Binded event
# Output: N/A
def keyPressed(event):
    char = str(event.char).lower()
    if char == "d":
        myHand = DominoHand(canvasSize=30)
        myHand.setSize(sizeVar.get())
        myHand.roll()
        canvas.delete("all")

        offset = myHand.size+myHand.size/2
        x = 20
        y = 20
        myHand.draw(canvas, x, y)
        myHand.drawSorted(canvas, x, y+offset)    
        myHand.drawRun(canvas, x, y+offset+offset)
    elif char == "g":
        count0 = 0
        count2 = 0
        count3 = 0
        for count in range(10000):
            runHand = DominoHand()
            runHand.roll()
            runData = runHand.getRun()
            if runData[0] == 0:
                count0 += 1
            elif runData[0] == 2:
                count2 += 1
            elif runData[0] == 3:
                count3 += 1

        count0percent = str(count0 / 100)
        count2percent = str(count2 / 100)
        count3percent = str(count3 / 100)
        str0Runs.set(str(count0) + "-" + count0percent + "%")
        str2Runs.set(str(count2) + "-" + count2percent + "%")
        str3Runs.set(str(count3) + "-" + count3percent + "%")

    elif char == "x":
        window.destroy()

# MAIN
window = Tk()
window.geometry("800x750")
window.title("Domino Hand Showcase")
labelTitle = Label(window, text="Domino Hand Class Demonstration", font=("Segoe UI", 20, "bold"), justify=CENTER)
labelInfo = Label(window, text="'D' to draw, 'G' to simulate hands and 'X' to exit.", font=("Segoe UI", 15), justify=CENTER)

canvas = Canvas(window,width=760, height=450)
canvas.focus_set()
canvas.bind("<Key>", keyPressed)
canvas.config(bg="white")

labelInfoSize = Label(window, text="Size", font=("Segoe UI", 15), justify=LEFT, padx = 10)
sizeVar = IntVar()
sizeVar.set(100)
slider1 = Scale(window, orient="horizontal", variable=sizeVar, from_=30, to=100, length=500)

labelRunInfo = Label(window, text="Run Simulation", font=("Segoe UI", 15, "bold"), justify=CENTER)
label0RunLabel = Label(window, text="# of runs of 0", font=("Segoe UI", 15), justify=CENTER)
label2RunLabel = Label(window, text="# of runs of 2", font=("Segoe UI", 15), justify=CENTER)
label3RunLabel = Label(window, text="# of runs of 3", font=("Segoe UI", 15), justify=CENTER)

str0Runs = StringVar(value="N/A")
str2Runs = StringVar(value="N/A")
str3Runs = StringVar(value="N/A")

label0Run = Label(window, textvariable=str0Runs, font=("Segoe UI", 15), justify=CENTER)
label2Run = Label(window, textvariable=str2Runs, font=("Segoe UI", 15), justify=CENTER)
label3Run = Label(window, textvariable=str3Runs, font=("Segoe UI", 15), justify=CENTER)

labelTitle.grid(row=0, column=0, columnspan=2, padx=1)
labelInfo.grid(row=1, column=0, columnspan=2, padx=1)
canvas.grid(row=2, column=0, columnspan=2, padx=15, sticky=(N,S,W,E))

labelInfoSize.grid(row=3, column=0)
slider1.grid(row=3, column=1, sticky=(W))

labelRunInfo.grid(row = 4, column=0, columnspan=2, padx=20, sticky=W)
label0RunLabel.grid(row = 5, column = 0)
label2RunLabel.grid(row = 6, column = 0)
label3RunLabel.grid(row = 7, column = 0)

label0Run.grid(row = 5, column=1)
label2Run.grid(row = 6, column=1)
label3Run.grid(row = 7, column=1)

mainloop()