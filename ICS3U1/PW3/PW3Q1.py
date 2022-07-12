# Author: Gavin Xiong
# Date: 2022/03/21
# Purpose: PY3Q1 - Get permutations, combinations, the GCD and the LCM from two numbers.
# ___________________________________________________________________________________________

import sys

# FUNCTIONS

# Author: Gavin Xiong
# Date: 2022/03/21
# getPositiveInteger - Gets a positive integer between a low and high range + without crashing.
# Parameters: Low, high for boundaries.
# Returns: Returns the user's positive integer which is within the boundary inclusive.
def getPositiveInteger(low, high, prompt):
    newPrompt = prompt + " between " +  str(low) + " and " + str(high) + " inclusive: "
    stringInput = input(newPrompt)
    
    while not stringInput.isdigit():
        print("ERROR: Number must be a positive integer.")
        stringInput = input(newPrompt)
    userInput = int(stringInput)
    while ((userInput < low) or (userInput > high)):
        print("ERROR: Number was outside the range.")
        stringInput = input(newPrompt)
        userInput = int(stringInput)
    return userInput

# Author: Gavin Xiong
# Date: 2022/03/21
# calcFactorial - Calculates factorials.
# Parameters: Whole number.
# Returns: Factorial of the whole number.
def calcFactorial(num1):
    factorial = 1
    for num2 in range(1, num1+1):
        factorial *= num2
    return factorial

# Author: Gavin Xiong
# Date: 2022/03/21
# calcPermutations - calculates permutations.
# Parameters: Number of items and items chosen.
# Returns: Permutations
def calcPermutations(items, chosen):
    if not (items>=chosen):
        items,chosen = chosen,items
    permutations = calcFactorial(items)/calcFactorial(items-chosen)
    return permutations

# Author: Gavin Xiong
# Date: 2022/03/21
# calcCombinations - calculates combinations
# Parameters: Number of items and items chosen.
# Returns: Combinations
def calcCombinations(items, chosen):
    if not (items>=chosen):
        items,chosen = chosen,items
    combinations = calcFactorial(items)/(calcFactorial(chosen)*calcFactorial(items-chosen))
    return combinations

# Author: Gavin Xiong
# Date: 2022/03/21
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

# Author: Gavin Xiong
# Date: 2022/03/21
# calcGCD - calculates lowest common multiple.
# Parameters: 2 numbers.
# Returns: lCM of 2 numbers.
def calcLCM(num1, num2):
    lcm = num1*num2/calcGCD(num1,num2)
    return lcm

# Author: Gavin Xiong
# Date: 2022/03/21
# isRelativelyPrime - checks if two numbers are relatively prime.
# Parameters: 2 numbers.
# Returns: Whether or not the two numbers are relatively prime.
def isRelativelyPrime(num1, num2):
    if calcGCD(num1, num2) == 1:
        result = "True"
    else:
        result = "False"
    return result

# MAIN
rerunCheck = True

while rerunCheck:
    num1 = getPositiveInteger(1, sys.maxsize, "Enter your 1st positive integer") # Specify the max limit for the positive integer.
    num2 = getPositiveInteger(1, sys.maxsize, "Enter your 2nd positive integer")
    numbersDisplay = str(num1) + ", "+ str(num2)

    print("Numbers:          %15s" % numbersDisplay)
    print("Permutations:     %15i" % calcPermutations(num1, num2))
    print("Combinations:     %15i" % calcCombinations(num1, num2))
    print("GCD:              %15i" % calcGCD(num1, num2))
    print("LCM:              %15i" % calcLCM(num1, num2))
    print("Relatively prime: %15s" % isRelativelyPrime(num1, num2))

    for count in range(2):
        print()

    rerunInput = input("Rerun program (Y/N): ")
    while rerunInput not in {"Y", "y", "N", "n"}:
        print("Error: Y/N only.")
        rerunInput = input("Rerun program (Y/N): ")
    if rerunInput not in {"Y", "y"}:
        rerunCheck  = False
    
    for count in range(50):
        print()