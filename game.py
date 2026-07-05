class Esm_famil_player_name:
    def __init__(self, name_of_player):
        self.name_of_player = name_of_player
    def welcome(self):
        print(f"Welcome to game {self.name_of_player} !!")
class Esm_famil_player_info(Esm_famil_player_name):
    def __init__(self, name_of_player, list_of_players):
        Esm_famil_player_name.__init__(self, name_of_player)
        self.list_of_players = list_of_players
    def print_info(self):
        self.list_of_players.append(self.name_of_player)
class Esm_famil_objects:
    def __init__(self, number_of_objects, item, dict_of_objects : dict):
        self.number_of_objects = number_of_objects
        self.item = item
        self.list_of_objects = []
        self.dict_of_objects = dict_of_objects
        self.answer_part = str()
        self.part = {}
    def objects(self):
        self.part = {self.item : self.answer_part}
        self.dict_of_objects.update(self.part)
        self.list_of_objects.append(self.dict_of_objects)
        print(self.list_of_objects)

class Esm_famil_game(Esm_famil_objects):
    def __init__(self, number_of_objects, answer_part, dict_of_objects : dict):
        Esm_famil_objects.__init__(self, number_of_objects, item, dict_of_objects)
        self.answer_part = answer_part

    def answer(self):
        new_item = self.answer_part
        self.dict_of_objects[x] = new_item
        self.list_of_objects.append(self.dict_of_objects)

        # def check_

players = int(input("How many players want to play? "))
players_list = list()

for i in range(players):
    if players > 0:
        name = input("What is your name?: ")
        a = Esm_famil_player_info(name, players_list)
        a.welcome()
        a.print_info()
    elif players <= 0:
        print("The game can't numbered the players.")

my_dict = dict()
objects = int(input("How many objects do you want to create? "))
# if objects >= 5:
for i in range(objects):
    item = input("What is your item: ")
    a = Esm_famil_objects(objects, item, my_dict)
    a.objects()

keys_to_process = list(my_dict.keys())
for x in keys_to_process:
    answer = input(f"What is your answer for {x}: ")
    b = Esm_famil_game(objects, answer, my_dict)
    b.objects()
    b.answer()