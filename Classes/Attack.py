import random


class Attack:
    def __init__(self, element, atk_pow, name):
        self.name = name
        self.element = element
        self.atk = atk_pow

    def generate_damage(self):
        return random.randrange(self.atk - 25, self.atk + 25)