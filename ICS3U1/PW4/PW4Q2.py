# Author
# Purpose:
# Date:

from tkinter import *

# Window
window = Tk()
window.geometry("385x325+50+50")
window.title("Shape Generator 2000")
window.resizable(False, False)
window.config(bg="#000000")

# Menu


# Frames
frameShapes = Frame(window, borderwidth=3, relief = SUNKEN, height=50, width=50)
frameOptions = Frame(window, borderwidth=3, relief = SUNKEN, height=50, width=50)
frameSlider = Frame(window, borderwidth=3, relief = SUNKEN, height=50, width=50)
frameOutput = Frame(window, borderwidth=3, relief = SUNKEN, height=50, width=50)

# Labels
labelShapes =  Label(window, text="Shapes", relief = SUNKEN, width=11)
labelOptions =  Label(window, text="Options", relief = SUNKEN, width=10)
labelSlider =  Label(window, text="Size Slider", relief = SUNKEN, width=10)
labelOutput =  Label(window, text="Output", relief = SUNKEN, width=10)

# Shapes.
selectedShape = StringVar()
winShapesRadio1 = Radiobutton(frameShapes, text="Square", variable=selectedShape, value="Square")
winShapesRadio2 = Radiobutton(frameShapes, text="Triangle", variable=selectedShape, value="Triangle")
winShapesRadio3 = Radiobutton(frameShapes, text="Diamond", variable=selectedShape, value="Diamond")
winShapesRadio4 = Radiobutton(frameShapes, text="Cross", variable=selectedShape, value="Cross")

winShapesRadio1.select()
winShapesRadio2.deselect()


# Options
selectedOption = BooleanVar()
winOptionsRadio1 = Radiobutton(frameOptions, text="Filled", variable=selectedOption, value=False)
winOptionsRadio2 = Radiobutton(frameOptions, text="Hollow", variable=selectedOption, value=True)

# Slider
selectedScale = IntVar()
winSliderScale = Scale(frameSlider, variable=selectedScale, from_=1, to=100, resolution=1, orient=VERTICAL)

# Output
winOutputButton = Button(frameOutput, text="Generate", justify=CENTER, relief=RAISED, height=3, width=41, command=lambda:generateClicked())
winOutputText = Text(frameOutput, state=DISABLED, height=3, width=41, wrap=WORD)

# GUI Sub programs
def generateClicked():
    winOutputText.config(state=NORMAL)
    winOutputText.delete(1.0, END)
    winOutputText.config(fg="#000000")

    shape = selectedShape.get()
    option = selectedOption.get()
    shapeSize = selectedScale.get()
    if shape == "Diamond" or shape == "Cross": # Diamond and cross shapes need to have odd sizes.
        if (shapeSize % 2) == 0:
            winOutputText.config(fg="#ed4337")
            winOutputText.insert(END, "Error: Diamond and Cross shapes must have odd sizes.")
        else:
            tempMessage = "Success: %s of size %i has been created. " % (shape, shapeSize)
            winOutputText.insert(END, tempMessage)
            createTextBox()
    else:
            tempMessage = "Success: %s of size %i has been created. " % (shape, shapeSize)
            winOutputText.insert(END, tempMessage)
            createTextBox()
    
            
    
    winOutputText.config(state=DISABLED)

def createTextBox():
    shape = selectedShape.get()
    option = selectedOption.get()
    shapeSize = selectedScale.get()

    tempWindow = Toplevel()
    tempWindow.title(shape)
    tempWindow.geometry("1000x1000")
    tempWindow.attributes("-fullscreen", True)
    tempTextBox = Text(tempWindow, height=100, width=475, font=("Lucida Console", 5), spacing3=1)


    def clear():
        tempTextBox.config(state=NORMAL)
        tempTextBox.delete(1.0, END)
        tempTextBox.config(state=DISABLED)

    def copy():
        window.clipboard_clear()
        window.clipboard_append(tempTextBox.get(1.0, END))

    copyButton = Button(tempWindow, text="Copy", height = 3, width = 83, command = lambda:copy())
    clearButton = Button(tempWindow, text="Clear", height = 3, width = 83, command = lambda:clear())
    exitButton = Button(tempWindow, text="Exit", height = 3, width = 83, command = lambda:tempWindow.destroy())

    tempTextBox.grid(row=0, column=0)
    copyButton.grid(row=1, column=0, sticky=W)
    clearButton.grid(row=1, column=0)
    exitButton.grid(row=1, column=0, sticky=E)
    
    
    if shape == "Square":
        displaySquare(tempTextBox, size = shapeSize, hollow = option)
    elif shape == "Triangle":
        displayTriangle(tempTextBox, size = shapeSize, hollow = option)
    elif shape == "Diamond":
        displayDiamond(tempTextBox, size = shapeSize, hollow = option)
    elif shape == "Cross":
        displayCross(tempTextBox, size = shapeSize, hollow = option)
    
    tempTextBox.config(state=DISABLED)

# Sub programs

def displaySquare(textBox, size = 1, hollow = False):
    if not hollow: # Filled
        for a1 in range(size):
            for a2 in range(size):
                textBox.insert(END, "* ")
            textBox.insert(END, "\n")
    else: # Hollow
        for a1 in range(size):
            for a2 in range(size):
                if a1 == 0 or a1 == (size-1) or a2 == 0 or a2 == (size-1): # Checking if the current area is the first or last row or if it's the first or last column.
                    textBox.insert(END, "* ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")

def displayTriangle(textBox, size = 1, hollow = False):
    if not hollow: # Filled
        for a1 in range(1, size+1):
            for a2 in range(a1):
                textBox.insert(END, "* ")
            textBox.insert(END, "\n")
    else: # Hollow
        for a1 in range(1, size+1):
            for a2 in range(a1):
                if a1 == 0 or a1 == size or a2 == 0 or a2 == a1-1:
                    textBox.insert(END, "* ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")

def displayDiamond(textBox, size = 1, hollow = False):
    if not hollow: # Filled
        # Top
        height = (size // 2) + 1
        for a1 in range(1, height+1):
            for a2 in range(height-a1, 0, -1):
                textBox.insert(END, "  ")
            for a2 in range(0, (a1*2)-1):
                textBox.insert(END, "* ")
            textBox.insert(END, "\n")
        
        # Bottom
        height = (size // 2)
        for a1 in range(1, height+1):
            for a2 in range(a1):
                textBox.insert(END, "  ")
            for a2 in range(0, (height-a2)*2-1):
                textBox.insert(END, "* ")
            textBox.insert(END, "\n")
    else: # Hollow
        # Top
        height = (size // 2) + 1
        for a1 in range(1, height+1):
            for a2 in range(height-a1, 0, -1):
                textBox.insert(END, "  ")
            for a2 in range(0, (a1*2)-1):
                if a2 == 0 or a2 == (a1*2)-2:
                    textBox.insert(END, "* ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")
        # Bottom
        height = (size // 2)
        for a1 in range(1, height+1):
            for a2 in range(a1):
                textBox.insert(END, "  ")
            for a2 in range(1, (height-a2)*2):
                if a2 == 1 or a2 ==((height-a1)*2+1):
                    textBox.insert(END, "* ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")

def displayCross(textBox, size = 1, hollow = False):
    if not hollow: # Filled
        for row in range(size*2+1):
            for a1 in range(size*3): # Doing only the left hand side. Basically using the row = column as a anchor for the rest of the stars.
                if a1 < row+size and a1 >= row:
                    textBox.insert(END, "* ")
                elif a1+row >= size*2 and a1+row <= 3*size-1: # Doing only the right hand side. Using a1+row = size*2 as an anchor for the rest.
                    textBox.insert(END, "* ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")
    else: # Hollow
        for row in range(size*2+1):
            for a1 in range(size*3):
                if a1 < row+size and a1 >= row: # Left hand side
                    if a1 == row+size-1 and row >= (size-(size-3)/2) and row < size: # Removing the extra stuff at the middle.
                        textBox.insert(END, "  ")
                    elif a1 == row and row <= (size+(size-3)/2) and row > size: # Removing extra stuff at the middle.
                        textBox.insert(END, "  ")
                    elif row == 0 or row == size*2 or a1 == row or a1 == row+size-1:
                        textBox.insert(END, "* ")
                    else:
                        textBox.insert(END, "  ")
                elif a1+row >= size*2 and a1+row <= 3*size-1: # Right hand side
                    if row == 0 or row == size*2 or a1+row == size*2 or a1+row == 3*size-1:
                        textBox.insert(END, "* ")
                    else:
                        textBox.insert(END, "  ")
                else:
                    textBox.insert(END, "  ")
            textBox.insert(END, "\n")

# Main

# Shapes
labelShapes.grid(row=1, column=1, rowspan=1, columnspan=3, padx=20, pady=(10,0), sticky=S)
frameShapes.grid(row=2, column=1, rowspan=5, columnspan=3, padx=20, pady=(0,0), sticky=(N, S, E, W))

winShapesRadio1.grid(row = 3, column=1, rowspan=1, columnspan = 2, sticky=W)
winShapesRadio2.grid(row = 4, column=1, rowspan=1, columnspan = 2, sticky=W)
winShapesRadio3.grid(row = 5, column=1, rowspan=1, columnspan = 2, sticky=W)
winShapesRadio4.grid(row = 6, column=1, rowspan=1, columnspan = 2, sticky=W)

# Options
labelOptions.grid(row=1, column=5, rowspan=1, columnspan=3, padx=35, pady=(10,0), sticky=S)
frameOptions.grid(row=2, column=5, rowspan=5, columnspan=3, padx=35, pady=(0,0), sticky=(N, S, E, W))

winOptionsRadio1.grid(row = 3, column=5, rowspan=1, columnspan = 2, sticky=W)
winOptionsRadio2.grid(row = 4, column=5, rowspan=1, columnspan = 2, sticky=W)

# Slider
labelSlider.grid(row=1, column=9, rowspan=1, columnspan=3, padx=20, pady=(10,0), sticky=S)
frameSlider.grid(row=2, column=9, rowspan=5, columnspan=3, padx=20, pady=(0,0), sticky=(N, S, E, W))
winSliderScale.grid(row=3, column=9, sticky=(E))

# Output
labelOutput.grid(row=11, column = 1, columnspan=10, padx=20, pady=15, sticky=N)
frameOutput.grid(row=11, column=1, columnspan=10, padx=20, pady=10, sticky=(N, S, E, W))
winOutputButton.grid(row=13, column=1, columnspan=10, padx=5, pady=(30, 5), sticky=(W, E))
winOutputText.grid(row=14, column=1, columnspan=10, padx=5, pady=(5, 5), sticky=(W, E))


mainloop()