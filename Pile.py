class Pile():

    score = 0
    amountOfCards = 0
    highAces = 0

    def __init__(self, score, amountOfCards, highAces):
        self.cards = []
        self.score = score
        self.amountOfCards = amountOfCards
        self.highAces = highAces

    def getScore(self):
        score = 0
        highAces = 0
        try:
            for i in range(self.getAmountOfCards()):
                score += self.cards[i].value
                if self.cards[i].rank == "Ace":
                    highAces += 1
                if score > 21 and highAces > 0:
                    score -= 10
                    highAces -= 1
        except TypeError:
            score = 0
        self.score = score
        return score

    def getAmountOfCards(self):
        return len(self.cards)

    def addNewCard(self, card):
        self.cards.append(card)

    def getLastCard(self):
        return self.cards[self.getAmountOfCards() - 1]

    def getPile(self):
        return self.cards
