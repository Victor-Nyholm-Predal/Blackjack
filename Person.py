from Pile import Pile

class Person():

    def __init__(self, amountOfCards, highAces):
        #self.score = score
        self.amountOfCards = amountOfCards
        self.highAces = highAces
        self.pile = Pile(0, 0, 0)

    def getScore(self):
        self.score = self.pile.getScore()
        return self.score

    def getAmountOfCards(self):
        self.amountOfCards = self.pile.getAmountOfCards()
        return self.amountOfCards

    def addNewCard(self, card):
        self.pile.addNewCard(card)

    def getLastCard(self):
        return self.pile.getLastCard()

    def getPile(self):
        return self.pile.getPile()

    def clearPile(self):
        self.pile.cards.clear()