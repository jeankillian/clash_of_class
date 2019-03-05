import Clash_Of_Class as Clash
import random

luffy = Clash.Warrior("Luffy")
zorro = Clash.Warrior("Zorro")
zero = Clash.Wizard("Zero")
diablo = Clash.Wizard("Diablo")
sogeking = Clash.Archer("Sogeking")
kaito = Clash.Archer("Kaito")
anime_chara = [luffy, zorro, zero, diablo, sogeking, kaito]
random_anime_chara = random.sample(anime_chara, 6)

genji = Clash.Warrior("Genji")
reinhardt = Clash.Warrior("Reinhardt")
ahri = Clash.Wizard("Ahri")
jaina = Clash.Wizard("Jaina")
sylvanas = Clash.Archer("Sylvanas")
xayah = Clash.Archer("Xayah")
game_chara = [genji, reinhardt, ahri, jaina, sylvanas, xayah]
random_game_chara = random.sample(game_chara, 6)

while len(random_anime_chara) != 0 or len(random_game_chara) != 0:
    for anime_chara, game_chara in zip(random_anime_chara, random_game_chara):
        print(anime_chara)
        arm, dice_value = anime_chara.attack()
        game_chara.defend(arm, dice_value)
        if game_chara.current_life_point <= 0:
            random_game_chara.remove(game_chara)
            print(random_game_chara)
            print("------------------------------------->")

    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||>")
    for anime_chara, game_chara in zip(random_anime_chara, random_game_chara):
        print(game_chara)
        arm, dice_value = game_chara.attack()
        anime_chara.defend(arm, dice_value)
        if anime_chara.current_life_point <= 0:
            random_anime_chara.remove(game_chara)
            print(random_anime_chara)
            print("------------------------------------->")
