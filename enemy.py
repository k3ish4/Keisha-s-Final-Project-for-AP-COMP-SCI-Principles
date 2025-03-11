class Enemy:
    def __init__(self, name: str, hp: int, atk: int):
        self.hp = hp
        self.atk = atk

    def take_dmg(self, dmg: int):
        self.hp-=dmg
    