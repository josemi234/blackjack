import random

# Now some classes that define the different elements of the game

# Class that builds each card
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

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

# Start Game
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play_game(self):
        print("Welcome to this Blackjack game!")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Players's hand: {self.player_hand}")
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}")

        while True:
            choice = input("Do you want to hit or stand?")
            if choice.lower() == 'hit':
                self.player_hand.add_card(self.deck.deal_card())
                print(f"Players's hand: {self.player_hand}")
                if self.player_hand.get_value() > 21:
                    print(" Wrong decission, Dealer wins!")
                    return
                
            elif choice.lower() == 'stand':
                break

        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        
        print(f"Players's hand: {self.player_hand}")
        print(f"Dealer's hand: {self.dealer_hand}")

        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        if player_value > 21:
            print('Dealer wins!')
        elif dealer_value > 21:
            print('Congrats, You win!')
        elif player_value > dealer_value:
            print('You win!')
        elif dealer_value > player_value:
            print('You loose!')
        else:
            print("It's a tie!")
game = Game()
game.play_game()

        