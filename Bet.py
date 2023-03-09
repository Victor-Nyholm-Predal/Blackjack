from ChipClasses import Chips

class Bet():

    amountOf100 = 0
    amountOf25 = 0
    amountOf10 = 0
    amountOf5 = 0
    amountOf1 = 0
    amountOf0point1 = 0

    def __init__(self, amountOf100, amountOf25, amountOf10, amountOf5, amountOf1, amountOf0point1):
        self.amountOf100 = amountOf100
        self.amountOf25 = amountOf25
        self.amountOf10 = amountOf10
        self.amountOf5 = amountOf5
        self.amountOf1 = amountOf1
        self.amountOf0point1 = amountOf0point1

    def getTotalBet(self):
        bet = 0
        bet += self.amountOf100 * Chips.chip100.value
        bet += self.amountOf25 * Chips.chip25.value
        bet += self.amountOf10 * Chips.chip10.value
        bet += self.amountOf5 * Chips.chip5.value
        bet += self.amountOf1 * Chips.chip1.value
        bet += self.amountOf0point1 * Chips.chip0point1.value
        return bet

    def addChipToBet(self, chip):
        if chip.value == Chips.chip100.value:
            self.amountOf100 += 1
        elif chip.value == Chips.chip25.value:
            self.amountOf25 += 1
        elif chip.value == Chips.chip10.value:
            self.amountOf10 += 1
        elif chip.value == Chips.chip5.value:
            self.amountOf5 += 1
        elif chip.value == Chips.chip1.value:
            self.amountOf1 += 1
        elif chip.value == Chips.chip0point1.value:
            self.amountOf0point1 += 1

    def subtractChip(self, chip):
        if chip.value == Chips.chip100.value:
            self.amountOf100 -= 1
        elif chip.value == Chips.chip25.value:
            self.amountOf25 -= 1
        elif chip.value == Chips.chip10.value:
            self.amountOf10 -= 1
        elif chip.value == Chips.chip5.value:
            self.amountOf5 -= 1
        elif chip.value == Chips.chip1.value:
            self.amountOf1 -= 1
        elif chip.value == Chips.chip0point1.value:
            self.amountOf0point1 -= 1

    def getAmountOf100(self):
        return self.amountOf100

    def getAmountOf25(self):
        return self.amountOf25

    def getAmountOf10(self):
        return self.amountOf10

    def getAmountOf5(self):
        return self.amountOf5

    def getAmountOf1(self):
        return self.amountOf1

    def getAmountOf0point1(self):
        return self.amountOf0point1

    def clearBet(self):
        self.amountOf100 = 0
        self.amountOf25 = 0
        self.amountOf10 = 0
        self.amountOf5 = 0
        self.amountOf1 = 0
        self.amountOf0point1 = 0

    def getListOfChips(self):
        chipsList = []

        for i in range(self.amountOf0point1):
            chipsList.append(Chips.chip0point1)
        for i in range(self.amountOf1):
            chipsList.append(Chips.chip1)
        for i in range(self.amountOf5):
            chipsList.append(Chips.chip5)
        for i in range(self.amountOf10):
            chipsList.append(Chips.chip10)
        for i in range(self.amountOf25):
            chipsList.append(Chips.chip25)
        for i in range(self.amountOf100):
            chipsList.append(Chips.chip100)

        return chipsList

    def getTotalAmountOfChipsInBet(self):
        amount = 0

        amount += self.getAmountOf100()
        amount += self.getAmountOf25()
        amount += self.getAmountOf10()
        amount += self.getAmountOf5()
        amount += self.getAmountOf1()
        amount += self.getAmountOf0point1()

        return amount

    def doubleBet(self):
        self.amountOf100 += self.amountOf100
        self.amountOf25 += self.amountOf25
        self.amountOf10 += self.amountOf10
        self.amountOf5 += self.amountOf5
        self.amountOf1 += self.amountOf1
        self.amountOf0point1 += self.amountOf0point1

    def getListOfSplitOrDoubleChips(self):
        chipsList = []

        for i in range(int(self.amountOf0point1 / 2)):
            chipsList.append(Chips.chip0point1)
        for i in range(int(self.amountOf1 / 2)):
            chipsList.append(Chips.chip1)
        for i in range(int(self.amountOf5 / 2)):
            chipsList.append(Chips.chip5)
        for i in range(int(self.amountOf10 / 2)):
            chipsList.append(Chips.chip10)
        for i in range(int(self.amountOf25 / 2)):
            chipsList.append(Chips.chip25)
        for i in range(int(self.amountOf100 / 2)):
            chipsList.append(Chips.chip100)

        return chipsList

    def copyLastBet(self, lastHand):
        for i in range(len(lastHand)):
            self.addChipToBet(lastHand[i])
