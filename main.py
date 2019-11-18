from Classes.Wand import *
from Classes.Attack import *
import random


attacker = -1
icy_cage = Attack("Ice", 560, "Icy Cage")
ice_fist = Attack("Ice", 1000, "Ice Fist")
stun = Attack("Magic", 300, "Stun")
punch = Attack("Magic", 300, "Punch")
volcano = Attack("Flame", 1200, "Volcano")
ice_wand = Wand("Ice Wand", 15, ["Ice"], [stun, icy_cage, punch, ice_fist])
fire_wand = Wand("Fire Wand", 15, ["Flame"], [stun, volcano, punch, volcano])
attack_power = 0

while not ice_wand.hp <= 0 or not fire_wand.hp <= 0:
    if ice_wand.hp <= 0 or fire_wand.hp <= 0:
        break
    if attacker == -1:
        attack_power = ice_wand.choose_attack()
        fire_wand.take_damage(attack_power)
        print("You dealt " + str(attack_power) + " points of damage. Enemy HP is:  " + fire_wand.get_stats())
    elif attacker == 1:
        atk_num = random.randrange(0, 4)
        attack_power = fire_wand.attacks[atk_num].generate_damage()
        ice_wand.take_damage(attack_power)
        print("Enemy deals " + str(attack_power) + " points of damage. Your HP is: " + ice_wand.get_stats())
    attacker *= -1

    if ice_wand.hp <= 0:
        print(bcolors.FAIL + "You lost..." + bcolors.ENDC)
        break
    elif fire_wand.hp <= 0:
        print(bcolors.OKGREEN + "You won!!!" + bcolors.ENDC)
        break