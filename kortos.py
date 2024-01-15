import random
from unicards import unicard

class Card:

    suits = ["s",
             "h",
             "d",
             "c"]
    
    ranks = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]
    
    ranks_print = [None, None,"2", "3",
                    "4", "5", "6", "7",
                    "8", "9", "T",
                    "J", "Q",
                    "K", "A"]

    def __init__(self, rank, suit, weight: int = 0):
        self.rank = rank
        self.suit = suit
        self.weight = weight
        
    def __repr__(self):
        card_print = f'{self.ranks[self.rank]} of {self.suits[self.suit]}'
        return card_print
    

class Deck:

    def __init__(self):
        self.cards = []
        for rank in range(2, 15):
            for suit in range(4):
                self.cards.append(Card(rank, suit, rank))
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

    def card_weight_check_all(self):
        for card in self.cards:
            print(f'{card} - {card.weight}\n')
        
    def card_suit_check(self, card1: Card, card2: Card):
        if card1.suit == card2.suit:
            return True
        else:
            False
    
    def card_weight_check(self, card1: Card, card2: Card):
        if card1.weight == card2.weight:
            check = 0
        elif card1.weight > card2.weight:
            check = card1
        else:
            check = card2
        return check

    def card_weight_modifier(self, suit, value):
        for card in deck.cards:
            if card.suit == suit:
                card.weight += value
    
    def print_playing_card_deck(self):
        for card in deck.cards:
            print(unicard(f'{card.ranks_print[card.rank]}{card.suits[card.suit]}'))

class GameLogic():

    def __init__(self):
        pass

class Computer1():

    def __init__(self):
        pass

deck = Deck()
print(deck.cards)
deck.print_playing_card_deck()
deck.take_top()
deck.take_bottom()
deck.take_random()
deck.card_weight_check_all()



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
