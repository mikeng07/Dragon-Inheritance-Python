import random
import dragon

class FlyingDragon(dragon.Dragon):
    """Represents a flying dragon fighter.
  Attributes:
    swoops (int) - number of fire shots a dragon can do.
  """

    def __init__(self,name,max_hp):
        # initialize fire draon's name, hp and fire_shots
        # self: a reference to current instance of the class
        super().__init__(name,max_hp)
        # call constructor of superclass (parent class) to initilize
        # the inherited attributes
        # super return a proxy object that delegates method calls to a parent 
        self._swoops = 5 

    def special_attack(self,hero):
        if self._swoops > 0:
            dmg = random.randint(5, 8)
        else:
            return self.name + " tries to swoop down to hit you, but failed."

        hero.take_damage(dmg)
        self._swoops -= 1
        return self. name + " swoops at you for " + str(dmg) + " damage!"

    def __str__(self):
        # string representation
        # represent of a fyling dragon 
        return super().__str__() + "\n Swoops attacks remaining: " + str(self._swoops)
        # call __str__ from parent class
        # append the additional information about the fire dragon 