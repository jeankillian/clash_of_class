import random


class Character:

    def __init__(self, name):
        self.name = name
        self.current_life_point = self.max_hp

    def __str__(self):
        return "{} the {}.".format(self.name, self.__class__.__name__)

    def clash_verification(self, hp, dice_value, defend_dice):
        print("Hp = " + str(hp))
        print("attack " + str(dice_value))
        print("defend " + str(defend_dice))
        if dice_value > defend_dice:
            hp -= dice_value
            print("Hp -" + str(dice_value))
        print("Current hp = " + str(hp))
        print("##################")
        return hp


class Warrior(Character):
    chara_class = "warrior"
    max_hp = 16
    current_life_point = max_hp
    sword = 12
    magic = 8
    bow = 10

    def attack(self):
        sword_dice = random.randint(1, self.sword)
        magic_dice = random.randint(1, self.magic)
        bow_dice = random.randint(1, self.bow)
        if sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            arm = "sword"
            return arm, sword_dice
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            arm = "bow"
            return arm, bow_dice
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            arm = "magic"
            return arm, magic_dice

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Warrior.current_life_point = Warrior.clash_verification(self, self.current_life_point, dice_value, defend_dice)


class Wizard(Character):
    chara_class = "wizard"
    max_hp = 12
    current_life_point = max_hp
    sword = 8
    magic = 12
    bow = 10

    def attack(self):
        sword_dice = random.randint(1, self.sword)
        magic_dice = random.randint(1, self.magic)
        bow_dice = random.randint(1, self.bow)
        if magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            arm = "magic"
            return arm, magic_dice
        elif bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            arm = "bow"
            return arm, bow_dice
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            arm = "sword"
            return arm, sword_dice

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Wizard.current_life_point = Wizard.clash_verification(self, self.current_life_point, dice_value, defend_dice)


class Archer(Character):
    chara_class = "archer"
    max_hp = 12
    current_life_point = max_hp
    sword = 10
    magic = 8
    bow = 12

    def attack(self):
        sword_dice = random.randint(1, self.sword)
        magic_dice = random.randint(1, self.magic)
        bow_dice = random.randint(1, self.bow)
        if bow_dice >= sword_dice and bow_dice >= magic_dice:
            print("attack with bow")
            arm = "bow"
            return arm, bow_dice
        elif sword_dice >= magic_dice and sword_dice >= bow_dice:
            print("attack with sword")
            arm = "sword"
            return arm, sword_dice
        elif magic_dice >= sword_dice and magic_dice >= bow_dice:
            print("attack with magic")
            arm = "magic"
            return arm, magic_dice

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Archer.current_life_point = Archer.clash_verification(self, self.current_life_point, dice_value, defend_dice)


gimli = Warrior("Gimli")
legolas = Archer("Legolas")
gandalf = Wizard("Gandalf")

# Attack 1: gimli attack legolas
print(gimli)
arm, dice_value = gimli.attack()
legolas.defend(arm, dice_value)

# Attack 2: gandalf attack gimli
print(gandalf)
arm, dice_value = gandalf.attack()
gimli.defend(arm, dice_value)

# Attack 3: legolas attack gandalf
print(legolas)
arm, dice_value = legolas.attack()
gandalf.defend(arm, dice_value)

