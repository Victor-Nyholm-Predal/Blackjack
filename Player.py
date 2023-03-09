from Person import Person
from Pile import Pile
from Bet import Bet

class Player(Person):

    def __init__(self, amountOfCards, highAces, chips, hasSplit, splitStand, hasDoubled, insurance):
        super().__init__(amountOfCards, highAces)
        self.chips = chips
        self.hasSplit = hasSplit
        self.pile0 = Pile(0, 0, 0)
        self.splitStand = splitStand
        self.bet = Bet(0, 0, 0, 0, 0, 0,)
        self.hasDoubled = hasDoubled
        self.lastHand = []
        self.insurance = insurance

    def doubleBet(self):
        self.chips -= self.getTotalBet()
        self.bet.doubleBet()

    def beforeSplit(self):
        self.hasSplit = True
        self.doubleBet()

    def afterSplit(self):
        splitCard = self.pile.getLastCard()
        self.pile.cards.remove(splitCard)
        self.pile0.addNewCard(splitCard)

    def getSplitAmountOfCards(self):
        return self.pile0.getAmountOfCards()

    def getSplitLastCard(self):
        return self.pile0.getLastCard()

    def getSplitPile(self):
        return self.pile0.getPile()

    def getSplitScore(self):
        return self.pile0.getScore()

    def addNewSplitCard(self, card):
        self.pile0.addNewCard(card)

    def clearSplitPile(self):
        self.pile0.cards.clear()

    def getChips(self):
        if self.insurance == False:
            return self.chips
        else:
            if self.hasSplit == True or self.hasDoubled == True:
                return self.chips - self.getTotalBet() * 0.25
            else:
                return self.chips - self.getTotalBet() * 0.5

    def getTotalBet(self):
        return self.bet.getTotalBet()

    def addChipToBet(self, chip):
        self.bet.addChipToBet(chip)

    def subtractChip(self, chip):
        self.bet.subtractChip(chip)

    def getAmountOfChipsLeft(self):
        return self.chips

    def getAmountOf100(self):
        return self.bet.getAmountOf100()

    def getAmountOf25(self):
        return self.bet.getAmountOf25()

    def getAmountOf10(self):
        return self.bet.getAmountOf10()

    def getAmountOf5(self):
        return self.bet.getAmountOf5()

    def getAmountOf1(self):
        return self.bet.getAmountOf1()

    def getAmountOf0point1(self):
        return self.bet.getAmountOf0point1()

    def clearBet(self):
        self.bet.clearBet()

    def getListOfChips(self):
        return self.bet.getListOfChips()

    def getTotalAmountOfChipsInBet(self):
        return self.bet.getTotalAmountOfChipsInBet()

    def double(self):
        self.hasDoubled = True
        self.doubleBet()

    def getListOfSplitOrDoubleChips(self):
        return self.bet.getListOfSplitOrDoubleChips()

    def copyLastBet(self, lastHand):
        self.bet.copyLastBet(lastHand)

    def turnInsuranceOn(self):
        self.insurance = True

    def turnInsuranceOff(self):
        self.insurance = False

    def isHasSplit(self):
        return self.hasSplit

    def isHasDoubled(self):
        return self.hasDoubled

    def isSplitStand(self):
        return self.splitStand

    def turnPlayerSplitStandOn(self):
        self.splitStand = True

    def turnPlayerSplitStandOff(self):
        self.splitStand = False

    def reset(self):
        self.clearPile()
        self.clearSplitPile()
        self.hasSplit = False
        self.splitStand = False
        self.hasDoubled = False
        self.turnInsuranceOff()

    def getTotalAmountOfCards(self):
        return self.getAmountOfCards() + self.getSplitAmountOfCards()

'''
    def __init__(self, score, amountOfCards, highAces, chips, split):
        self.score = score
        self.amountOfCards = amountOfCards
        self.highAces = highAces
        self.chips = chips
        self.split = split

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