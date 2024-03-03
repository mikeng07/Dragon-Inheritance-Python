import random
import entity

class Hero(entity.Entity):
    # represent hero fighter
    # Entity is a part of entity module 
    # hero class inherits from entity.Entity class
    # parent class and child class
    # reuse the attribute and methods of parent

    def sword_attack(self, dragon):
        #sword attact to enemy
        dmg = random.randint(1,6) + random.randint(1,6)
        dragon.take_damage(dmg)
        # take damage on dragon object
        return self.name + " slashes the " + dragon.name + " with their sword for " + str(dmg) + " damage!"

    def arrow_attack(self, dragon):
        dmg = random.randint(1,12) 
        dragon.take_damage(dmg)
        # take damage on dragon object
        return self.name + " hits the " + dragon.name + " with an arrow for " + str(dmg) + " damage!"

