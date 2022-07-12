# Author: Gavin Xiong
# Date: 2022/03/02
# Purpose: Calculate coins needed for change.
# Input: Price paid and money given.
# Output: Coins given back.
# ___________________________________________________________________________________________


while True:
    # Asking for inputs.
    purchasePrice = round(float(input("Please enter the purchase price: ")), 2)
    cashTendered = round(float(input("Please enter cash tendered: ")), 2)

    # Editing
    while purchasePrice < 0:
        print("Error: Purchase price cannot be negative.")
        purchasePrice = round(float(input("Please enter the purchase price: ")), 2)

    while cashTendered < purchasePrice:
        print("Error: Cash tendered cannot be less than the purchase price.")
        cashTendered = round(float(input("Please enter cash tendered: ")), 2)
    
    # Converting inputs to cents.
    changeOwned = 100 * (cashTendered - purchasePrice)

    # Rounding to nearest nickle.
    if (changeOwned % 5) >= 2:
        changeOwned += 5 - (changeOwned % 5)
    
    # Calculating denominations.
    bill20 = changeOwned // (20*100)
    changeOwned %= 20*100

    bill10 = changeOwned // (10*100)
    changeOwned %= 10*100

    bill5 = changeOwned // (5*100)
    changeOwned %= 5*100

    toonies = changeOwned // 200
    changeOwned %= 2*100

    loonies = changeOwned // 100
    changeOwned %= 100

    quarters = changeOwned // 25
    changeOwned %= 25

    dimes = changeOwned // 10
    changeOwned %= 10

    nickels = changeOwned // 5
    changeOwned %= 5

    changeOwned = (cashTendered - purchasePrice)

    print("Purchase price: %10.2f" % purchasePrice)
    print("Cash given: %14.2f" % cashTendered)
    print("Change due: %14.2f" % changeOwned)
    
    print("You are owed %i 20s, %i 10s, %i 5s, %i toonies, %i loonies, %i quarters, %i dimes and %i nickels." % 
        (bill20, bill10, bill5, toonies, loonies, quarters, dimes, nickels))
    
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
    
    # Resetting values since sometimes toonies were negative.
    bill20 = bill10 = bill5 = toonies = loonies = quarters = dimes = nickels = 0