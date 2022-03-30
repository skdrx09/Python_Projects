from dataclasses import asdict
import random
import math

class Warrior:
    def __init__(self, name="Warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        attk_dmg = self.attk_max * (random.random() + .5)
        return attk_dmg
    
    def block(self):
        block_dmg = self.block_max * (random.random() + .5)
        return block_dmg

class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                break
    def get_attack_result(self, warriorA, warriorB):
        warrior_a_attack_dmg = warriorA.attack()
        warrior_b_block_dmg = warriorB.block()
        damage_to_warrior_b = math.ceil(warrior_a_attack_dmg - warrior_b_block_dmg)
        if damage_to_warrior_b <= 0:
            damage_to_warrior_b = 0
        warriorB.health -= damage_to_warrior_b
        print("{} attacks {} for {} points of damage".format(warriorA.name, warriorB.name, damage_to_warrior_b))
        print("{} is down to {} HP".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is victorious!".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    thor = Warrior("Thor", 50, 20, 10)
    loki = Warrior("Loki", 50, 12, 15)
    battle = Battle()
    battle.start_fight(thor, loki)

main()