import random
class Player:
    def __init__(self, name: str, weapon: str):
        self.name = name
        self.weapon = weapon

        self.lvl = 1
        self.shielded = False
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

    def print_stats(self):
        print('Name: ' + self.name)
        print('Weapon: ' + self.weapon)
        print('ATK: ' + str(self.ATK))
        print('Max HP: ' + str(self.MAXHP))
        print('Current HP: ' + str(self.CurrentHP))
        print('Defense: ' + str(self.DEF))
        print('Energy : ' + str(self.Energy))
        print('Max Energy: ' + str(self.MaxEnergy))


    def fight(self, attack: str)->str:
        if attack.lower == "normal attack":
            dmg = int(random.uniform(self.ATK * .1, self.ATK * .2))
            used_skill = False
            shielded - False

        elif attack.lower == "skill":
            if used_skill:
                print('Your skill is on cooldown! Try something else.')
            dmg = int(random.uniform(self.ATK * .2, self.ATK * .3))
            used_skill = True
            shielded = False
        
        elif attack.lower == "shield":
            self.shielded == True
            slime_dmg -= int(random.uniform(self.DEF * 0.07, self.DEF * 0.1))
            used_skill = False
            shielded = False
        
        elif attack.lower == "burst":
            if self.Energy < self.MAXEnergy:
                print("Not enough energy to use burst right now.")
            else:
                dmg = int(random.uniform(self.ATK * .4, self.ATK * .5))
            used_skill = False
            shielded = False
    

    
    def hurt(self, slime_dmg: int):
        self.CurrentHP -= slime_dmg
        print("The enemy hits you and deals " + str(slime_dmg) + " damage. You have " + str(self.CurrentHP) + " remaining.")

    def player_revive(self):
        self.CurrentHP = self.MAXHP
