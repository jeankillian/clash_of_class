from Clash_Of_Class import *

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
# Attack 2: legolas attack gandalf
print(legolas)
if legolas.current_life_point <= 0:
    print("|*DEAD*")
else:
    arm, dice_value = legolas.attack()
    gandalf.defend(arm, dice_value)
# Attack 3: gandalf attack gimli
print(gandalf)
if gandalf.current_life_point <= 0:
    print("|*DEAD*")
else:
    arm, dice_value = gandalf.attack()
    gimli.defend(arm, dice_value)

print(gimli)
a = gimli.height
b = gimli.weight
print(legolas)
c = legolas.height
d = legolas.weight
print(gandalf)
e = gandalf.height
f = gandalf.weight





