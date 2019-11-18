from .bcolors import *


class Wand:
    def __init__(self, name, level, elements, attacks):
        self.unlocked_when = [1, 1, 8, 15]
        self.level = level
        self.name = name
        self.hp = level * 700
        self.maxhp = level * 700
        self.elements = elements
        self.attacks = attacks
        if 0 <= self.level < 8:
            self.unlocked = [True, True, False, False]
        elif 8 <= self.level < 15:
            self.unlocked = [True, True, True, False]
        elif self.level >= 15:
            self.unlocked = [True, True, True, True]

    def choose_attack(self):
        for item in self.attacks:
            if self.unlocked[self.attacks.index(item)]:
                print(bcolors.OKBLUE + str(self.attacks.index(
                    item) + 1) + ". " + item.element + "    " + bcolors.OKGREEN + item.name + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "Unlocked At Level " + str(
                    self.unlocked_when[self.attacks.index(item)]) + bcolors.ENDC)
        successful = False
        while not successful:
            try:
                attack_index = int(input("Enter The Input Number: ")) - 1
                dmg = self.attacks[attack_index].generate_damage()
                successful = True
                return dmg
            except IndexError:
                print(bcolors.FAIL + "There is no attack with that number" + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "Please enter a " + bcolors.UNDERLINE + bcolors.BOLD + "NUMBER" + bcolors.ENDC)

    def take_damage(self, dmg):
        self.hp -= dmg

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "
        return hp_bar