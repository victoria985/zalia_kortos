# Importuojame integruotą python modulį random, kad galėtume kviesti random modulyje esančias funkcijas.
import random

# Objektas korta.
class Card:

# Kintamasis/sąrašas, kuriame nurodyti kortų rangai/reikšmės.
    card_rank = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Kintamasis/sąrašas, kuriame nurodytos kortų rūšys.
    card_suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

# Konstruktorius/metodas __init__, jame nurodyti pradiniai kintamieji: (rank, suit, weight) ir jų atributai: (int = 0).
    def __init__(self, rank: int = 0, suit: int = 0, weight: int = 0):
        self.rank = rank
        self.suit = suit
        self.weight = weight

# Metodas __repr__ reprezentuoja (spausdina) card_print kintamąjame nurodytą tekstą ir laužtiniuose skliaustuose {} nurodytas reikšmes. 
    def __repr__(self):
        card_print = f'{self.card_rank[self.rank]} of {self.card_suit[self.suit]}'
        return card_print

# Metodas rank tiesiogiai grąžina sąrašo card_rank reikšmes.  
    def rank(self, card_rank):
        return card_rank

# Metodas suit tiesiogiai grąžina sąrašo card_suit reikšmes.   
    def suit(self, card_suit):
        return card_suit

 # Metodas sign priskiria kortų rūšim atitinkamus unicode paveikslėlius. 
    def sign(self):
        if self.suit == 'Spades':
            return u"\u2660"
        elif self.suit == 'Clubs':
            return u'\u2663'
        elif self.suit == 'Hearts':
            return u'\u2665'
        elif self.suit == 'Diamonds':
            return u'\u2666'

# Metodas naudoja for ciklą, kad priskirtume kortoms taškus.
    def weight(self, rank):

# Ciklas for sunumeruoja self.rank() turinį iteruodamas indeksą (i) ir kintamąjį (card_rank). 
# Šioje vietoje grąžintą indeksą (i) interpretuojame kaip atitinkamus kortos taškus.
        for i, card_rank in enumerate(self.rank()):
            if card_rank == rank:
                return i
        
# Objektas.
class Deck:

# Konstruktorius/metodas __init__, jame nurodyti pradiniai kintamieji.
    def __init__(self, deck=None):
        self.deck = deck if deck is not None else []

# Metodas deck_creation sukuria išmaišytą kaladę.
    def deck_creation(self, setting = 6):
        self.deck = []
        for rank in range(setting, 15):
            for suit in range(4):
                self.deck.append(Card(rank, suit, rank))
        random.shuffle(self.deck)

# Metodas išmaišo kaladę.
    def shuffle(self):
        random.shuffle(self.deck)

# Metodas grąžina kortą paimtą nuo kaladės viršaus.
    def take_top(self):
        if self.deck:
            t_card = self.deck.pop(0)
            print(t_card)
            return t_card
        else:
            print("Deck is empty.")
            return None
          
# Metodas grąžina kortą paimtą iš kaladės apačios.   
    def take_bottom(self):
        b_card = self.deck.pop(-1)
        print(b_card)
        return b_card

# Metodas grąžina atsitiktinę kortą iš kaladės
    def take_random(self):
        r_number = random.randint(0, len(self.deck)-1)
        r_card = self.deck.pop(r_number)
        print(r_card)
        return r_card

# Metodo ciklas atspausdina visas kaladėje esančias kortas bei jų svorį/taškus.
    def card_weight_check_all(self):
        for card in self.deck:
            print(f'{card} - {card.weight}\n')

# Metodas patikrina ar dviejų kortų rūšis yra vienoda      
    def card_suit_check(self, card1: Card, card2: Card):
        return card1.suit == card2.suit

    def card_weight_check(self, card1: Card, card2: Card):
        if card1.weight == card2.weight:
            return 0
        elif card1.weight > card2.weight:
            return card1
        else:
            return card2

    def card_weight_modifier(self, card: Card, value = 20): 
        for cards in self.deck:
            if cards.suit == card.suit:
                cards.weight += value

class GameLogic:

    def __init__(self, players: list = [], deck: Deck = None, table: list = [], game_hand: list = []):
        self.players = players
        self.deck = deck if deck is not None else Deck()
        self.table = table
        self.game_hand = game_hand

    def deal_cards(self):
        for player in self.players:
            if len(player.hand) < 6:
                player.draw_cards(6 - len(player.hand), self.deck)

    def power_card(self):
        card_power = self.deck.deck[-1]
        return card_power
    
    def add_card(self, card: Card):
        self.table.append(card)
        print(self.table)
        return self.table
    
    def beaten_pair(self):
        if deck.card_weight_check(self.table[0], self.table[1]) == self.table[1]:
            self.game_hand.append(self.table[0])
            self.game_hand.append(self.table[1])
            return True
        else:
            return False
    
    def discard_game_hand(self):
        self.game_hand = []
        return self.game_hand

    def stick_game_hand(self, player):
          player.hand += self.game_hand
          self.discard_game_hand
          return self.game_hand
            

class Player:
    
    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand if hand is not None else []

    def draw_cards(self, number: int, deck:Deck):
        for i in range(number):
            card = deck.take_top()
            self.hand.append(card)
        print(f'player hand: {self.hand}')
        return self.hand
    
    def play_card(self, number: int):
        play_card = self.hand.pop(number - 1)
        print(play_card)
        print(self.hand)
        return play_card

class Computer:

    def __init__(self, name, level: int = 1, hand: list = []):
        self.name = name
        self.level = level
        self.hand = hand
    
    def draw_cards(self, number: int, deck):
        for i in range(number):
            card = deck.take_top()
            self.hand.append(card)
        print(f'computer hand: {self.hand}')
        return self.hand
    
    def play_card(self, number: int):
        play_card = self.hand.pop(number)
        print(play_card)
        print(self.hand)
        return play_card


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
game = GameLogic(player_nr, deck)
ace = game.power_card()
deck.card_weight_modifier(ace)
game.deal_cards()
print(deck.deck)
print(ace)
deck.card_weight_check_all()
print(len(deck.deck))
card1 = player.play_card(1)
game.add_card(card1)
card2 = player.play_card(1)
game.add_card(card2)
game.beaten_pair()
game.stick_game_hand(player)
player.play_card(1)
game.deal_cards()
print(len(deck.deck))
print(deck.deck)

# UŽDUOTIS:
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
