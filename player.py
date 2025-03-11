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
    
    def assign_stats(self):
        stats = [30, 25, 35, 22]
        random.shuffle(stats)
        self.ATK = stats[0]
        self.MAXHP = stats[1]
        self.DEF = stats[2]
        self.MAXEnergy = stats[3]
        self.CurrentHP = self.MAXHP      

    def fight(self, attack: str)->str:
        attack = input()
        if attack.lower == "normal attack":
            dmg = int(random.uniform(self.ATK * .1, self.ATK * .2))
        elif attack.lower == "skill":
            dmg = int(random.uniform)