import random

# Now some classes that define the different elements of the game

# Class that builds each card
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {serlf.suit}"

# Class that builds each Deck
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '20', 'Jack', 'Queen', 'King']

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))

        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Class that build players hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        ace = False

        for card in self.cards:
            if card.value == "Ace":
                ace = True
            value += self.get_card_value(card)

        if ace and value <= 11:
            value += 10
        return value
    def get_card_value(self, card):
        if card.value in ['Jack', 'Queen', 'King']:
            return 10
        elif card.value == 'Ace':
            return 1
        else:
            return int(card.value)
        
    def __str__(self) -> str:
        cards_string = ""
        for card in self.cards:
            cards_string += str(card) + ", "
        return cards_string[:-2]
    