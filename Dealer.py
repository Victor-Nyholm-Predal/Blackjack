from Person import Person
from Pile import Pile

class Dealer(Person):

    def __init__(self, amountOfCards, highAces, faceDownCards):
        super().__init__(amountOfCards, highAces)
        self.faceDownCards = faceDownCards

    def reset(self):
        self.clearPile()
        self.faceDownCards = 0

'''
    def getScore(self):
        self.score = pile.getScore()
        return self.score

    def getAmountOfCards(self):
        self.amountOfCards = pile.getAmountOfCards()
        return self.amountOfCards

    def addNewCard(self, card):
        pile.addNewCard(card)

    def getLastCard(self):
        return pile.getLastCard()

    def getPile(self):
        return pile.getPile()
'''