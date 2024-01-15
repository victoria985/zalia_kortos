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
    
    def get_sign(self):
        if self.suit == 'Spades':
            return u"\u2660"
        elif self.suit == 'Clubs':
            return u'\u2663'
        elif self.suit == 'Hearts':
            return u'\u2665'
        elif self.suit == 'Diamonds':
            return u'\u2666'

class Deck:

    def __init__(self, deck=None):
        self.deck = deck if deck is not None else []

    def deck_creation(self, setting = 6):
        self.deck = []
        for rank in range(setting, 15):
            for suit in range(4):
                self.deck.append(Card(rank, suit, rank))
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def take_top(self):
        if self.deck:
            t_card = self.deck.pop(0)
            print(t_card)
            return t_card
        else:
            print("Deck is empty.")
            return None
    
    def take_bottom(self):
        b_card = self.deck.pop(-1)
        print(b_card)
        return b_card

    def take_random(self):
        r_number = random.randint(0, len(self.deck)-1)
        r_card = self.deck.pop(r_number)
        print(r_card)
        return r_card

    def card_weight_check_all(self):
        for card in self.deck:
            print(f'{card} - {card.weight}\n')
        
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

    def __init__(self, players: list = [], deck: Deck = None):
        self.players = players
        self.deck = deck if deck is not None else Deck()

    def deal_cards(self):
        for player in self.players:
            if len(player.hand) < 6:
                player.draw_cards(6 - len(player.hand), self.deck)

    def power_card(self):
        card_power = self.deck.deck[-1]
        return card_power
    
    def add_card(self, card: Card, table: list = []):
        table.append(card)
            

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


player = Player('Bob')
aran = Computer('Aran')
player_nr = []
player_nr.append(player)
player_nr.append(aran)
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
player.play_card(1)
player.play_card(1)
player.play_card(1)
game.deal_cards()
print(len(deck.deck))
print(deck.deck)
