import random


class Warrior:
    Max_hp = 20
    Sword = 12
    Magic = 8
    Bow = 10

    def atk(self):
        sword_dice = random.randint(1, Warrior.Sword)
        magic_dice = random.randint(1, Warrior.Magic)
        bow_dice = random.randint(1, Warrior.Bow)
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")


class Wizard:
    Max_hp = 20
    Sword = 8
    Magic = 12
    Bow = 10

    def atk(self):
        sword_dice = random.randint(1, Wizard.Sword)
        magic_dice = random.randint(1, Wizard.Magic)
        bow_dice = random.randint(1, Wizard.Bow)
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")


class Archer:
    Max_hp = 20
    Sword = 10
    Magic = 8
    Bow = 12

    def atk(self):
        sword_dice = random.randint(1, Archer.Sword)
        magic_dice = random.randint(1, Archer.Magic)
        bow_dice = random.randint(1, Archer.Bow)
        if bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")


def init():
    nb_of_player = input("How many players ? ")
    player_class_table = {}
    for player in range(int(nb_of_player)):
        print(f"Player {player+1}:")
        name_choice = input("Chose your name: ")
        class_choice = input("chose your class between Warrior, Wizard and Archer: ").lower()
        if class_choice == "warrior":
            player_class_table[name_choice] = Warrior()
        elif class_choice == "wizard":
            player_class_table[name_choice] = Wizard()
        elif class_choice == "archer":
            player_class_table[name_choice] = Archer()
    return player_class_table


player_class_table = init()
print(player_class_table)
