import random

class Card:
    def __init__(self, rank = 1, suit = "Spades"):   # Officially called a Constructor in other languages
        if suit == "Spades" or suit == "Hearts" or suit == "Diamonds" or suit == "Clubs":
            #self.suit = suit
            self.shuffle()
        else:
            self.suit = "Spades"
            
        if str(rank).isdigit():
            if int(rank) >= 1 and int(rank) <= 13:
                self.rank = rank
            else:
                #self.rank = 1
                self.shuffle()
        
        #self.shuffle()

    def __str__(self):
        if self.rank == 1:
            me = "Ace"
        elif self.rank == 11:
            me = "Jack"
        elif self.rank == 12:
            me = "Queen"
        elif self.rank == 13:
            me = "King"
        else:
            me = str(self.rank)
            
        return me + " " + self.suit

    def shuffle(self):
        self.rank = random.randint(1,13)
        self.suit = random.choice(["Hearts","Spades","Diamonds","Clubs"])

# Dependencies
class Hand:
    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()
        self.card3 = Card()

    def __str__(self):
        return f"{self.card1} {self.card2} {self.card3}"
    
    def shuffle(self):
        self.card1.shuffle()
        self.card2.shuffle()
        self.card3.shuffle()

class GroupOfHands:
    def __init__(self):
        self.player1 = Hand()
        self.player2 = Hand()

    def __str__(self):
        return f"Player 1: {self.player1} Player 2: {self.player2}"

    def shuffle(self):
        self.player1.shuffle()
        self.player2.shuffle()


# Main
aCard = Card()
aCard.shuffle()
print(aCard)

aHand = Hand()
aHand.shuffle()
print(aHand)

aGroup = GroupOfHands()
aGroup.shuffle()
print(aGroup)
print(aGroup.player2.card3)

