
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
        elif self.suit == 'Clubs':
            return u'\u2663'
        elif self.suit == 'Hearts':
            return u'\u2665'
        elif self.suit == 'Diamonds':
            return u'\u2666'

    def weight(self, rank):

        for i, card_rank in enumerate(self.rank()):
            if card_rank == rank:
                return i

class Deck():
    
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
            print("Kaladė tuščia.")
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
        if Deck.card_weight_check(self.table[0], self.table[1]) == self.table[1]:
            self.game_hand.append(self.table[0])
            self.game_hand.append(self.table[1])
            return True
        else:
            return False
        
    def attack(self, attacker):
        print(f"{attacker.name} puola.")
        
        table_value = None
        if self.table:
            table_value = self.table[0].weight

        while True:
            print(f"Stalas: {self.table}")
            print("Ar norite pulti?")
            attack_choice = input().lower()
            
            if attack_choice == 'ne':
                break

            attack_card = attacker.play_card(1)
            self.add_card(attack_card)

            for player in self.players:
                if player != attacker and player.hand:
                    print(f"{player.name}, ar norite primesti kortų?")
                    contribute_choice = input().lower()
                    if contribute_choice == 'taip':
                        contribute_card = player.play_card(1)
                        if contribute_card.weight == table_value:
                            self.add_card(contribute_card)
                        else:
                            print(f"{player.name} negali primesti kortų.")
            print("Puolimo pabaiga.")

    def defend(self, defender):
        print(f"{defender.name} ginasi.")

        table_value = self.table[0].weight

        while self.table:
            print(f"Stalas: {self.table}")
            print("Ar norite gintis?")
            defend_choice = input().lower()

            if defend_choice == 'ne':
                break

            defend_card = defender.play_card(1)

            if defend_card.suit == self.table[0].suit and defend_card.weight > table_value:
                print("Žaidėjas sėkmingai apsigynė.")
                self.discard_game_hand()
            elif defend_card.suit == self.uber_suit:
                print("Žaidėjas sėkmingai apsigynė su kozeriu.")
                self.discard_game_hand()
            else:
                print("Žaidėjas neapsigynė.")
                self.stick_game_hand(defender)

    def cleanup_turn(self):

        if self.deck.deck and all(len(player.hand) >= 6 for player in self.players):
            print("Tęsiamas ėjimas.")
            self.start_turn()
        else:
            self.end_turn()

    def start_turn(self):

        self.deal_cards()

    def end_turn(self):

        print("Ėjimo pabaiga.")

    def end_game(self):
        print("Žaidimo pabaiga!")
        winner = min(self.players, key=lambda player: len(player.hand))
        print(f"{winner.name} laimėjo!")
    
    def discard_game_hand(self):
        self.game_hand = []
        return self.game_hand

    def stick_game_hand(self, player):
        player.hand += self.game_hand
        self.discard_game_hand
        return self.game_hand
    
    def get_number_of_players(self, num_players):
        self.num_players = num_players
        while True:
            num_players = int(input("Įveskite žaidėjų skaičių: "))
            if num_players >= 2 and num_players <= 6:
                return num_players
            else:
                print("Įveskite skaičių nuo 2 iki 6.")
                        

class Player:
    
    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand if hand is not None else []

    def draw_cards(self, number: int, deck:Deck):
        for i in range(number):
            card = deck.take_top()
            self.hand.append(card)
        print(f'Žaidėjo kortos: {self.hand}')
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
        print(f'Kompiuterio kortos: {self.hand}')
        return self.hand
    
    def play_card(self, number: int):
        play_card = self.hand.pop(number)
        print(play_card)
        print(self.hand)
        return play_card


while True:


# player = Player('Bob')
# aran = Computer('Aran')
# player_nr = []
# player_nr.append(player)
# player_nr.append(aran)
# deck = Deck()
# deck.deck_creation()
# game = GameLogic(player_nr, deck)
# ace = game.power_card()
# deck.card_weight_modifier(ace)
# game.deal_cards()
# print(deck.deck)
# print(ace)
# deck.card_weight_check_all()
# print(len(deck.deck))
# card1 = player.play_card(1)
# game.add_card(card1)
# card2 = player.play_card(1)
# game.add_card(card2)
# game.beaten_pair()
# game.stick_game_hand(player)
# player.play_card(1)
# game.deal_cards()
# print(len(deck.deck))
# print(deck.deck)


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
