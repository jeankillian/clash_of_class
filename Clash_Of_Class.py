import random
print("|############################>")
print("| Welcome to Clash Of Class!")
print("|############################>")


class Character:
    sword_dice = 0
    magic_dice = 0
    bow_dice = 0
    max_hp = 12

    def __init__(self, name):
        self.name = name
        self.current_life_point = self.max_hp

    def __str__(self):
        return "|{} the {}".format(self.name, self.__class__.__name__)

    def attack_gen(self):
        if self.sword_dice >= self.magic_dice and self.sword_dice >= self.bow_dice:
            print("|attack with sword")
            arm = "sword"
            return arm, self.sword_dice
        elif self.bow_dice >= self.sword_dice and self.bow_dice >= self.magic_dice:
            print("|attack with bow")
            arm = "bow"
            return arm, self.bow_dice
        elif self.magic_dice >= self.sword_dice and self.magic_dice >= self.bow_dice:
            print("|attack with magic")
            arm = "magic"
            return arm, self.magic_dice

    def clash_verification(self, hp, dice_value, defend_dice, arm):
        print("|{} the {}".format(self.name, self.__class__.__name__))
        print("|" + self.name + " Current HP = " + str(hp))
        print("|attacker " + str(dice_value))
        print("|defender " + str(defend_dice))
        if dice_value > defend_dice:
            hp -= dice_value
            print("|Deals " + str(dice_value) + " " + arm + " damage")
        else:
            print("|defense success")
        if hp <= 0:
            print("|Dead")
        else:
            print("|" + self.name + " HP = " + str(hp))
        print("|############################>")
        return hp


class Warrior(Character):
    max_hp = 16
    sword = 12
    magic = 8
    bow = 10

    def attack(self):
        self.sword_dice = random.randint(1, self.sword)
        self.magic_dice = random.randint(1, self.magic)
        self.bow_dice = random.randint(1, self.bow)
        return self.attack_gen()

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        self.current_life_point = self.clash_verification(self.current_life_point, dice_value, defend_dice, arm)


class Wizard(Character):
    sword = 8
    magic = 12
    bow = 10

    def attack(self):
        self.sword_dice = random.randint(1, self.sword)
        magic_dice1 = random.randint(1, self.magic)
        magic_dice2 = random.randint(1, self.magic)
        self.magic_dice = max(magic_dice1, magic_dice2)
        self.bow_dice = random.randint(1, self.bow)
        return self.attack_gen()

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        self.current_life_point = self.clash_verification(self.current_life_point, dice_value, defend_dice, arm)


class Archer(Character):
    sword = 10
    magic = 8
    bow = 12

    def attack(self):
        self.sword_dice = random.randint(1, self.sword)
        self.magic_dice = random.randint(1, self.magic)
        self.bow_dice = random.randint(1, self.bow)
        arm, dice_value = self.attack_gen()
        if arm == "sword" or arm == "magic":
            dice_value += 1
        return arm, dice_value

    def defend(self, arm, dice_value):
        if arm == "sword":
            defend_dice = random.randint(1, self.sword)
        elif arm == "magic":
            defend_dice = random.randint(1, self.magic)
        else:
            defend_dice = random.randint(1, self.bow)
        self.current_life_point = self.clash_verification(self.current_life_point, dice_value, defend_dice, arm)


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
