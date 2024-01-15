import random

class Card:

    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    
    ranks = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, rank, suit, weight: int = 0):
        self.rank = rank
        self.suit = suit
        self.weight = weight
        
    def __repr__(self):
        v = self.ranks[self.rank] + " of " + self.suits[self.suit]
        return v


class Deck:

    def __init__(self):
        self.cards = []
        for rank in range(2, 15):
            for suit in range(4):
                self.cards.append(Card(rank,suit))
        random.shuffle(self.cards)
    
    def take_top(self):
        t_card = self.cards.pop(0)
        print(t_card)
        return t_card
    
    def take_bottom(self):
        b_card = self.cards.pop(len(self.cards)-1)
        print(b_card)
        return b_card

    def take_random(self):
        r_number = random.randint(0, 52)
        r_card = self.cards.pop(r_number)
        print(r_card)
        return r_card

class GameLogic():

    def __init__(self):
        pass

class Computer1():

    def __init__(self):
        pass

deck = Deck()
print(deck.cards)
deck.take_top()
deck.take_bottom()
deck.take_random()



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
