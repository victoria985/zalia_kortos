import random

class Card:

    def __init__(self, suit: str = '', weight: int = 0, color: str = '', rank: str = ''):
        self.suit = suit
        self.weight = weight(rank)
        self.color = color
        self.rank = rank

    def rank(self):
        card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        return card_rank

    def suit(self):
        card_suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        return card_suit

    def sign(self):
        if self.suit == 'Spades':
            return '\U+2660'
        if self.suit == 'Clubs':
            return 'U+2663'
        if self.suit == 'Hearts':
            return 'U+2665'
        if self.suit == 'Diamonds':
            return 'U+2666'
    
    def weight(self, rank):
        for i, card_rank in enumerate(self.rank(), start=1):
            if card_rank == rank:
                return i
        

    
    def update_suit(self, spades=False, clubs=False, hearts=False, diamonds=False):
        if spades:
            self.suit = 'Spades'
        elif clubs:
            self.suit = 'Clubs'
        elif hearts:
            self.suit = 'Hearts'
        elif diamonds:
            self.suit = 'Diamonds'
        return self.suit
    
    def weight(self):
        ranks_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'D', 'T'] 
        return ranks_values
    

        
    

class Deck:

    def __init__(self, deck: list = []):
        self.deck = deck

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



    def forkinimas(self):
      pass


# Kortų kaladė
# Korta: Objektas (Class)
# def __init__
# def rank (2-9, T, J, Q, K, A)
# def suit (spades, clubs, hearts, diamonds)
# def sign (suit + rank)
# def weight
# Kortų kaladė: Objektas (Class)
# def deck - kortų sąrašas []
# def shuffle
# def take from top
# def take from bottom
# def take random
# Mąstom apie žaidimą