import random
import time
from CardClasses import Deck
from Player import Player
from Dealer import Dealer
from ChipClasses import Chips

highestValidScore = 21
dealerMustStandScore = 17
highestScoreToDouble = 11
lowestScoreToDouble = 9
betExecutionWaitTime = 3


class Service:
    player = Player(0, 0, 500.00, False, False, False, False)
    dealer = Dealer(0, 0, 0)
    lastBet = []

    activeHand = False

    def startHand(self):
        self.activeHand = True

    def isHandActive(self):
        return self.activeHand

    def playerHasSplit(self):
        return self.player.isHasSplit()

    def playerHasDoubled(self):
        return self.player.isHasDoubled()

    def getDealerScore(self):
        return self.dealer.getScore()

    def getPlayerScore(self):
        return self.player.getScore()

    def getPlayerAmountOfCards(self):
        return self.player.getAmountOfCards()

    def getPlayerSplitAmountOfCards(self):
        return self.player.getSplitAmountOfCards()

    def getPlayerSplitScore(self):
        return self.player.getSplitScore()

    def getPlayerChips(self):
        return self.player.getChips()

    def playerSplitStand(self):
        return self.player.isSplitStand()

    def getPlayerPile(self):
        return self.player.getPile()

    def getPlayerSplitPile(self):
        return self.player.getSplitPile()

    def getPlayerTotalBet(self):
        return self.player.getTotalBet()

    def getPlayerTotalAmountOfChipsInBet(self):
        return self.player.getTotalAmountOfChipsInBet()

    def getPlayerListOfChips(self):
        return self.player.getListOfChips()

    def getPlayerListOfSplitOrDoubleChips(self):
        return self.player.getListOfSplitOrDoubleChips()

    def addNewSplitCardToPlayer(self, theCard):
        self.player.addNewSplitCard(theCard)

    def addNewCardToPlayer(self, theCard):
        self.player.addNewCard(theCard)

    def drawNewCard(self):
        return Deck.cardsList[12]
        #return Deck.cardsList[random.randint(0, 51)]

    def compareScores(self, playerScore, playerAmountOfCards, dealerScore):
        if playerScore == highestValidScore and playerAmountOfCards == 2 and dealerScore >= dealerMustStandScore:
            return 0
        elif highestValidScore >= playerScore > dealerScore >= dealerMustStandScore \
                or dealerScore > highestValidScore:
            return 1
        elif playerScore == dealerScore and playerScore <= highestValidScore and dealerScore >= dealerMustStandScore:
            return 2
        elif playerScore < dealerScore <= highestValidScore and dealerScore >= dealerMustStandScore \
                or playerScore > highestValidScore \
                or self.player.splitStand is True and self.method_name():
            return 3
        else:
            return 101

    def method_name(self):
        return self.player.getSplitScore() < highestValidScore < self.player.getScore()

    def gameEnded(self):
        winner = self.compareScores(self.player.getScore(), self.player.getAmountOfCards(), self.dealer.getScore())

        if self.playerHasSplit() is True and self.player.splitStand is True:
            winnerSplit = self.compareScores(self.player.getSplitScore(), self.player.getAmountOfCards(), self.dealer.getScore())

            if winner != 101 and winnerSplit != 101:
                return True
            else:
                return False

        else:
            if winner != 101:
                return True
            else:
                return False

    def payOutWins(self, winner, bet):
        # bet = player.getTotalBet()

        if winner == 0:
            self.player.chips += bet * 2.5  # 3 #3:2
        elif winner == 1:
            self.player.chips += bet * 2
        elif winner == 2:
            self.player.chips += bet

        if self.player.insurance is True and self.dealer.getAmountOfCards() == 2 and self.dealer.getScore() == highestValidScore:
            if self.playerHasSplit() is True or self.playerHasDoubled() is True:
                self.player.chips += bet * 0.5
            else:
                self.player.chips += bet

    def executeBet(self):
        winner = self.compareScores(self.player.getScore(), self.player.getAmountOfCards(), self.dealer.getScore())

        if self.playerHasSplit() is True:
            self.payOutWins(winner, self.player.getTotalBet() / 2)
            winner0 = self.compareScores(self.player.getSplitScore(), self.player.getSplitAmountOfCards(), self.dealer.getScore())
            self.payOutWins(winner0, self.player.getTotalBet() / 2)
        else:
            self.payOutWins(winner, self.player.getTotalBet())

        self.player.clearBet()
        self.activeHand = False

    def checkForWinner(self):
        winner = self.compareScores(self.player.getScore(), self.player.getAmountOfCards(), self.dealer.getScore())
        if self.playerHasSplit() is True and self.player.splitStand is True:
            winnerSplit = self.compareScores(self.player.getSplitScore(), self.player.getAmountOfCards(), self.dealer.getScore())

            if winner != 101 and winnerSplit != 101:
                return [winner, winnerSplit]

        elif self.playerHasSplit() is False:
            if winner != 101:
                return [winner]

    def updateLastBet(self):
        #global lastBet
        self.lastBet = self.player.getListOfChips()

    def clearBet(self):
        self.player.chips += self.player.getTotalBet()
        self.player.clearBet()

    def copyLastBet(self):
        self.player.copyLastBet(self.lastBet)
        self.player.chips -= self.player.getTotalBet()

    def placeBet(self, chip):
        if round(self.player.getAmountOfChipsLeft(), 2) >= chip.value:
            self.player.addChipToBet(chip)
            self.player.chips -= chip.value

    def subtractChip(self, chip):
        if chip in self.player.getListOfChips():
            self.player.subtractChip(chip)
            self.player.chips += chip.value

    def resetDealerAndPlayer(self):
        self.player.reset()
        self.dealer.reset()
        #self.player.clearPile()
        #self.dealer.clearPile()
        #self.player.clearSplitPile()
        #self.dealer.faceDownCards = 0
        #self.player.hasSplit = False
        #self.player.splitStand = False
        #self.player.hasDoubled = False
        #self.player.turnInsuranceOff()

    def makeInsuranceBet(self):
        insurance = self.player.getTotalBet() / 2
        while insurance != 0:
            if insurance - Chips.chip100.value >= 0:
                print(Chips.chip100.value)
                insurance -= Chips.chip100.value
            elif insurance - Chips.chip25.value >= 0:
                print(Chips.chip25.value)
                insurance -= Chips.chip25.value
            elif insurance - Chips.chip10.value >= 0:
                print(Chips.chip10.value)
                insurance -= Chips.chip10.value
            elif insurance - Chips.chip5.value >= 0:
                print(Chips.chip5.value)
                insurance -= Chips.chip5.value
            elif insurance - Chips.chip1.value >= 0:
                print(Chips.chip1.value)
                insurance -= Chips.chip1.value
            elif insurance - Chips.chip0point1.value >= 0:
                print(Chips.chip0point1.value)
                insurance -= Chips.chip0point1.value

    def insurance(self):
        self.makeInsuranceBet()
        self.player.turnInsuranceOn()

    def double(self):
        self.player.double()

    def isAbleToDeal(self):
        if self.player.getTotalBet() > 0 and self.activeHand is False:
            return True
        else:
            return False

    def isAbleToSplit(self):
        if self.player.getAmountOfCards() == 2 \
                and self.playerHasSplit() is False \
                and self.player.getPile()[0].rank == self.player.getPile()[1].rank:
            return True
        else:
            return False

    def isAbleToDouble(self):
        if self.playerHasSplit() is False \
                and highestScoreToDouble >= self.player.getScore() >= lowestScoreToDouble \
                and self.player.getAmountOfCards() == 2:
            return True
        else:
            return False

    def isAbleToHitOrStand(self):
        if self.player.getScore() <= highestValidScore \
                and self.player.getAmountOfCards() + self.dealer.getAmountOfCards() + self.player.getSplitAmountOfCards() >= 3 \
                and self.dealer.getScore() < dealerMustStandScore:
            return True
        else:
            return False

    def isAbleToClearBet(self):
        if self.player.getTotalBet() > 0 and self.isHandActive() is False:
            return True
        else:
            return False

    def isAbleToCopyBet(self):
        if self.lastBet != [] and self.isHandActive() is False:
            return True
        else:
            return False

    def turnPlayerSplitStandOn(self):
        self.player.turnPlayerSplitStandOn()

    def turnPlayerSplitStandOff(self):
        self.player.turnPlayerSplitStandOff()

    def getPlayerTotalAmountOfCards(self):
        return self.player.getTotalAmountOfCards()

    def getPlayerLastCard(self):
        return self.player.getLastCard()

    def getPlayerSplitLastCard(self):
        return self.player.getSplitLastCard()

    def executeBetWithDelay(self):
        time.sleep(betExecutionWaitTime)
        self.executeBet()
