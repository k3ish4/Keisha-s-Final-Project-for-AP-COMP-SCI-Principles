import random
class Enemy:
    def __init__(self, species: str, maxhp: int, atk: int):
        self.species = species 
        self.maxhp = maxhp
        self.hp = maxhp
        self.atk = atk

    def take_dmg(self, dmg: int):
        self.hp-=dmg
        print("You strike the enemy and deal " + str(dmg) + " damage. " + str(self.hp) + " hp remaining")
        
    def hit(self)-> int: 
        slime_dmg = random.uniform((0.4 * self.atk, 1.00 * self.atk))

    def enemy_revive(self):
        self.hp = self.maxhp