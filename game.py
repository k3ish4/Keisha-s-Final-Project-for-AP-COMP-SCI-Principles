import time
import random
from player import Player
from enemy import Enemy

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('Hello Traveler!')

    print_dramatic_text("Today you start your journey to become a fierce warrior!")
    name = input("What is your name, traveller?\n")
    weapons = ['claymore', 'bow', 'sword', 'polearm', 'catalyst']
    print(weapons)
    weapon = input("Which weapon do you wish to yeild? ")
    while weapon.lower() not in weapons:
        weapon = input("That weapon does not yet exist in this world. What weapon do you weild? ")

    player = Player(name, weapon)
    player.assign_stats()
    view_stats = input(("If you wish to see your current stats, type 'stats'. "))
    if view_stats.lower() == 'stats':
        print("")
        player.print_stats()
        print("") 

    print("Here comes your first enemy! I'll explain how combat works.")
    print("Type 'normal attack', 'skill', 'shield', or 'burst' to perform the corresponding action.")
    print("Your skill does more damage than your normal attack, but it cannot be used back to back.")
    print("Your shield does not do damage, but it absorbs a portion of the damage that your enemy deals to you in this turn.")
    print("After each normal attack, skill, or shield, you gain 5 Energy. You may only perform your burst when your Energy is equal to or greater than your MAXEnergy stat. Performing your burst will reset your Energy back to 0.")
    print("Your burst does even more damage than your skill.")
    print("")
    print("Good luck on your first battle!")
    print("")
    monster = Enemy("slime", 35, 5)

    while monster.hp > 0:
        print("\nType in any of the aforementioned actions to make a move.")
        attack = input()
        if player.CurrentHP > 0:
            dmg = player.fight(attack)
            monster.take_dmg(dmg)
            slime_dmg = monster.hit()
            player.hurt(slime_dmg)
        else:
            print("You've been defeated! Let's try this again.")
            player.player_revive()
            monster.enemy_revive()

    print("\nCongratulations " + player.name + ". Lift your " + player.weapon + " to the sky in victory! You've completed the battle!")

