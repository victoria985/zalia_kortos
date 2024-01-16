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
        if self.suit == 'Clubs':
            return u'\u2663'
        if self.suit == 'Hearts':
            return u'\u2665'
        if self.suit == 'Diamonds':
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
    def __init__(self, deck: list = []):
        self.deck = deck

# Metodas deck_creation sukuria išmaišytą kaladę.
    def deck_creation(self):
        self.deck = []
        for rank in range(2, 15):
            for suit in range(4):
                self.deck.append(Card(rank, suit, rank))
        random.shuffle(self.deck)

# Metodas išmaišo kaladę.
    def shuffle(self):
        random.shuffle(self.deck)

# Metodas grąžina kortą paimtą nuo kaladės viršaus.
    def take_top(self):
        t_card = self.deck.pop(0)
        print(t_card)
        return t_card

# Metodas grąžina kortą paimtą iš kaladės apačios.   
    def take_bottom(self):
        b_card = self.deck.pop(len(self.deck)-1)
        print(b_card)
        return b_card

# Metodas grąžina atsitiktinę kortą iš kaladės
    def take_random(self):
        r_number = random.randint(0, 52)
        r_card = self.deck.pop(r_number)
        print(r_card)
        return r_card

# Metodo ciklas atspausdina visas kaladėje esančias kortas bei jų svorį/taškus.
    def card_weight_check_all(self):
        for card in self.deck:
            print(f'{card} - {card.weight}\n')

# Metodas patikrina ar dviejų kortų rūšis yra vienoda      
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


class GameLogic():

    def __init__(self, num_players, num_cards):
        self.num_players = num_players
        self.num_cards = num_cards
        self.players = []
        self.deck = []
        self.trump_card = None
        self.current_player = None
    
    def game_start(self):
        deck.deck_creation()
        
    # Kiekvienam žaidėjui iš 36 kortų kaladės išdalijama po 6 kortas. Galima dalyti po vieną arba iš karto po dvi kortas. 
    # Likusios kortos padedamos į kaladę. Apatinė kaladės korta atverčiama, ji bus koziris. 
    # Žaidimą „Kvailys" pradeda tas, kuris turi mažiausią kozirį arba iš viso jo neturi. Žaidžiama pagal laikrodžio rodyklę.
    # Kortą kerta didesnė tos pačios mosties (būgnas, čirvas, kryžius, pikas) korta arba koziris. 
    # Visos atmuštosios kortos dedamos į šalį. Jei žaidėjas neturi didesnės kortos arba kozirio, pasiima padėtą kortą.
    # Kai bent vienas iš žaidėjų nebeturi kortų, visi pasiima iš kortų kaladės tiek, kad kiekvienas turėtų po 6 kortas. 
    # Žaidimą pralaimi susirinkęs kortas, o laimi tas žaidėjas, kuris išleidžia visas kortas.

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
