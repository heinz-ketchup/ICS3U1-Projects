# Author: Gavin Xiong
# Date: 2022/02/16
# Purpose: Calculate the area of a triangle using 3 sides.
# Input: 3 sides of a triangle.
# Output: The area of the triangle given by the three sides.
# Question: PY1Q2
# _________________________________________________________________________________________________________

import math

# Initialization of variables.
sideA = 0
sideB = 0
sideC = 0 

sideA = float(input("Enter the 1st side of your triangle: "))
print()
sideB = float(input("Enter the 2nd side of your triangle: "))
print()
sideC = float(input("Enter the 3nd side of your triangle: "))
print()

# Editing for correct values.
while (sideA or sideB or sideC) <= 0 or (sideA + sideB <= sideC) or (sideA + sideC <= sideB) or (sideB + sideC <= sideA):
    print("Error: Your triangle is invalid.")
    sideA = float(input("Enter the 1st side of your triangle: "))
    print()
    sideB = float(input("Enter the 2nd side of your triangle: "))
    print()
    sideC = float(input("Enter the 3nd side of your triangle: "))
    print()

semiPerimeter = (sideA + sideB + sideC)/2

# Using Heron's formula
area = math.sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC)) 

# Formatted each variable to 2 decimal places.
print("The area of the triangle with the sides %0.2f, %0.2f, and %0.2f is %0.2f units^2." % (sideA, sideB, sideC, area))
