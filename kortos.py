import random

class Card:

    card_rank = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    card_suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, rank: int = 0, suit: int = 0, weight: int = 0):
        self.rank = rank
        self.suit = suit
        self.weight = weight
    
    def __repr__(self):
        card_print = f'{self.card_rank[self.rank]} of {self.card_suit[self.suit]}'
        return card_print
    
    def rank(self, card_rank):
        return card_rank
    
    def suit(self, card_suit):
        return card_suit

    def sign(self):
        if self.suit == 'Spades':
            return u"\u2660"
        if self.suit == 'Clubs':
            return u'\u2663'
        if self.suit == 'Hearts':
            return u'\u2665'
        if self.suit == 'Diamonds':
            return u'\u2666'
    
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
    

    def deck_creation(self):
        self.deck = []
        for rank in range(2, 15):
            for suit in range(4):
                self.deck.append(Card(rank, suit, rank))
        random.shuffle(self.deck)

    def shufle(self):
        random.shuffle(self.deck)


    def take_top(self):
        t_card = self.deck.pop(0)
        print(t_card)
        return t_card
    

    def take_bottom(self):
        b_card = self.deck.pop(len(self.deck)-1)
        print(b_card)
        return b_card


    def take_random(self):
        r_number = random.randint(0, 52)
        r_card = self.deck.pop(r_number)
        print(r_card)
        return r_card


    def card_weight_check_all(self):
        for card in self.deck:
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
        for card in deck.deck:
            if card.suit == suit:
                card.weight += value


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


    def draw_initial_hand(self, deck):
        for _ in range(6):
            self.hand.append(deck.take_top())


    def play_card(self):
        if not self.hand:
            print(f"{self.name} has no cards left!")
            return
        card = self.hand.pop(0)
        print(f"{self.name} played {card}")
        return card


    def add_to_hand(self, cards):
        self.hand.extend(cards)


    def __repr__(self):
        return f"Player(name={self.name}, hand={self.hand})"
           


class GameLogic():

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.deck.deck_creation()
        self.current_round = 1


    def start_game(self):
        print("Game started!")
        for player in self.players:
            player.draw_initial_hand(self.deck)


    def play_round(self):
        print(f"Round {self.current_round}")
        for player in self.players:
            print(f"Player {player.name}'s turn:")
            played_card = player.play_card()
            if self.is_valid_play(played_card):
                self.table.append(played_card)
                print(f"{player.name} played {played_card}")
                if self.check_for_capture(played_card):
                    player.add_to_hand(self.table)
                    self.table = []  
                    print(f"{player.name} captured the pile!")       
                if player.is_winner():
                    print(f"{player.name} is the winner!")
                    return
            else:
                print("Invalid play. Try again.")


class Computer1():

    def __init__(self):
        pass

deck = Deck()
deck.deck_creation()
print(deck.deck)
deck.take_top()
deck.take_bottom()
deck.take_random()
deck.card_weight_check_all()



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