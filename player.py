import random
class Tav:
    def __init__(self, name: str, weapon: str):
        self.name = name
        self.weapon = weapon

        self.lvl = 1
        self.MaxHP = 0
        self.CurrentHP = 0
        self.DEF = 0
        self.Energy = 0
        self.MaxEnergy = 0