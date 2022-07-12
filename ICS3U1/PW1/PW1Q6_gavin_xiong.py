# Author: Gavin Xiong
# Date: 2022/02/21
# Purpose: Determine the middle number out of three numbers.
# Input: 3 unique positive odd numbers.
# Output: The middle number.
# Question: PW1Q6
# ________________________________________________________________________________________________________

# Initialization of numbers.
numA = 0
numB = 0
numC = 0
middleNum = 0

numA = int(input("Please input your 1st integer: "))
numB = int(input("Please input your 2nd integer: "))
numC = int(input("Please input your 3rd integer: "))

# Checking if it's not positive, not unique and not odd.
while (numA <= 0 or numB <= 0 or numC <= 0) or (numA == numB or numA == numC or numB == numC) or \
        (numA % 2 == 0 or numB % 2 == 0 or numC % 2 == 0):
    print("Error: Your number was either negative, not unique or even.")
    numA = int(input("Please input your 1st integer: "))
    numB = int(input("Please input your 2nd integer: "))
    numC = int(input("Please input your 3rd integer: "))

# Elif for middle number.
if (numA >= numB and numA <= numC) or (numA <= numB and numA >= numC):
    middleNum = numA
elif (numB >= numA and numB <= numC) or (numB <= numA and numB >= numC):
    middleNum = numB
else:
    middleNum = numC

print("The middle number of the numbers: %i, %i, %i was %i." % (numA, numB, numC, middleNum))