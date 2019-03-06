import random
print("|############################>")
print("| Welcome to Clash Of Class!")
print("|############################>")


class Character:
    max_hp = 12

    def __init__(self, name):
        self.name = name
        self.current_life_point = self.max_hp
        self._height = random.randint(170, 190)
        self._weight = random.randint(70, 90)
        self.new_height = self._height / 2
        self.new_weight = self._weight / 2

    def __repr__(self):
        return "|{} the {}".format(self.name, self.__class__.__name__)

    def _get_height(self):
        print("|height = {}".format(self._height))
        return self._height

    def _set_height(self, new_height):
        print("|new height = {}".format(new_height))
        self._height = new_height

    def _get_weight(self):
        print("|weight = {}".format(self._weight))
        return self._weight

    def _set_weight(self, new_weight):
        print("|weight = {}".format(new_weight))
        self._weight = new_weight

    height = property(_get_height, _set_height)
    weight = property(_get_weight, _set_weight)

    def _attack_gen(self):
        if self.current_life_point <= 0:
            print("|can't attack while Dead")
            print("|############################>")
        else:
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

    def defend(self, arm, dice_value):
        if self.current_life_point <= 0:
            print("|" + self.name + " is already Dead")
            print("|############################>")
        else:
            if arm == "sword":
                defend_dice = random.randint(1, self.sword)
            elif arm == "magic":
                defend_dice = random.randint(1, self.magic)
            else:
                defend_dice = random.randint(1, self.bow)
            self.current_life_point = self.clash_verification(self.current_life_point, dice_value, defend_dice, arm)

    def clash_verification(self, hp, dice_value, defend_dice, arm):
        print("|{} the {}".format(self.name, self.__class__.__name__))
        print("|" + self.name + " Current HP = " + str(hp))
        print("|attacker " + str(dice_value))
        print("|defender " + str(defend_dice))
        if dice_value > defend_dice:
            hp -= dice_value - defend_dice
            print("|Dealed " + str(dice_value - defend_dice) + " " + arm + " damage")
        else:
            print("|defense success")
        if hp <= 0:
            print("|" + self.name + " is Dead")
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
        arm, dice_value = self._attack_gen()
        if arm == "magic":
            dice_value += self.weight // 30
        elif arm == "bow":
            dice_value += (self.height - 170) % 3
        return arm, dice_value


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
        arm, dice_value = self._attack_gen()
        if arm == "sword":
            dice_value += (self.weight + self.height) // 40
        elif arm == "bow":
            dice_value += (self.height - 170) % 3
        return arm, dice_value


class Archer(Character):
    sword = 10
    magic = 8
    bow = 12

    def attack(self):
        self.sword_dice = random.randint(1, self.sword)
        self.magic_dice = random.randint(1, self.magic)
        self.bow_dice = random.randint(1, self.bow)
        arm, dice_value = self._attack_gen()
        if arm == "sword":
            dice_value += (self.height // 40) + 1
        elif arm == "magic":
            dice_value += (self.weight // 20) + 1
        return arm, dice_value


gimli = Warrior("Gimli")
legolas = Archer("Legolas")
gandalf = Wizard("Gandalf")

# Attack 1: gimli attack legolas
print(gimli)
if gimli.current_life_point <= 0:
    print("|*DEAD*")
else:
    arm, dice_value = gimli.attack()
    legolas.defend(arm, dice_value)
# # Attack 2: legolas attack gandalf
# print(legolas)
# if legolas.current_life_point <= 0:
#     print("|*DEAD*")
# else:
#     arm, dice_value = legolas.attack()
#     gandalf.defend(arm, dice_value)
# # Attack 3: gandalf attack gimli
# print(gandalf)
# if gandalf.current_life_point <= 0:
#     print("|*DEAD*")
# else:
#     arm, dice_value = gandalf.attack()
#     gimli.defend(arm, dice_value)

print(gimli)
a = gimli.height
b = gimli.weight
print(legolas)
c = legolas.height
d = legolas.weight
print(gandalf)
e = gandalf.height
f = gandalf.weight

