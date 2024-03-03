import random
import entity

class Dragon(entity.Entity):
    # represent a dragon fighter
    def basic_attack(self, hero):
        dmg = random.randint(3,7) 
        hero.take_damage(dmg)
        # take damage on dragon object
        return self.name + " smashes you with its tail for " + str(dmg) + " damage!"

    def special_attack(self, hero):
        dmg = random.randint(4,8) 
        hero.take_damage(dmg)
        # take damage on dragon object
        return self.name + " slashes you with its claws for " + str(dmg) + " damage!"

