#Author: Mr. Smith
#Date: November 10, 2021
#Purpose: SANDBOX - OOP1 - DOMINO
import random
from tkinter import *

class Domino:
    def __init__(self, value = 0, size = 60 , orientation = "H"):
        
        if str(value).isdigit():
            value = int(value)
            if value >= 0 and value <= 66 and value%10 <= 6:
                self.value = value
            else:
                self.value = 0
        else:
            self.value = 0
            
        if str(size).isdigit():
            size = int(size)
            if size >= 30 and size <= 100:
                self.size = size
            else:
                self.size = 60
        else:
            self.size = 60
            
        if str(orientation) == "H" or str(orientation) == "V":
            self.orientation = str(orientation)
        else:
            self.orientation = "H"

        self.diameter = self.size // 5
        self.gap = self.diameter // 2
    #DON'T FORGET THAT AUTHOR/DATE/PURPOSE/ INPUTS/OUTPUTS would be on top of every method
    def draw(self,ARCcanvas,x=0,y=0,orientation="H"):
        if orientation == "H" or orientation == "h":
            self.drawHalf(canvas,x,y,self.value//10)
            self.drawHalf(canvas,x+self.size,y,self.value%10)

    def drawHalf(self,canvas,x=0,y=0, value=0):
        canvas.create_rectangle(x,y,x+self.size,y+self.size)
        canvas.create_oval(x+self.gap,y+self.gap,x+self.gap+self.diameter,y+self.gap+self.diameter)

#SUBS HERE
def keyPressed(event):
    if event.char == "h" or event.char == "H":
        #horizontal domino draw here
        print("HORIZONTAL")
        myDomino = Domino(size=100)
        myDomino.draw(canvas, 400, 100)
    elif event.char == "v" or event.char == "V":
        print("VERTICAL")
        #vertical domino draw here
    else:
        #DO NOTHING
        print("Wrong Input, use v or h")
        
#=-=-=-=-=-=-MAIN Testing
myBoard = Tk()
myBoard.title("My Domino Testing Board")
canvas = Canvas(myBoard,width=640, height=240)
canvas.config(background = "white")

canvas.bind("<Key>",keyPressed)
canvas.pack()
canvas.focus_set()

mainloop()
        
myDomino = Domino(66,100,"V")
print(myDomino.size, myDomino.value, myDomino.orientation)
