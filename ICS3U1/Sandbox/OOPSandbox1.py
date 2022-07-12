#Author: Mr. Smith
#Date: November 8, 2021
#Purpose: SANDBOX- OOP1 - Building a Class
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import random

#Author: Mr. Smith
#Date: November 8, 2021
#Purpose: The Creation of Definition of a Playing Card
#DATA ELEMENTS
# rank - a value between 1 and 13
# suit - a value of Spades, Hearts, Diamonds, Clubs
#METHODS
# init - ..............
# str
# deal
# validateMyself
# others.....
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class Card:
    def __init__(self, rank = 1, suit = "Spades"):   # Officially called a Constructor in other languages
        if suit == "Spades" or suit == "Hearts" or suit == "Diamonds" or suit == "Clubs":
            #self.suit = suit
            self.deal()
        else:
            self.suit = "Spades"
            
        if str(rank).isdigit():
            if int(rank) >= 1 and int(rank) <= 13:
                self.rank = rank
            else:
                #self.rank = 1
                self.deal()
        
        #self.deal()

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

    def deal(self):
        self.rank = random.randint(1,13)
        self.suit = random.choice(["Hearts","Spades","Diamonds","Clubs"])
#MAIN----------------------------------------------
myCard = Card(2,"Purple")
print(myCard.rank)
print(myCard.suit)
print(myCard)
myCard.deal()
print(myCard)