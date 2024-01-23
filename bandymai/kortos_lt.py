import random

# sukuriam kortu kalade
kortu_kurimas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'D': 12, 'K': 13, "A": 14}

# sukuriam zaidejus

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        

    def pradinės_kortos():
        pradinės_kortos = list(kortos.keys())
        random.shuffle(pradinės_kortos)
        return pradinės_kortos[:6]

    zaidejai = [Player("Žaidėjas 1"), Player("Žaidėjas 2")]

    for zaidejas in zaidejai:
        zaidejas.hand = pradinės_kortos()


class GameLogic():

    def __init__(self, players):
        self.players = players  

    def start_game(self):
        print("Zaidimas prasidejo!")
        for player in self.players:
            player.hand(self.hand)


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





    def keisti_kortas(zaidejas):
        pasirinktos_kortos = random.sample(zaidejas.hand, 3)
        print(f"{zaidejas.name} pasirinko šias korteles: ", end="")
        for korta in pasirinktos_kortos:
            print(korta, end=", ")
    

    def lyginti_kortas(zaidejas1, zaidejas2):
        korta1 = zaidejas1.played_card
        korta2 = zaidejas2.played_card

        if korta1 > korta2:
            print(f"{zaidejas1.name} laimėjo raundą!")
        elif korta1 < korta2:
            print(f"{zaidejas2.name} laimėjo raundą!")
        else:
            print("Lygiosios šiame raunde.")


    def tikrinti_laimėjimą():
      for zaidejas in zaidejai:
        if not zaidejas.hand:
            print(f"{zaidejas.name} laimėjo žaidimą!")
            return True
   