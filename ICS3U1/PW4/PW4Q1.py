# Author: Gavin Xiong
# Date: 2022/04/02
# Purpose: PY4Q1 - Create front-end for PW3Q1
# Extras: checkbox, save files, frames, text editor, text editor buttons and menu.
# ___________________________________________________________________________________________

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

# Classes
class NumberPackage:
    def __init__(self, num = False, perm = False, comb = False, gcd = False, \
        lcm = False, relative = False):
        self.num = num
        self.perm = perm
        self.comb = comb
        self.gcd = gcd
        self.lcm = lcm
        self.relative = relative


# Window
window = Tk()
window.title("Number Theory - Gavin Xiong")
window.geometry("410x440+20+20")
window.resizable(False, False)
window.config(bg="#000000")

# Menu
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File", command=lambda:openFile())
filemenu.add_command(label="Open Output", command=lambda:createNewWindow())
filemenu.add_command(label="Save As...", command=lambda:saveFile())
filemenu.add_separator()
filemenu.add_command(label="Reset", command=lambda:resetData())
filemenu.add_command(label="Exit", command=lambda:window.destroy())

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=lambda:cut())
editmenu.add_command(label="Copy", command=lambda:copy())
editmenu.add_command(label="Paste", command=lambda:paste())
editmenu.add_separator()
editmenu.add_command(label="Clear", command=lambda:clear())
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=lambda:messagebox.showinfo("Credits", "Created by Gavin. \n2022"))

def resetData():
    strInteger1.set("")
    strInteger2.set("")
    checkButtonNum.select()
    checkButtonPerm.select()
    checkButtonComb.select()
    checkButtonLCM.select()
    checkButtonGCD.select()
    checkButtonRelative.select()
    clear()

def openFile():
    outputText.config(state=NORMAL)
    file = fd.askopenfile(filetypes=[("Text Documents","*.txt")])
    fileData = file.read()
    outputText.insert(END, fileData)
    outputText.config(state=DISABLED)

def saveFile():
    outputText.config(state=NORMAL)
    fileDialog = fd.asksaveasfile(initialfile = "Output.txt", filetypes=[("Text Documents","*.txt")])
    if fileDialog is None:
        return
    savedText = outputText.get(1.0, END)
    fileDialog.write(savedText)
    fileDialog.close()
    outputText.config(state=DISABLED)


def createNewWindow():
    newWindow = Toplevel(window)
    newWindow.title = "Output"
    newWindow.geometry("375x100")
    newTextWindow = Text(newWindow, state=DISABLED, height=6, width=45)
    newTextWindow.config(state=NORMAL)
    newTextWindow.insert(END, outputText.get(1.0, END))
    newTextWindow.config(state=DISABLED)
    newTextWindow.pack()

def cut():
    copy()
    clear()

def paste():
    clear()
    outputText.config(state=NORMAL)
    outputText.insert(END, window.clipboard_get())
    outputText.config(state=DISABLED)

helpmenu = Menu(menubar, tearoff=0)

# Frames
frameInput = Label(window, relief = SUNKEN, height=10, width=10, bg="#5e35b1")
frameOutput = Label(window, relief = SUNKEN, height=10, width=10, bg="#5e35b1")
frameOptions = Label(window, relief = SUNKEN, height=10, width=10, bg="#5e35b1")

# Frame input
labelInput = Label(window, text="Input", bg="#212121", fg="#ffffff")
strInteger1 = StringVar()
strInteger2 = StringVar()
feedback = StringVar()
feedback.set("Input Log")

entry1 = Entry(frameInput, textvariable = strInteger1, bg="#9162e4", fg="#ffffff")
entryLabel1 = Label(frameInput, text="Integer 1", relief=FLAT, width=8, bg="#9162e4", fg="#ffffff")
entry2 = Entry(frameInput, textvariable = strInteger2, bg="#9162e4", fg="#ffffff")
entryLabel2 = Label(frameInput, text="Integer 2", relief=FLAT, width=8, bg="#9162e4", fg="#ffffff")
labelFeedback = Label(frameInput, textvariable = feedback, width=30, relief=GROOVE, bg="#280680", fg="#ffffff")
inputButton = Button(frameInput, text = "Submit", height=7, width=30, bg="#9162e4", fg="#ffffff", \
    command=lambda:inputButtonClicked())

# Frame Output
labelOutput = Label(window, text="Output", bg="#212121", fg="#ffffff")

outputText = Text(frameOutput, state=DISABLED, height=6, width=45, bg="#280680", fg="#ffffff")

def clear():
    outputText.config(state=NORMAL)
    outputText.delete(1.0, END)
    outputText.config(state=DISABLED)

def copy():
    window.clipboard_clear()
    window.clipboard_append(outputText.get(1.0, END))

copyButton = Button(frameOutput, text="Copy", height = 2, width = 25, bg="#9162e4", fg="#ffffff",command = lambda:copy())
clearButton = Button(frameOutput, text="Clear", height = 2, width = 25, bg="#9162e4", fg="#ffffff", command = lambda:clear())

# Frame Options
labelOptions = Label(window, text="Options", bg="#212121", fg="#ffffff")

checkNum = BooleanVar()
checkPerm = BooleanVar()
checkComb = BooleanVar()
checkLCM = BooleanVar()
checkGCD = BooleanVar()
checkRelative = BooleanVar()

checkButtonNum = Checkbutton(frameOptions, text = "Number", variable = checkNum, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonPerm = Checkbutton(frameOptions, text = "Permutations", variable = checkPerm, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonComb = Checkbutton(frameOptions, text = "Combinations", variable = checkComb, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonLCM = Checkbutton(frameOptions, text = "LCM", variable = checkLCM, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonGCD = Checkbutton(frameOptions, text = "GCD", variable = checkGCD, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonRelative = Checkbutton(frameOptions, text = "Relatively Prime", variable = checkRelative, \
    offvalue=False, onvalue=True, bg="#5e35b1", fg="#ffffff", selectcolor="#000000")
checkButtonNum.select()
checkButtonPerm.select()
checkButtonComb.select()
checkButtonLCM.select()
checkButtonGCD.select()
checkButtonRelative.select()

# Subprograms

# inputButtonClicked - Checks entries and calls inputButtonCalc()
# Parameters: None
# Returns: Number Package
def inputButtonClicked():
    strTemp1 = strInteger1.get()
    strTemp2 = strInteger2.get()
    if not (strTemp1.isdigit() and strTemp2.isdigit()):
        feedback.set("Error: Number must be an integer.")
        messagebox.showinfo(title="ERROR!", message="Error: Number must be an integer.")
    else:
        integer1 = int(strTemp1)
        integer2 = int(strTemp2)
        if (integer1 < 1 or integer2 < 1):
            feedback.set("Error: Number cannot be negative.")
            messagebox.showinfo(title="ERROR!", message="Error: Number cannot be negative.")
        else:
            feedback.set("Valid Input!")
            tempNumPack = inputButtonCalc(integer1, integer2)
            setText(tempNumPack)

# inputButtonCalc - Calls other calc functions 
# Parameters: 2 numbers.
# Returns: NumberPackage containing strings.
def inputButtonCalc(num1, num2):
    tempNumPack = NumberPackage()
    numbersDisplay = "%i, %i" % (num1, num2)
    if checkNum.get():
        tempNumPack.num = "Numbers:          %27s" % numbersDisplay
    if checkPerm.get():
        tempNumPack.perm = "Permutations:     %27i" % calcPermutations(num1, num2)
    if checkComb.get():
        tempNumPack.comb = "Combinations:     %27i" % calcCombinations(num1, num2)
    if checkGCD.get():
        tempNumPack.gcd = "GCD:              %27i" % calcGCD(num1, num2)
    if checkLCM.get():
        tempNumPack.lcm = "LCM:              %27i" % calcLCM(num1, num2)
    if checkRelative.get():
        tempNumPack.relative = "Relatively prime: %27s" % isRelativelyPrime(num1, num2)
    return tempNumPack

# setText - Adds Number Package to text widget
# Parameters: Number Package
# Returns: Nothing
def setText(tempNumPack):
    outputText.config(state=NORMAL)
    outputText.delete(1.0, END)
    if checkNum.get():
        outputText.insert(END, tempNumPack.num + '\n')
    if checkPerm.get():
        outputText.insert(END, tempNumPack.perm + '\n')
    if checkComb.get():
        outputText.insert(END, tempNumPack.comb + '\n')
    if checkGCD.get():
        outputText.insert(END, tempNumPack.gcd + '\n')
    if checkLCM.get():
        outputText.insert(END, tempNumPack.lcm + '\n')
    if checkRelative.get():
        outputText.insert(END, tempNumPack.relative + '\n')
    outputText.config(state=DISABLED)

# calcFactorial - Calculates factorials.
# Parameters: Whole number.
# Returns: Factorial of the whole number.
def calcFactorial(num1):
    factorial = 1
    for num2 in range(1, num1+1):
        factorial *= num2
    return factorial

# calcPermutations - calculates permutations.
# Parameters: Number of items and items chosen.
# Returns: Permutations
def calcPermutations(items, chosen):
    if not (items>=chosen):
        items,chosen = chosen,items
    permutations = calcFactorial(items)/calcFactorial(items-chosen)
    return permutations

# calcCombinations - calculates combinations
# Parameters: Number of items and items chosen.
# Returns: Combinations
def calcCombinations(items, chosen):
    if not (items>=chosen):
        items,chosen = chosen,items
    combinations = calcFactorial(items)/(calcFactorial(chosen)*calcFactorial(items-chosen))
    return combinations

# calcGCD - calculates greatest common divisor
# Parameters: 2 numbers.
# Returns: GCD of 2 numbers.
def calcGCD(num1, num2):
    remainder = num1 % num2
    while not remainder == 0:
        num1 = num2
        num2 = remainder
        remainder = num1 % num2
    return num2

# calcGCD - calculates lowest common multiple.
# Parameters: 2 numbers.
# Returns: lCM of 2 numbers.
def calcLCM(num1, num2):
    lcm = num1*num2/calcGCD(num1,num2)
    return lcm

# isRelativelyPrime - checks if two numbers are relatively prime.
# Parameters: 2 numbers.
# Returns: Whether or not the two numbers are relatively prime.
def isRelativelyPrime(num1, num2):
    if calcGCD(num1, num2) == 1:
        result = "True"
    else:
        result = "False"
    return result

# Main
# _______________________________________________________________________

# Gridding Widgets
# Input
labelInput.grid(row=1, column=1, rowspan=1, columnspan=3, padx=5, pady=0, sticky=S)
frameInput.grid(row=2, column=1, rowspan=1, columnspan=3, padx=5, pady=0, sticky=(N, S, E, W))

entryLabel1.grid(row=3, column=1, rowspan=1, columnspan=1, padx=2, pady=3)
entry1.grid(row=3, column=2, rowspan=1, columnspan=1, padx=2, pady=3)
entryLabel2.grid(row=4, column=1, rowspan=1, columnspan=1, padx=2, pady=3)
entry2.grid(row=4, column=2, rowspan=1, columnspan=1, padx=2, pady=3)
labelFeedback.grid(row=5, column=1, rowspan=1, columnspan=3, padx=2, pady=3)
inputButton.grid(row=6, column=1, rowspan=1, columnspan=3, padx=3, pady=3)

# Options
labelOptions.grid(row=1, column=6, rowspan=1, columnspan=4, padx=5, pady=0, sticky=S)
frameOptions.grid(row=2, column=6, rowspan=1, columnspan=4, padx=5, pady=0, sticky=(N, S, E, W))

checkButtonNum.grid(row=3, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)
checkButtonPerm .grid(row=4, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)
checkButtonComb.grid(row=5, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)
checkButtonLCM.grid(row=6, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)
checkButtonGCD.grid(row=7, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)
checkButtonRelative.grid(row=8, column=6, rowspan=1, columnspan=1, padx=3, ipady=5, sticky=W)

# Output
labelOutput.grid(row=9, column=1, rowspan=1, columnspan=8, padx=5, pady=0, sticky=S)
frameOutput.grid(row=10, column=1, rowspan=1, columnspan=8, padx=5, pady=5, sticky=(N, S, E, W))
outputText.grid(row=11, column=1, rowspan=1, columnspan=8, ipadx=5, pady=5)
copyButton.grid(row=12, column=1, rowspan=1, columnspan=4, padx=5, pady=5)
clearButton.grid(row=12, column=5, rowspan=1, columnspan=4, padx=5, pady=5)

window.config(menu=menubar)
mainloop()