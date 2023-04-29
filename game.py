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