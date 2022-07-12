# Author: Gavin Xiong
# Date: 2022/02/19
# Purpose: Print out 4 sequences.
# Input: N/A
# Output: 4 sequences.
# Question PW1Q3
# ________________________________________________________________________________________________

# Initialization of variables

# Sequence 1.
num1 = 5 # Starting num.
step1 = 3 # Relation between each num.
lastNum1 = 50 # Last num in sequence.

# Sequence 2.
num2 = 90
step2 = -4
lastNum2 = 50

# Sequence 3.
num3 = 3
step3 = 2
lastNum3 = 24576

# Sequence 4.
num4 = 1
step4 = 3
counter = 0
maxCounter = 15 # Limit to the counter.

# Prints out first sequence: 5, 8, 11, ... 50
print("Sequence 1:")

while num1 <= lastNum1:
    if num1 == lastNum1:
        print(num1)
    else: 
        print(num1, end=", ")
    num1 += step1

print()

# Prints out second sequence: 90, 86, 82, ... 50
print("Sequence 2:")

while num2 >= lastNum2:
    if num2 == lastNum2:
        print(num2)
    else: 
        print(num2, end=", ")
    num2 += step2

print()

# Prints out third sequence: 3, 6, 12, 24, ... 24576
print("Sequence 3:")

while num3 <= lastNum3:
    if num3 == lastNum3:
        print(num3)
    else: 
        print(num3, end=", ")
    num3 *= step3

print()

# Prints out fourth sequence 1, 3, 9, ... (15 terms)
print("Sequence 4:")

while counter < maxCounter:
    if counter == (maxCounter-1):
        print(num4)
    else:
        print(num4, end=", ")
    num4 *= step4
    counter +=1