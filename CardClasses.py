import random
from pictures import cardPictures

class Card:

    value = ''
    img = ''
    rank = ''

    def __init__(self, value, img, rank):
        self.value = value
        self.img = img
        self.rank = rank

class Deck:

    cardsList = [
        Card(2, cardPictures.TwoOfClubs, 2),
        Card(3, cardPictures.ThreeOfClubs, 3),
        Card(4, cardPictures.FourOfClubs, 4),
        Card(5, cardPictures.FiveOfClubs, 5),
        Card(6, cardPictures.SixOfClubs, 6),
        Card(7, cardPictures.SevenOfClubs, 7),
        Card(8, cardPictures.EightOfClubs, 8),
        Card(9, cardPictures.NineOfClubs, 9),
        Card(10, cardPictures.TenOfClubs, 10),
        Card(10, cardPictures.JackOfClubs, "Jack"),
        Card(10, cardPictures.QueenOfClubs, "Queen"),
        Card(10, cardPictures.KingOfClubs, "King"),
        Card(11, cardPictures.AceOfClubs, "Ace"),

        Card(2, cardPictures.TwoOfDiamonds, 2),
        Card(3, cardPictures.ThreeOfDiamonds, 3),
        Card(4, cardPictures.FourOfDiamonds, 4),
        Card(5, cardPictures.FiveOfDiamonds, 5),
        Card(6, cardPictures.SixOfDiamonds, 6),
        Card(7, cardPictures.SevenOfDiamonds, 7),
        Card(8, cardPictures.EightOfDiamonds, 8),
        Card(9, cardPictures.NineOfDiamonds, 9),
        Card(10, cardPictures.TenOfDiamonds, 10),
        Card(10, cardPictures.JackOfDiamonds, "Jack"),
        Card(10, cardPictures.QueenOfDiamonds, "Queen"),
        Card(10, cardPictures.KingOfDiamonds, "King"),
        Card(11, cardPictures.AceOfDiamonds, "Ace"),

        Card(2, cardPictures.TwoOfHearts, 2),
        Card(3, cardPictures.ThreeOfHearts, 3),
        Card(4, cardPictures.FourOfHearts, 4),
        Card(5, cardPictures.FiveOfHearts, 5),
        Card(6, cardPictures.SixOfHearts, 6),
        Card(7, cardPictures.SevenOfHearts, 7),
        Card(8, cardPictures.EightOfHearts, 8),
        Card(9, cardPictures.NineOfHearts, 9),
        Card(10, cardPictures.TenOfHearts, 10),
        Card(10, cardPictures.JackOfHearts, "Jack"),
        Card(10, cardPictures.QueenOfHearts, "Queen"),
        Card(10, cardPictures.KingOfHearts, "King"),
        Card(11, cardPictures.AceOfHearts, "Ace"),

        Card(2, cardPictures.TwoOfSpades, 2),
        Card(3, cardPictures.ThreeOfSpades, 3),
        Card(4, cardPictures.FourOfSpades, 4),
        Card(5, cardPictures.FiveOfSpades, 5),
        Card(6, cardPictures.SixOfSpades, 6),
        Card(7, cardPictures.SevenOfSpades, 7),
        Card(8, cardPictures.EightOfSpades, 8),
        Card(9, cardPictures.NineOfSpades, 9),
        Card(10, cardPictures.TenOfSpades, 10),
        Card(10, cardPictures.JackOfSpades, "Jack"),
        Card(10, cardPictures.QueenOfSpades, "Queen"),
        Card(10, cardPictures.KingOfSpades, "King"),
        Card(11, cardPictures.AceOfSpades, "Ace"),
        ]

    playerDeck = [
        cardsList[5],
        cardsList[18],
        cardsList[5],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)]
    ]

    playerDeck2 = [
        cardsList[5],
        cardsList[18],
        cardsList[5],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)]
    ]

    dealerDeck = [
        cardsList[0],
        cardsList[0],
        cardsList[0],
        cardsList[0],
        cardsList[0],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)],
        cardsList[random.randint(0, 51)]
    ]

    '''
        cardsList.append(Card([2], cards.TwoOfClubs))
        cardsList.append(Card([3], cards.ThreeOfClubs))
        cardsList.append(Card([4], cards.FourOfClubs))
        cardsList.append(Card([5], cards.FiveOfClubs))
        cardsList.append(Card([6], cards.SixOfClubs))
        cardsList.append(Card([7], cards.SevenOfClubs))
        cardsList.append(Card([8], cards.EightOfClubs))
        cardsList.append(Card([9], cards.NineOfClubs))
        cardsList.append(Card([10], cards.TenOfClubs))
        cardsList.append(Card([10], cards.JackOfClubs))
        cardsList.append(Card([10], cards.QueenOfClubs))
        cardsList.append(Card([10], cards.KingOfClubs))
        cardsList.append(Card([11, 1], cards.AceOfClubs))

        cardsList.append(Card([2], cards.TwoOfDiamonds))
        cardsList.append(Card([3], cards.ThreeOfDiamonds))
        cardsList.append(Card([4], cards.FourOfDiamonds))
        cardsList.append(Card([5], cards.FiveOfDiamonds))
        cardsList.append(Card([6], cards.SixOfDiamonds))
        cardsList.append(Card([7], cards.SevenOfDiamonds))
        cardsList.append(Card([8], cards.EightOfDiamonds))
        cardsList.append(Card([9], cards.NineOfDiamonds))
        cardsList.append(Card([10], cards.TenOfDiamonds))
        cardsList.append(Card([10], cards.JackOfDiamonds))
        cardsList.append(Card([10], cards.QueenOfDiamonds))
        cardsList.append(Card([10], cards.KingOfDiamonds))
        cardsList.append(Card([11, 1], cards.AceOfDiamonds))

        cardsList.append(Card([2], cards.TwoOfHearts))
        cardsList.append(Card([3], cards.ThreeOfHearts))
        cardsList.append(Card([4], cards.FourOfHearts))
        cardsList.append(Card([5], cards.FiveOfHearts))
        cardsList.append(Card([6], cards.SixOfHearts))
        cardsList.append(Card([7], cards.SevenOfHearts))
        cardsList.append(Card([8], cards.EightOfHearts))
        cardsList.append(Card([9], cards.NineOfHearts))
        cardsList.append(Card([10], cards.TenOfHearts))
        cardsList.append(Card([10], cards.JackOfHearts))
        cardsList.append(Card([10], cards.QueenOfHearts))
        cardsList.append(Card([10], cards.KingOfHearts))
        cardsList.append(Card([11, 1], cards.AceOfHearts))

        cardsList.append(Card([2], cards.TwoOfSpades))
        cardsList.append(Card([3], cards.ThreeOfSpades))
        cardsList.append(Card([4], cards.FourOfSpades))
        cardsList.append(Card([5], cards.FiveOfSpades))
        cardsList.append(Card([6], cards.SixOfSpades))
        cardsList.append(Card([7], cards.SevenOfSpades))
        cardsList.append(Card([8], cards.EightOfSpades))
        cardsList.append(Card([9], cards.NineOfSpades))
        cardsList.append(Card([10], cards.TenOfSpades))
        cardsList.append(Card([10], cards.JackOfSpades))
        cardsList.append(Card([10], cards.QueenOfSpades))
        cardsList.append(Card([10], cards.KingOfSpades))
        cardsList.append(Card([11, 1], cards.AceOfSpades))


        self.cardsList.append(Card([2], cards.TwoOfClubs))
        self.cardsList.append(Card([3], cards.ThreeOfClubs))
        self.cardsList.append(Card([4], cards.FourOfClubs))
        self.cardsList.append(Card([5], cards.FiveOfClubs))
        self.cardsList.append(Card([6], cards.SixOfClubs))
        self.cardsList.append(Card([7], cards.SevenOfClubs))
        self.cardsList.append(Card([8], cards.EightOfClubs))
        self.cardsList.append(Card([9], cards.NineOfClubs))
        self.cardsList.append(Card([10], cards.TenOfClubs))
        self.cardsList.append(Card([10], cards.JackOfClubs))
        self.cardsList.append(Card([10], cards.QueenOfClubs))
        self.cardsList.append(Card([10], cards.KingOfClubs))
        self.cardsList.append(Card([11, 1], cards.AceOfClubs))

        self.cardsList.append(Card([2], cards.TwoOfDiamonds))
        self.cardsList.append(Card([3], cards.ThreeOfDiamonds))
        self.cardsList.append(Card([4], cards.FourOfDiamonds))
        self.cardsList.append(Card([5], cards.FiveOfDiamonds))
        self.cardsList.append(Card([6], cards.SixOfDiamonds))
        self.cardsList.append(Card([7], cards.SevenOfDiamonds))
        self.cardsList.append(Card([8], cards.EightOfDiamonds))
        self.cardsList.append(Card([9], cards.NineOfDiamonds))
        self.cardsList.append(Card([10], cards.TenOfDiamonds))
        self.cardsList.append(Card([10], cards.JackOfDiamonds))
        self.cardsList.append(Card([10], cards.QueenOfDiamonds))
        self.cardsList.append(Card([10], cards.KingOfDiamonds))
        self.cardsList.append(Card([11, 1], cards.AceOfDiamonds))

        self.cardsList.append(Card([2], cards.TwoOfHearts))
        self.cardsList.append(Card([3], cards.ThreeOfHearts))
        self.cardsList.append(Card([4], cards.FourOfHearts))
        self.cardsList.append(Card([5], cards.FiveOfHearts))
        self.cardsList.append(Card([6], cards.SixOfHearts))
        self.cardsList.append(Card([7], cards.SevenOfHearts))
        self.cardsList.append(Card([8], cards.EightOfHearts))
        self.cardsList.append(Card([9], cards.NineOfHearts))
        self.cardsList.append(Card([10], cards.TenOfHearts))
        self.cardsList.append(Card([10], cards.JackOfHearts))
        self.cardsList.append(Card([10], cards.QueenOfHearts))
        self.cardsList.append(Card([10], cards.KingOfHearts))
        self.cardsList.append(Card([11, 1], cards.AceOfHearts))

        self.cardsList.append(Card([2], cards.TwoOfSpades))
        self.cardsList.append(Card([3], cards.ThreeOfSpades))
        self.cardsList.append(Card([4], cards.FourOfSpades))
        self.cardsList.append(Card([5], cards.FiveOfSpades))
        self.cardsList.append(Card([6], cards.SixOfSpades))
        self.cardsList.append(Card([7], cards.SevenOfSpades))
        self.cardsList.append(Card([8], cards.EightOfSpades))
        self.cardsList.append(Card([9], cards.NineOfSpades))
        self.cardsList.append(Card([10], cards.TenOfSpades))
        self.cardsList.append(Card([10], cards.JackOfSpades))
        self.cardsList.append(Card([10], cards.QueenOfSpades))
        self.cardsList.append(Card([10], cards.KingOfSpades))
        self.cardsList.append(Card([11, 1], cards.AceOfSpades))
         '''



