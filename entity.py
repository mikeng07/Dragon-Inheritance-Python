class Entity:
    """Represents an Entity to fight.
    Attributes: 
    name (str) - name of the entity.
    max_hp (int) - starting hp of entity.
    hp (int) - hit points of entity. """

    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        # '_' indicate private variable

    @property
    # use decorator to define a property
    # cleaner interface, for simple attribute access
    # allow method to be accessed like attribute
    # self refer to instance of the class
    def name(self):
       # access name of entity
        return self._name
    
    @property
    # access hp of entity
    def hp(self):
        return self._hp

    def take_damage(self, dmg):
        self._hp -= dmg
        self._hp = 0 if self._hp < 0 else self._hp 

    def __str__(self):
    # represent entity
        return self.name + ": " + str(self._hp) + "/" + str(self._max_hp)