# Author: Gavin Xiong
# Date: 2022/03/26
# Purpose: Play Red Dog
# Enrichement: True
# ___________________________________________________________________________________________

import random

# Classes
class TwoCard:
    def __init__(self, card1 = 2, card2 = 2):
        self.card1 = card1
        self.card2 = card2

# Functions

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

#Author: Gavin Xiong
#Date: 2022/03/26
# getCard - Generates a random number to get a card from a deck.
#Parameters: None
#Return: Random integer between 2 and 14 inclusive.
def getCard():
    return random.randint(2, 14)

#Author: Gavin Xiong
#Date: 2022/03/26
# getSuit  - Generates a random number to get a suit.
#Parameters: None
#Return: Random integer between 1 and 4 inclusive.
def getSuit():
    return random.randint(1, 4)

#Author: Gavin Xiong
#Date: 2022/03/26
# getHand - generates a random TwoCard object.
#Parameters: None
#Return: A TwoCard object.
def getHand():
    playerHand = TwoCard()
    playerHand.card1 = getCard()
    playerHand.card2 = getCard()
    return playerHand

def printCard(card):
    if card == 11:
        cardTemp = "Jack"
    elif card == 12:
        cardTemp = "Queen"
    elif card == 13:
        cardTemp = "King"
    elif card == 14:
        cardTemp = "Ace"
    else:
        cardTemp = str(card)
    cardDisplay = cardTemp

    suit = getSuit()
    spades = "\U00002660"
    hearts = "\U00002665"
    diamonds = "\U00002666"
    clubs = "\U00002663"
    
    if suit == 1:
        suitTemp = clubs
    if suit == 2:
        suitTemp = diamonds
    if suit == 3:
        suitTemp = hearts
    if suit == 4:
        suitTemp = spades
    print("%s of %s" % (cardDisplay, suitTemp))

def printHand(TwoCard):
    cardDisplay1 = 0
    cardDisplay2 = 0
    card1 = TwoCard.card1
    card2 = TwoCard.card2
    cards = {card1, card2}
    cardCheck = True

    if card1 == card2:
        if card1 == 11:
            cardTemp = "Jack"
        elif card1 == 12:
            cardTemp = "Queen"
        elif card1 == 13:
            cardTemp = "King"
        elif card1 == 14:
            cardTemp = "Ace"
        else:
            cardTemp = str(card1)
        cardDisplay1 = cardTemp
        cardDisplay2 = cardTemp
    else:
        for card in cards:
            # Number
            if card == 11:
                cardTemp = "Jack"
            elif card == 12:
                cardTemp = "Queen"
            elif card == 13:
                cardTemp = "King"
            elif card == 14:
                cardTemp = "Ace"
            else:
                cardTemp = str(card)
            if cardCheck:
                cardDisplay1 = cardTemp
            else:
                cardDisplay2 = cardTemp
            cardCheck = False
        # Suit
    suit1 = getSuit()
    suit2 = getSuit()
    suits = {suit1, suit2}
    spades = "\U00002660"
    hearts = "\U00002665"
    diamonds = "\U00002666"
    clubs = "\U00002663"
    suitCheck = True
    
    # The suit emojis are coloured but not in python which is weird.
    if suit1 == suit2:
        if suit1 == 1:
            suitTemp = clubs
        if suit1 == 2:
            suitTemp = diamonds
        if suit1 == 3:
            suitTemp = hearts
        if suit1 == 4:
            suitTemp = spades
        print("%s of %s" % (cardDisplay1, suitTemp))
        print("%s of %s" % (cardDisplay2, suitTemp))
    else:
        for suit in suits:
            if suit == 1:
                suitTemp = clubs
            if suit == 2:
                suitTemp = diamonds
            if suit == 3:
                suitTemp = hearts
            if suit == 4:
                suitTemp = spades
            if suitCheck:
                print("%s of %s" % (cardDisplay1, suitTemp))
            else:
                print("%s of %s" % (cardDisplay2, suitTemp))
            suitCheck = False
        
#Author: Gavin Xiong
#Date: 2022/03/26
# getHand - generates a random TwoCard object.
#Parameters: None
#Return: A TwoCard object.
def handType(playerHand):
    if playerHand.card1 - playerHand.card2 == 0:
        handType = "pair"
    elif abs(playerHand.card1 - playerHand.card2) == 1:
        handType = "consecutive"
    else:
        handType = "non-consecutive"
    return handType

#Author: Gavin Xiong
#Date: 2022/03/26
# getHand - generates a random TwoCard object.
#Parameters: None
#Return: A TwoCard object.
def spread(playerHand):
    spread = abs(playerHand.card1 - playerHand.card2) - 1
    if spread <= 0:
        spread = 0
    return spread

#Author: Gavin Xiong
#Date: 2022/03/26
# getHand - generates a random TwoCard object.
#Parameters: None
#Return: A TwoCard object.
def payout(playerHand):
    dist = spread(playerHand)
    if dist == 1:
        payout = 5
    elif dist == 2:
        payout = 4
    elif dist == 3:
        payout = 2
    elif dist > 3:
        payout = 1
    return payout

#Author: Gavin Xiong
#Date: 2022/03/26
# getHand - generates a random TwoCard object.
#Parameters: None
#Return: A TwoCard object.
def between(card, playerHand):
    betweenCheck = card > playerHand.card1 and card < playerHand.card2 or \
        (card < playerHand.card1 and card > playerHand.card2)
    return betweenCheck

# Main
purse = 100
rerunCheck = True

while rerunCheck and (purse > 0):

    print("Purse: " + str(purse) + " credits.")
    bet = getPositiveInteger(1, purse, "Please enter a bet")
    playerHand = getHand()
    print("Your cards:")
    
    printHand(playerHand)
    
    tempType = handType(playerHand)

    if tempType == "pair":
        tempCard = getCard()
        print("3rd Card:")
        printCard(tempCard)
        if tempCard == playerHand.card1 and playerHand.card2:
            print("You won %i credits!" % (bet*11))
            purse += bet*11
        else:
            print("It was a tie.")

    elif tempType == "consecutive":
        print("It was a tie.")

    elif tempType == "non-consecutive":
        if (purse-bet) > bet:
            betLimit = bet
        else:
            betLimit = purse-bet
        bet += getPositiveInteger(0, betLimit, "Make another bet")
        tempCard = getCard()
        print("3rd Card:")
        printCard(tempCard)

        if between(tempCard, playerHand):
            payoff = payout(playerHand)
            print("You won %i credits!" % (bet*payoff))
            purse += bet*payoff
        else:
            purse -= bet
            print("You lost %i credits." % (bet))
        
    for count in range(2):
        print()

    rerunInput = input("Make another bet? (Y/N) ")
    while rerunInput not in {"Y", "y", "N", "n"}:
        print("Error: Y/N only.")
        rerunInput = input("Make another bet? (Y/N) ")
    if rerunInput not in {"Y", "y"}:
        rerunCheck  = False

    for count in range(30):
        print()
