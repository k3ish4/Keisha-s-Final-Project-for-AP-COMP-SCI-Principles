import random
class Player:
    def __init__(self, name: str, weapon: str):
        self.name = name
        self.weapon = weapon

        self.lvl = 1
        self.shielded = False
        self.used_skill = False
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
        self.MaxEnergy = stats[3]

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


    def fight(self, attack: str) -> int:

        if attack.lower() == "normal attack":
            dmg = int(random.uniform(self.ATK * .1, self.ATK * .2))
            self.used_skill = False
            self.shielded = False
            self.Energy += 5
            return dmg

        elif attack.lower() == "skill":
            if self.used_skill:
                print('Your skill is on cooldown! Try something else.')
                return 0
            dmg = int(random.uniform(self.ATK * .2, self.ATK * .3))
            self.used_skill = True
            self.shielded = False
            self.Energy += 5
            return dmg
        
        elif attack.lower() == "shield":
            self.shielded == True
            self.used_skill = False
            self.Energy += 5
            return 0
        
        elif attack.lower() == "burst":
            if self.Energy < self.MaxEnergy:
                print("Not enough energy to use burst right now.")
                return 0
            else:
                dmg = int(random.uniform(self.ATK * .4, self.ATK * .5))
                self.used_skill = False
                self.shielded = False
                self.Energy = 0
                return dmg
        else:
            print("I'm not familliar with this fighting tactic. Please try something else.")
            return 0

    
    def hurt(self, slime_dmg: int):
        if self.shielded: 
            self.CurrentHP -= int(slime_dmg / 2)
        else:
            self.CurrentHP -= slime_dmg
        if self.CurrentHP <= 0:
            self.CurrentHP = 0
        print("The enemy hits you and deals " + str(slime_dmg) + " damage. You have " + str(self.CurrentHP) + " remaining.")

    def player_revive(self):
        self.CurrentHP = self.MAXHP
