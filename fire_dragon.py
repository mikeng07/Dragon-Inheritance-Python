import random
import dragon

class FireDragon(dragon.Dragon):
    """Represents a fire dragon fighter.
  Attributes:
    fire_shots (int) - number of fire shots a dragon can do.
  """

    def __init__(self,name,max_hp):
        # initialize fire draon's name, hp and fire_shots
        # self: a reference to current instance of the class
        super().__init__(name,max_hp)
        # call constructor of superclass (parent class) to initilize
        # the inherited attributes
        # super return a proxy object that delegates method calls to a parent 
        self._fire_shots = 3 

    def special_attack(self,hero):
        if self._fire_shots > 0:
            dmg = random.randint(5, 9)
        else:
            return self.name + " tries to spit fire at you but is all out of fire shots."

        hero.take_damage(dmg)
        self._fire_shots -= 1
        return self. name + " engulfs you in flames for " + str(dmg) + " damage!"

    def __str__(self):
        # string representation
        # represent of a fire dragon 
        return super().__str__() + "\n Fire shots remaining: " + str(self._fire_shots)
        # call __str__ from parent class
        # append the additional information about the fire dragon 