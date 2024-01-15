import random

class Card:

    def __init__(self, suit: str = '', weight: int = 0,):
        self.suit = suit
        self.weight = weight

class Deck:

    def __inir__(self, contents: list = []):
        self.contents = contents
    
    def __str__(self):
        return f'{self.contents}'
    def deck_creation(self, card: Card, settings: int = 0):
        
        # 52/4 = 13
        weight_settings = settings/4
        suits = ['Spades', 'Clubs', 'Diamonds', 'Clubs']
        for c in suits:
            card.suit = c
            for w in range(1, weight_settings):
                card.weight = w
            self.contents.append(card)

    def shufle(self):
        random.shuffle(self.deck)

    def take_top(self):
        pass
    
    def take_bottom(self):
        pass

    def take_random(self):
        r_card = random.randint(1, 52)
        pass

class GameLogic():

    def __init__(self):
        pass

class Computer1():

    def __init__(self):
        pass

deck = Deck()
deck.deck_creation
print(deck)
print(deck.contents)


def forkinimas(self):
      pass


# Kortų kaladė
# Korta: Objektas (Class)
# def rank (2-9, T, J, Q, K, A)
# def suit (spades, clubs, hearts, diamonds)
# def sign (suit + rank)
# def weight
# Kortų kaladė: Objektas (Class)
# def cards - kortų sąrašas []
# def shuffle
# def take from top
# def take from bottom
# def take random
# Mąstom apie žaidimą
