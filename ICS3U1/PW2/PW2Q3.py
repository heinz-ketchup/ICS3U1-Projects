# Author: Gavin Xiong
# Date: 2022/03/03
# Purpose: Draw a variety of shapes.
# Input: The size of the desired shape.
# Output: The shape.
# Enrichment: Y
# ___________________________________________________________________________________________

while True:
    # Formatting for avaliable shapes.
    print("Please choose your desired shape:")
    print("%15s: %2i" % ("Square", 1))
    print("%15s: %2i" % ("Triangle", 2))
    print("%15s: %2i" % ("Diamond", 3))
    print("%15s: %2i" % ("Cross", 4))
    print("%15s: %2i" % ("Hollow Square", 5))
    print("%15s: %2i" % ("Hollow Triangle", 6))
    print("%15s: %2i" % ("Hollow Diamond", 7))
    print("%15s: %2i" % ("Hollow Cross", 8))
    
    selectedShape = int(input("> "))
    print()

    # Editing
    while selectedShape < 1 or selectedShape > 8:
        print("Error: Integer chosen was not within bounds.")
        print("Please choose your desired shape:")
        print("%15s: %2i" % ("Square", 1))
        print("%15s: %2i" % ("Triangle", 2))
        print("%15s: %2i" % ("Diamond", 3))
        print("%15s: %2i" % ("Cross", 4))
        print("%15s: %2i" % ("Hollow Square", 5))
        print("%15s: %2i" % ("Hollow Triangle", 6))
        print("%15s: %2i" % ("Hollow Diamond", 7))
        print("%15s: %2i" % ("Hollow Cross", 8))

        selectedShape = int(input("> "))
        print()

    # Asking for size of desired shape.
    print("Please enter size:")
    size = int(input("> "))

    # Editing for bounds and odd number if its a diamond.
    while True:
        if size < 1 or size > 20:
            print("Error: Number must be between 1 and 20, inclusive.")
            print("Please enter size:")
            size = int(input("> "))
        elif (selectedShape == 3 or selectedShape == 7 or selectedShape == 4 or selectedShape == 8) and (size % 2 == 0):
            print("Error: Diamond and cross shapes must have odd sizes.")
            print("Please enter size:")
            size = int(input("> "))
        else: break
    
    # Square
    if selectedShape == 1:
        for a1 in range(size):
            for a2 in range(size):
                print("*", end=" ")
            print()

    # Triangle
    if selectedShape == 2:
        for a1 in range(1, size+1):
            for a2 in range(a1):
                print("*", end=" ")
            print()

    # Diamond
    if selectedShape == 3:

        # Top end of the diamond.
        height = (size // 2) + 1
        for a1 in range(1, height+1):
            for a2 in range(height-a1, 0, -1):
                print(" ", end=" ")
            for a2 in range(0, (a1*2)-1):
                print("*", end=" ")
            print()
        
        # Low end of diamond.
        height = (size // 2)
        for a1 in range(1, height+1):
            for a2 in range(a1):
                print(" ", end=" ")
            for a2 in range(0, (height-a2)*2-1):
                print("*", end=" ")
            print()

    # Cross
    if selectedShape == 4:
        for row in range(size*2+1):
            for a1 in range(size*3): # Doing only the left hand side. Basically using the row = column as a anchor for the rest of the stars.
                if a1 < row+size and a1 >= row:
                    print(("*"), end=" ")
                elif a1+row >= size*2 and a1+row <= 3*size-1: # Doing only the right hand side. Using a1+row = size*2 as an anchor for the rest.
                    print(("*"), end=" ")
                else:
                    print(" ", end=" ")
            print()
        

    # Hollow Square
    if selectedShape == 5:
        for a1 in range(size):
            for a2 in range(size):
                if a1 == 0 or a1 == (size-1) or a2 == 0 or a2 == (size-1): # Checking if the current area is the first or last row or if it's the first or last column.
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    
    # Hollow Triangle
    if selectedShape == 6:
        for a1 in range(1, size+1):
            for a2 in range(a1):
                if a1 == 0 or a1 == size or a2 == 0 or a2 == a1-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # Hollow diamond
    if selectedShape == 7:

        # Top end of the diamond.
        height = (size // 2) + 1
        for a1 in range(1, height+1):
            for a2 in range(height-a1, 0, -1):
                print(" ", end=" ")
            for a2 in range(0, (a1*2)-1):
                if a2 == 0 or a2 == (a1*2)-2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
            
        # Low end of diamond.
        height = (size // 2)
        for a1 in range(1, height+1):
            for a2 in range(a1):
                print(" ", end=" ")
            for a2 in range(1, (height-a2)*2):
                if a2 == 1 or a2 ==((height-a1)*2+1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    
    # Hollow cross
    if selectedShape == 8:
        for row in range(size*2+1):
            for a1 in range(size*3):
                if a1 < row+size and a1 >= row: # Left hand side
                    if a1 == row+size-1 and row >= (size-(size-3)/2) and row < size: # Removing the extra stuff at the middle.
                        print((" "), end=" ")
                    elif a1 == row and row <= (size+(size-3)/2) and row > size: # Removing extra stuff at the middle.
                        print((" "), end=" ")
                    elif row == 0 or row == size*2 or a1 == row or a1 == row+size-1:
                        print(("*"), end=" ")
                    else:
                        print(" ", end=" ")
                elif a1+row >= size*2 and a1+row <= 3*size-1: # Right hand side
                    if row == 0 or row == size*2 or a1+row == size*2 or a1+row == 3*size-1:
                        print(("*"), end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")
            print()
         # Taken from PW2Q1
    continueCheck = input("Re-execute program? Y/N : " )
    while True:
        if continueCheck == "Y" or continueCheck == "y" or continueCheck == "N" or continueCheck == "n":
            break
        else:
            print("Error: Invalid input.")
            continueCheck = input("Re-execute program? Y/N : ")

    if continueCheck == "Y" or continueCheck == "y":
        pass
    else:
        print("Exiting program")
        break
