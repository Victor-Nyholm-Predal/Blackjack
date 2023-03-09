import pygame
import os
from math import cos, radians
from pictures import cardPictures, chipsPictures
from button import button_class
from Service import Service
from ChipClasses import Chips

service = Service()

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screenWidth = 1200
screenHeight = 650

screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Blackjack")
icon = pygame.image.load("blackjack_icon.png")
pygame.display.set_icon(icon)

green = (46, 84, 44)
blue = (43, 50, 255)
grey = (130, 130, 130)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

chipHeight = chipsPictures.blackChip.get_height()
chipWidth = chipsPictures.blackChip.get_width()
buttonSpace = screenWidth / 240
buttonHeight = chipHeight
buttonWidth = (screenWidth - (chipWidth + buttonSpace) * 6 - buttonSpace * 8) / 7  # 100 #75

clearBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 7 - (chipWidth + buttonSpace) * 6,
                        screenHeight - (chipHeight + buttonSpace), buttonWidth, buttonHeight, True, "Clear")
copyBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 6 - (chipWidth + buttonSpace) * 6,
                       screenHeight - (chipHeight + buttonSpace), buttonWidth, buttonHeight, True, "Copy")
bet100Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 6,
                         screenHeight - (chipHeight + buttonSpace), chipWidth, chipHeight, True, "")
bet25Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 5,
                        screenHeight - (chipHeight + buttonSpace), chipWidth, chipHeight, True, "")
bet10Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 4,
                        screenHeight - (chipHeight + buttonSpace), chipWidth, chipHeight, True, "")
bet5Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 3,
                       screenHeight - (chipHeight + buttonSpace), chipWidth, chipHeight, True, "")
bet1Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 2,
                       screenHeight - (chipHeight + buttonSpace), chipWidth, chipHeight, True, "")
bet0point1Btn = button_class(green, screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 1,
                             screenHeight - (buttonHeight + buttonSpace), chipWidth, chipHeight, True, "")
dealBtn = button_class(blue, screenWidth - (buttonWidth + buttonSpace) * 5, screenHeight - (buttonHeight + buttonSpace),
                       buttonWidth, buttonHeight, True, "Deal")
hitBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 4, screenHeight - (buttonHeight + buttonSpace),
                      buttonWidth, buttonHeight, False, "Hit")
standBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 3,
                        screenHeight - (buttonHeight + buttonSpace), buttonWidth, buttonHeight, False, "Stand")
doubleBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 2,
                         screenHeight - (buttonHeight + buttonSpace), buttonWidth, buttonHeight, False, "Double")
splitBtn = button_class(grey, screenWidth - (buttonWidth + buttonSpace) * 1,
                        screenHeight - (buttonHeight + buttonSpace), buttonWidth, buttonHeight, False, "Split")
yesBtn = button_class(blue, screenWidth / 2 - 150, screenHeight / 2, 100, 50, False, "Yes")
noBtn = button_class(blue, screenWidth / 2 + 50, screenHeight / 2, 100, 50, False, "No")

running = True
cardsMoving = False
askingForInsurance = False

cardWidth = cardPictures.cardBack.get_width()
cardHalfWidth = cardWidth / 2
cardHeight = cardPictures.cardBack.get_height()
cardHalfHeight = cardHeight / 2
cardDisplacemnet = 20  # 25

# TODO: cardDisplacement så att den ändras för spelaren eller annan lösning så korten aldrig krockar med dealerns kort

# Some variables to show-off the card
d = 1  # Direction to spin
speed = 4  # Spin speed
a = 0  # Angle to show
turns = 180 / (d * speed)

cardStartX = screenWidth - cardHalfWidth - 25
cardStartY = cardHalfHeight + 25
# cardStartX = 1117
# cardStartY = 97.5

cardPosX = screenWidth / 2
cardPosY = screenHeight - 275  # 525

cardX = cardStartX
cardY = cardStartY

chipPosX = screenWidth / 2 - chipWidth / 2
chipPosY = screenHeight - 150  # 675

chipsTotalScoreX = buttonSpace
chipsTotalScoreY = screenHeight - (buttonHeight + buttonSpace) * 2  # screenHeight - (buttonHeight + buttonSpace)
chipsTotalScoreWidth = screenWidth - (buttonWidth + buttonSpace) * 5 - (
            chipWidth + buttonSpace) * 6 - buttonSpace * 2  # screenWidth - (buttonWidth + buttonSpace) * 7 - (chipWidth + buttonSpace) * 6 - buttonSpace * 2
chipsTotalScoreHeight = buttonHeight

askForInsuranceWindowWidth = int(screenWidth / 3)
askForInsuranceWindowHeight = int(screenHeight * 4 / 13)
askForInsuranceWindowX = (screenWidth - askForInsuranceWindowWidth) / 2
askForInsuranceWindowY = (screenHeight - askForInsuranceWindowHeight) / 2

dealerSpacedCardsLimit = 5

fontScore = pygame.font.SysFont("Comicsans", 100)
fontChips = pygame.font.SysFont("Comicsans", 40)
fontWinner = pygame.font.SysFont("Comicsans", 60)
fontBet = pygame.font.SysFont("Comicsans", 30)

#TODO: Tjock i andra (vänstra) högen när spiltat inte automatisk omstart
#TODO: avsluta spelet också efter


def drawCard(x, y, card, angle):
    cardSurface = pygame.Surface((cardWidth, cardHeight))  # creates surface

    tx, ty = x - cardHalfWidth, y - cardHalfHeight  # Top-left co-ordinates
    w = cardWidth  # Width of card
    cardSurface.blit(card, (0, 0))  # Blits the front of the card (white side)

    if angle < 90:  # If the card is still turned over (or the back is still visible)
        cardSurface.blit(cardPictures.cardBack, (0, 0))  # Draw back of card (red side)

        if angle > 0:  # If not completely faced down
            # rotate
            w = cos(radians(angle)) * cardWidth  # Work out the new width based on the angle and original width
            cardSurface = pygame.transform.scale(cardSurface, (int(w), cardHeight))  # Scale the width

    elif angle == 90:  # If exactly horizontal
        cardSurface.blit(cardPictures.cardBack, (0, 0))
        w = 1  # Display the back in a 1 pixel width surface
        cardSurface = pygame.transform.scale(cardSurface, (int(w), cardHeight))

    elif angle < 180:  # Same as before
        # rotate
        w = cos(radians(180 - angle)) * cardWidth
        cardSurface = pygame.transform.scale(cardSurface, (int(w), cardHeight))

    px = x - int(
        w / 2)  # Works out the new place-x coordinate based on the new width (ensuring the centre point remains the same regardless of width)
    screen.blit(cardSurface, (int(px), int(ty)))


def message_to_screen(msg, color, font, x, y):
    screen_text = font.render(str(msg), True, color)

    if font == fontBet:
        x -= screen_text.get_width()

    else:
        x -= screen_text.get_width() / 2

    y -= screen_text.get_height() / 2

    screen.blit(screen_text, (x, y))


def blitWinnerMsg():
    winner = service.checkForWinner()

    for i in range(len(winner)):
        if i == 0:
            x = 450
        else:
            x = 700

        if winner[i] == 0:
            message_to_screen("Blackjack!", white, fontWinner, x, 200)
        elif winner[i] == 1:
            message_to_screen("You win!", white, fontWinner, x, 200)
        elif winner[i] == 2:
            message_to_screen("Tie!", white, fontWinner, x, 200)
        elif winner[i] == 3:
            message_to_screen("Dealer win!", white, fontWinner, x, 200)


def updateScore():
    message_to_screen(service.getDealerScore(), white, fontScore, 100, cardStartY)
    message_to_screen(service.getPlayerScore(), white, fontScore, 100, cardPosY)
    if service.getPlayerAmountOfCards() >= 1 and service.getPlayerSplitAmountOfCards() >= 1:
        message_to_screen(service.getPlayerSplitScore(), white, fontScore, 1000, cardPosY)


def updateChips():
    pygame.draw.rect(screen, grey,
                     (chipsTotalScoreX - 2, chipsTotalScoreY - 2, chipsTotalScoreWidth + 4, chipsTotalScoreHeight + 4))
    pygame.draw.rect(screen, black, (chipsTotalScoreX, chipsTotalScoreY, chipsTotalScoreWidth, chipsTotalScoreHeight))

    msg = "{chips:.2f} $"

    message_to_screen(msg.format(chips=service.getPlayerChips()), yellow, fontChips,
                      chipsTotalScoreX + chipsTotalScoreWidth / 2, chipsTotalScoreY + chipsTotalScoreHeight / 2)


def turnBtnOff(btn):
    btn.color = grey
    btn.enabled = False


def turnBtnOn(btn):
    btn.color = blue
    btn.enabled = True


def adjustAngle(a, d, i):
    a += d * speed * i  # Increases/Decreases angle
    # if a >= 180:  # If fully revealed
    #    a = 180
    #    d = -1  # Switch direction
    # elif a <= 0:  # If fully turned-over
    #    a = 0
    #    d = 1  # Switch direction

    return a


def updateBtns():
    if service.isAbleToDeal() is True:
        turnBtnOn(dealBtn)
    else:
        turnBtnOff(dealBtn)

    if service.isAbleToSplit() is True:
        turnBtnOn(splitBtn)
    else:
        turnBtnOff(splitBtn)

    if service.isAbleToDouble() is True:
        turnBtnOn(doubleBtn)
    else:
        turnBtnOff(doubleBtn)

    if service.isAbleToHitOrStand() is True:
        turnBtnOn(hitBtn)
        turnBtnOn(standBtn)
    else:
        turnBtnOff(hitBtn)
        turnBtnOff(standBtn)

    if service.isHandActive() is True:
        bet100Btn.enabled = False
        bet25Btn.enabled = False
        bet10Btn.enabled = False
        bet5Btn.enabled = False
        bet1Btn.enabled = False
        bet0point1Btn.enabled = False
    else:
        bet100Btn.enabled = True
        bet25Btn.enabled = True
        bet10Btn.enabled = True
        bet5Btn.enabled = True
        bet1Btn.enabled = True
        bet0point1Btn.enabled = True

    if service.isAbleToClearBet() is True:
        turnBtnOn(clearBtn)
    else:
        turnBtnOff(clearBtn)

    if service.isAbleToCopyBet() is True:
        turnBtnOn(copyBtn)
    else:
        turnBtnOff(copyBtn)

    clearBtn.draw(screen, black)
    copyBtn.draw(screen, black)
    dealBtn.draw(screen, black)
    hitBtn.draw(screen, black)
    standBtn.draw(screen, black)
    doubleBtn.draw(screen, black)
    splitBtn.draw(screen, black)

    screen.blit(Chips.chip100.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 6,
                                    screenHeight - (chipHeight + buttonSpace)))
    screen.blit(Chips.chip25.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 5,
                                   screenHeight - (chipHeight + buttonSpace)))
    screen.blit(Chips.chip10.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 4,
                                   screenHeight - (chipHeight + buttonSpace)))
    screen.blit(Chips.chip5.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 3,
                                  screenHeight - (chipHeight + buttonSpace)))
    screen.blit(Chips.chip1.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 2,
                                  screenHeight - (chipHeight + buttonSpace)))
    screen.blit(Chips.chip0point1.img, (screenWidth - (buttonWidth + buttonSpace) * 5 - (chipWidth + buttonSpace) * 1,
                                        screenHeight - (chipHeight + buttonSpace)))


def moveCards(i):
    for j in range(service.dealer.getAmountOfCards()):
        cardX = int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + (cardWidth + cardDisplacemnet) * j)

        change = (cardX - (
            int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + cardDisplacemnet * j))) / turns

        cardX -= change * i
        screen.blit(service.dealer.getPile()[j].img, (int(cardX), int(cardStartY - cardHalfHeight)))


def markActivePile():
    if cardsMoving == False:
        if service.playerHasSplit() == False:
            amount = service.getPlayerAmountOfCards()
            changeX = 0
        elif service.playerSplitStand() == False:
            amount = service.getPlayerSplitAmountOfCards()
            changeX = 180
        else:
            amount = service.getPlayerAmountOfCards()
            changeX = -180

        for i in range(amount):
            screen.blit(cardPictures.glow, (int(cardPosX - cardHalfWidth + changeX - 10 + cardDisplacemnet * i),
                                            int(cardPosY - cardHalfHeight - 10 - cardDisplacemnet * i)))


def blitPlayerCards():
    #print(cardsMoving)
    for i in range(service.getPlayerAmountOfCards()):
        if service.playerHasSplit() == False and service.getPlayerSplitAmountOfCards() != 1:
            screen.blit(service.getPlayerPile()[i].img, (int(cardPosX - cardHalfWidth + cardDisplacemnet * i),
                                                  int(cardPosY - cardHalfHeight - cardDisplacemnet * i)))
        elif service.playerHasSplit() == True and service.getPlayerAmountOfCards() >= 1 and service.getPlayerSplitAmountOfCards() >= 1 and cardsMoving == False:
            for j in range(service.getPlayerAmountOfCards()):
                screen.blit(service.getPlayerPile()[j].img, (int(cardPosX - cardHalfWidth - 180 + cardDisplacemnet * j),
                                                      int(cardPosY - cardHalfHeight - cardDisplacemnet * j)))
            for k in range(service.getPlayerSplitAmountOfCards()):
                screen.blit(service.getPlayerSplitPile()[k].img, (int(cardPosX - cardHalfWidth + 180 + cardDisplacemnet * k),
                                                           int(cardPosY - cardHalfHeight - cardDisplacemnet * k)))


def blitDealerCards():
    for i in range(service.dealer.getAmountOfCards()):
        if service.dealer.getAmountOfCards() > dealerSpacedCardsLimit:
            screen.blit(service.dealer.getPile()[i].img, (
            int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + cardDisplacemnet * i),
            int(cardStartY - cardHalfHeight)))
        elif service.dealer.getAmountOfCards() < dealerSpacedCardsLimit or service.dealer.getAmountOfCards() == dealerSpacedCardsLimit and service.dealer.getScore() >= 17:
            screen.blit(service.dealer.getPile()[i].img, (
            int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + (cardWidth + cardDisplacemnet) * i),
            int(cardStartY - cardHalfHeight)))

    if service.dealer.faceDownCards == 1:
        screen.blit(cardPictures.cardBack, (int(cardPosX - cardHalfWidth), int(cardStartY - cardHalfHeight)))


def blitDeck():
    for i in range(20):
        screen.blit(cardPictures.cardBack, (cardStartX - cardHalfHeight + i, cardStartY - cardHalfWidth - i))


def blitBet():
    msg = "{bet:.2f} $"

    if service.playerHasSplit() == False:
        bet = service.getPlayerTotalBet()
    else:
        bet = (service.getPlayerTotalBet()) / 2
        message_to_screen(msg.format(bet=bet), yellow, fontBet, chipPosX - chipWidth, chipPosY + chipHeight / 2 + 50)

    message_to_screen(msg.format(bet=bet), yellow, fontBet, chipPosX - chipWidth, chipPosY + chipHeight / 2)

def blitStacks():
    stacks = 0
    if service.playerHasSplit() == False and service.playerHasDoubled() == False:
        for i in range(service.getPlayerTotalAmountOfChipsInBet()):
            if i != 0 and i % 10 == 0:
                stacks += 1

            screen.blit(service.getPlayerListOfChips()[i].img, (chipPosX + 75 * stacks, chipPosY - 5 * i + 50 * stacks))

    if service.playerHasSplit() == True or service.playerHasDoubled() == True:
        for i in range(int(service.getPlayerTotalAmountOfChipsInBet() / 2)):
            if i != 0 and i % 10 == 0:
                stacks += 1

            screen.blit(service.getPlayerListOfSplitOrDoubleChips()[i].img,
                        (chipPosX + 75 * stacks, chipPosY - 5 * i + 50 * stacks))
            screen.blit(service.getPlayerListOfSplitOrDoubleChips()[i].img,
                        (chipPosX + 75 * stacks, chipPosY + 50 - 5 * i + 50 * stacks))


def updateBet():
    blitStacks()
    blitBet()


def updateScreen():
    screen.fill(green)

    message_to_screen("Dealer must draw to 16 and stand on all 17's", white, fontChips, screenWidth / 2, screenHeight / 2)

    pygame.draw.ellipse(screen, yellow,
                        (int(chipPosX - chipWidth / 2), int(chipPosY - chipHeight / 2), chipWidth * 2, chipHeight * 2),
                        2)

    updateBtns()
    updateScore()
    blitDeck()
    updateChips()
    updateBet()

    if service.isHandActive() is True:
        markActivePile()
        blitPlayerCards()
        blitDealerCards()


def playerNewCard(a, d, cardX, cardY):
    theCard = service.drawNewCard()

    for i in range(int(turns)):

        if service.playerHasSplit() == False:
            cardX -= ((cardStartX - cardPosX) - cardDisplacemnet * service.getPlayerAmountOfCards()) / turns
            cardY += ((cardPosY - cardStartY) - cardDisplacemnet * service.getPlayerAmountOfCards()) / turns
        elif service.playerHasSplit() == True and service.playerSplitStand() == False:
            cardX -= ((cardStartX - (cardPosX + 180)) - cardDisplacemnet * service.getPlayerSplitAmountOfCards()) / turns
            cardY += ((cardPosY - cardStartY) - cardDisplacemnet * service.getPlayerSplitAmountOfCards()) / turns
        elif service.playerHasSplit() == True and service.playerSplitStand() == True:
            cardX -= ((cardStartX - (cardPosX - 180)) - cardDisplacemnet * service.getPlayerAmountOfCards()) / turns
            cardY += ((cardPosY - cardStartY) - cardDisplacemnet * service.getPlayerAmountOfCards()) / turns

        drawCard(cardX, cardY, theCard.img, adjustAngle(a, d, i))
        pygame.display.update()
        updateScreen()

    if service.playerHasSplit() == True and service.playerSplitStand() == False:
        service.addNewSplitCardToPlayer(theCard)
        if service.getPlayerSplitScore() > 21:
            service.turnPlayerSplitStandOn()
    else:
        service.addNewCardToPlayer(theCard)

    updateScreen()


def dealerNewCard(a, d, cardX, cardY):
    theCard = service.drawNewCard()

    for i in range(int(turns)):
        if service.dealer.getAmountOfCards() == dealerSpacedCardsLimit:
            moveCards(i)

        if service.dealer.getAmountOfCards() < dealerSpacedCardsLimit:
            cardX -= ((cardStartX - cardPosX + (cardWidth + cardDisplacemnet)) - (
                        cardWidth + cardDisplacemnet) * service.dealer.getAmountOfCards()) / turns
        else:
            cardX -= ((cardStartX - cardPosX + (
                        cardWidth + cardDisplacemnet)) - cardDisplacemnet * service.dealer.getAmountOfCards()) / turns

        drawCard(cardX, cardY, theCard.img, adjustAngle(a, d, i))
        pygame.display.update()
        updateScreen()

    service.dealer.addNewCard(theCard)

    updateScreen()


def dealerSecondCard(cardX):
    for i in range(int(turns)):
        cardX -= (cardStartX - cardPosX) / turns
        screen.blit(cardPictures.cardBack, (int(cardX - cardHalfWidth), int(cardStartY - cardHalfHeight)))
        pygame.display.update()
        updateScreen()

    service.dealer.faceDownCards += 1
    updateScreen()


def turnDealersSecondCard(a, d):
    theCard = service.drawNewCard()

    service.dealer.faceDownCards -= 1
    for i in range(int(turns)):
        drawCard(cardPosX, cardStartY, theCard.img, adjustAngle(a, d, i))
        pygame.display.update()
        updateScreen()

    service.dealer.addNewCard(theCard)


def stand():
    if service.playerHasSplit() is True and service.playerSplitStand() is False:
        service.turnPlayerSplitStandOn()
        updateScreen()
    else:
        turnBtnOff(hitBtn)
        turnBtnOff(standBtn)
        turnBtnOff(doubleBtn)
        turnBtnOff(splitBtn)
        turnDealersSecondCard(a, d)
        updateScreen()

        while service.dealer.getScore() <= 16:
            dealerNewCard(a, d, cardX, cardY)
            updateScreen()


def double():
    service.double()

    playerNewCard(a, d, cardX, cardY)
    updateScreen()

    stand()
    updateScreen()


def split():
    service.player.beforeSplit()
    service.player.afterSplit()

    global cardsMoving
    cardsMoving = True

    for i in range(int(turns)):
        for j in range(service.getPlayerTotalAmountOfCards()):
            cardX = (cardPosX + cardDisplacemnet * j)
            cardY = (cardPosY - cardDisplacemnet * j)

            changeX = (cardPosX - (int(cardX) - 180)) / turns
            changeY = (cardPosY - (int(cardY))) / turns

            if j == 0:
                cardX -= changeX * i
                screen.blit(service.getPlayerLastCard().img, (int(cardX - cardHalfWidth), int(cardY - cardHalfHeight)))

            elif j == 1:
                cardX += changeX * i
                cardY += changeY * i
                screen.blit(service.getPlayerSplitLastCard().img, (int(cardX - cardHalfWidth), int(cardY - cardHalfHeight)))

            #screen.blit(service.getPlayerPile()[j].img, (int(cardX - cardHalfWidth), int(cardY - cardHalfHeight)))

        #if i == turns - 1:
        #    service.player.afterSplit()

        if i == turns - 1:

            cardsMoving = False

        pygame.display.update()
        updateScreen()


def clearDealerCards(i):
    if service.dealer.getAmountOfCards() == 1:
        amountOfCards = 2
    else:
        amountOfCards = service.dealer.getAmountOfCards()
    for j in range(amountOfCards):

        cardY = int(cardStartY - cardHalfHeight)

        if service.dealer.getAmountOfCards() <= dealerSpacedCardsLimit:

            cardX = int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + (cardWidth + cardDisplacemnet) * j)

        else:

            cardX = int(cardPosX - (cardWidth + cardDisplacemnet + cardHalfWidth) + cardDisplacemnet * j)

        changeX = (cardX - 200) / turns
        changeY = (cardY + cardHeight + 20) / turns

        x = cardX - changeX * i
        y = cardY - changeY * i

        if service.dealer.getAmountOfCards() == 1 and j == 1:
            cardImg = cardPictures.cardBack
        else:
            cardImg = service.dealer.getPile()[j].img

        screen.blit(cardImg, (int(x), int(y)))


def clearPlayerCards(i):
    if service.playerHasSplit() == False:
        for j in range(service.getPlayerAmountOfCards()):

            cardX = int(cardPosX - cardHalfWidth + cardDisplacemnet * j)
            cardY = int(cardPosY - cardHalfHeight - cardDisplacemnet * j)

            changeX = (cardX - 200) / turns
            changeY = (cardY + cardHeight + 20) / turns

            x = cardX - changeX * i
            y = cardY - changeY * i

            screen.blit(service.getPlayerPile()[j].img, (int(x), int(y)))

    else:
        for j in range(service.getPlayerAmountOfCards()):

            cardX = int(cardPosX - cardHalfWidth - 180 + cardDisplacemnet * j)
            cardY = int(cardPosY - cardHalfHeight - cardDisplacemnet * j)

            changeX = (cardX - 200) / turns
            changeY = (cardY + cardHeight + 20) / turns

            x = cardX - changeX * i
            y = cardY - changeY * i

            screen.blit(service.getPlayerPile()[j].img, (int(x), int(y)))

        for k in range(service.getPlayerSplitAmountOfCards()):

            cardX = int(cardPosX - cardHalfWidth + 180 + cardDisplacemnet * k)
            cardY = int(cardPosY - cardHalfHeight - cardDisplacemnet * k)

            changeX = (cardX - 200) / turns
            changeY = (cardY + cardHeight + 20) / turns

            x = cardX - changeX * i
            y = cardY - changeY * i

            screen.blit(service.getPlayerSplitPile()[k].img, (int(x), int(y)))


def clearTable():
    for i in range(int(turns)):
        clearDealerCards(i)
        clearPlayerCards(i)
        pygame.display.update()
        updateScreen()


def askForInsurance():
    turnBtnOn(yesBtn)
    turnBtnOn(noBtn)
    pygame.draw.rect(screen, white, (askForInsuranceWindowX, askForInsuranceWindowY, askForInsuranceWindowWidth, askForInsuranceWindowHeight))
    message_to_screen("Do you want insurance?", black, fontChips, screenWidth / 2, (screenHeight - 100) / 2)
    yesBtn.draw(screen, black)
    noBtn.draw(screen, black)


def dealNewHand():
    service.startHand()
    service.updateLastBet()
    playerNewCard(a, d, cardX, cardY)
    dealerNewCard(a, d, cardX, cardY)
    playerNewCard(a, d, cardX, cardY)
    dealerSecondCard(cardX)
    if service.dealer.getLastCard().value == 11:
        askForInsurance()


def restart():
    clearTable()
    service.resetDealerAndPlayer()
    updateScreen()


def changeBet(button, chip):
    if button == 1:
        service.placeBet(chip)
    elif button == 3:
        service.subtractChip(chip)

    pygame.display.update()
    updateScreen()


def gameEnded():
    blitWinnerMsg()
    pygame.display.update()
    service.executeBetWithDelay()
    restart()


updateScreen()

while running:

    if service.gameEnded() is True:
        gameEnded()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:  # pygame.QUIT funkar inte... Returnerar fel värde...
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and dealBtn.isOver(pos) is True and dealBtn.enabled is True:
            dealNewHand()

        elif event.type == pygame.MOUSEBUTTONDOWN and hitBtn.isOver(pos) is True and hitBtn.enabled is True:
            playerNewCard(a, d, cardX, cardY)
            updateScreen()

        elif event.type == pygame.MOUSEBUTTONDOWN and standBtn.isOver(pos) is True and standBtn.enabled is True:
            stand()

        elif event.type == pygame.MOUSEBUTTONDOWN and doubleBtn.isOver(pos) is True and doubleBtn.enabled is True:
            double()

        elif event.type == pygame.MOUSEBUTTONDOWN and splitBtn.isOver(pos) is True and splitBtn.enabled is True:
            split()

        elif event.type == pygame.MOUSEBUTTONDOWN and bet100Btn.isOver(pos) is True and bet100Btn.enabled is True:
            changeBet(event.button, Chips.chip100)
        elif event.type == pygame.MOUSEBUTTONDOWN and bet25Btn.isOver(pos) is True and bet25Btn.enabled is True:
            changeBet(event.button, Chips.chip25)
        elif event.type == pygame.MOUSEBUTTONDOWN and bet10Btn.isOver(pos) is True and bet10Btn.enabled is True:
            changeBet(event.button, Chips.chip10)
        elif event.type == pygame.MOUSEBUTTONDOWN and bet5Btn.isOver(pos) is True and bet5Btn.enabled is True:
            changeBet(event.button, Chips.chip5)
        elif event.type == pygame.MOUSEBUTTONDOWN and bet1Btn.isOver(pos) is True and bet1Btn.enabled is True:
            changeBet(event.button, Chips.chip1)
        elif event.type == pygame.MOUSEBUTTONDOWN and bet0point1Btn.isOver(pos) is True and bet0point1Btn.enabled is True:
            changeBet(event.button, Chips.chip0point1)

        elif event.type == pygame.MOUSEBUTTONDOWN and clearBtn.isOver(pos) is True and clearBtn.enabled is True:
            service.clearBet()
            updateScreen()
        elif event.type == pygame.MOUSEBUTTONDOWN and copyBtn.isOver(pos) is True and copyBtn.enabled is True:
            service.copyLastBet()
            dealNewHand()

        elif event.type == pygame.MOUSEBUTTONDOWN and yesBtn.isOver(pos) is True and yesBtn.enabled:
            service.insurance()
            updateScreen()
        elif event.type == pygame.MOUSEBUTTONDOWN and noBtn.isOver(pos) is True and noBtn.enabled:
            updateScreen()

        break

    pygame.display.update()
