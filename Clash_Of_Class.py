import random


class Character:
    Max_hp = 12


class Warrior(Character):
    name = "Gimli"
    Sword = 12
    Magic = 8
    Bow = 10

    def atk(test):
        sword_dice = random.randint(1, Warrior.Sword)
        magic_dice = random.randint(1, Warrior.Magic)
        bow_dice = random.randint(1, Warrior.Bow)
        print(str(Warrior.name) + " attack!")
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            return sword_dice
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            return bow_dice
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            return magic_dice

    def defend(test):
        hp = 12
        atk_dice = Warrior.atk(test)
        print("Hp = " + str(hp))
        defend_dice = random.randint(1, 10)
        print("attack " + str(atk_dice))
        print("defend " + str(defend_dice))
        if atk_dice > defend_dice:
            hp -= atk_dice
            print("Hp -" + str(atk_dice))
        print("Current hp = " + str(hp))
        print("##################")


class Wizard(Character):
    name = "Gandalf"
    Sword = 8
    Magic = 12
    Bow = 10

    def atk(test):
        sword_dice = random.randint(1, Wizard.Sword)
        magic_dice = random.randint(1, Wizard.Magic)
        bow_dice = random.randint(1, Wizard.Bow)
        print(str(Wizard.name) + " attack!")
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            return magic_dice
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            return bow_dice
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            return sword_dice

    def defend(test):
        hp = 12
        atk_dice = Wizard.atk(test)
        print("Hp = " + str(hp))
        defend_dice = random.randint(1, 10)
        print("attack " + str(atk_dice))
        print("defend " + str(defend_dice))
        if atk_dice > defend_dice:
            hp -= atk_dice
            print("Hp -" + str(atk_dice))
        print("Current hp = " + str(hp))
        print("##################")


class Archer(Character):
    name = "Legolas"
    Sword = 10
    Magic = 8
    Bow = 12

    def atk(test):
        sword_dice = random.randint(1, Archer.Sword)
        magic_dice = random.randint(1, Archer.Magic)
        bow_dice = random.randint(1, Archer.Bow)
        print(str(Archer.name) + " attack!")
        if bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            return bow_dice
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            return sword_dice
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            return magic_dice

    def defend(test):
        hp = 12
        atk_dice = Archer.atk(test)
        print("Hp = " + str(hp))
        defend_dice = random.randint(1, 10)
        print("attack " + str(atk_dice))
        print("defend " + str(defend_dice))
        if atk_dice > defend_dice:
            hp -= atk_dice
            print("Hp -" + str(atk_dice))
        print("Current hp = " + str(hp))
        print("##################")


# def init():
#     nb_of_player = input("How many players ? ")
#     player_class_table = {}
#     for player in range(int(nb_of_player)):
#         print(f"Player {player+1}:")
#         name_choice = input("Chose your name: ")
#         class_choice = input("chose your class between Warrior, Wizard and Archer: ").lower()
#         if class_choice == "warrior":
#             player_class_table[name_choice] = Warrior()
#         elif class_choice == "wizard":
#             player_class_table[name_choice] = Wizard()
#         elif class_choice == "archer":
#             player_class_table[name_choice] = Archer()
#     return player_class_table


# player_class_table = init()
# print(player_class_table)
test = Warrior()
Warrior.defend(test)
test = Wizard()
Wizard.defend(test)
test = Archer()
Archer.defend(test)


