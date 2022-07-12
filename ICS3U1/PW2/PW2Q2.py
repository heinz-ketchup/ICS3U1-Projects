# Author: Gavin Xiong
# Date: 2022/03/02
# Purpose: Give data about a number.
# Input: A number
# Output: The number of digits, the sum of digits, the reverse of the number, the palindrome and the digital root.
# Enrichment: Y
# ___________________________________________________________________________________________

while True:

    # Getting the number.
    number = int(input("Please enter your selected number: "))
    
    while number <= 0:
        print("Error: Only positive integers!")
        number = int(input("Please enter your selected number: "))
    
    # Number of digits.
    counter = 1
    while (number // 10**counter) != 0:
        counter += 1

    numberOfDigits = counter

    # Sum of digits
    number = str(number)
    sumOfDigits = 0
    
    # Using the for loop to iterate through each character.
    for digit in number:
        sumOfDigits += int(digit)
    
    number = int(number)

    # Reverse of the number.
    reverse = 0
    counter = 1
    tempNumber = number

    while tempNumber != 0:
        tempDigit = tempNumber % 10
        tempNumber //= 10

        reverse = reverse*10 + tempDigit

    # Palindrome checker.
    if number == reverse:
        palindrome = "True"
    else:
        palindrome = "False"

    # Digital root:
    tempNumber = number
    loopCounter = 0
    digitalRoot = 0
    tempSum = 0

    while (tempNumber >= 10) and (loopCounter < 20):
        tempNumber = str(tempNumber)
        for digit in tempNumber:
            tempSum += int(digit)

        tempNumber = tempSum
        tempSum = 0
        loopCounter += 1
    
    digitalRoot = tempNumber
    
    print("%50s: %7i" % ("Number", number))
    print("%50s: %7i" % ("Number of digits in number", numberOfDigits))
    print("%50s: %7i" % ("Sum of digits in number", sumOfDigits))
    print("%50s: %7i" % ("Reverse of the number", reverse))
    print("%50s: %7s" % ("Is it palindrome", palindrome))
    print("%50s: %7i" % ("What is the digital root", digitalRoot))

    # Taken from PW2Q1
    continueCheck = input("Re-execute program? Y/N : " )
    while True:
        if continueCheck == "Y" or continueCheck == "y" or continueCheck == "N" or continueCheck == "n":
            break
        else:
            print("Error: Invalid input")
            continueCheck = input("Re-execute program? Y/N : ")

    if continueCheck == "Y" or continueCheck == "y":
        pass
    else:
        print("Exiting program")
        break