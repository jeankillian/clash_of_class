import random


class Character:
    max_hp = 12

    def __init__(self, name):
        self.name = name
        self.current_life_point = self.max_hp

    def clash_verification(self, hp, dice_value, defend_dice):
        print("Hp = " + str(hp))
        print("attack " + str(dice_value))
        print("defend " + str(defend_dice))
        if dice_value > defend_dice:
            hp -= dice_value
            print("Hp -" + str(dice_value))
        print("Current hp = " + str(hp))
        print("##################")


class Warrior(Character):
    chara_class = "warrior"
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
        hp = 12
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Warrior.clash_verification(self, hp, dice_value, defend_dice)


class Wizard(Character):
    chara_class = "wizard"
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
        hp = 12
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Wizard.clash_verification(self, hp, dice_value, defend_dice)


class Archer(Character):
    chara_class = "archer"
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
        hp = 12
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        Archer.clash_verification(self, hp, dice_value, defend_dice)


gimli = Warrior("Gimli")
legolas = Archer("Legolas")
gandalf = Wizard("Gandalf")

print(gimli.name + " the " + gimli.chara_class)
arm, dice_value = gimli.attack()
legolas.defend(arm, dice_value)

print(gandalf.name + " the " + gandalf.chara_class)
arm, dice_value = gandalf.attack()
gimli.defend(arm, dice_value)

print(legolas.name + " the " + legolas.chara_class)
arm, dice_value = legolas.attack()
gandalf.defend(arm, dice_value)
