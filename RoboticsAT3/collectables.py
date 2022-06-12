class DeathBringers:
    def __init__(self):
        pass

    def __str__(self):
        return "{} ({} Damage)".format(self.description, self.damage)


class Hands(DeathBringers):
    def __init__(self):
        self.description = "Bare hands"
        self.attributes = "Use what your mother gave you!"
        self.damage = 1
        self.goldValue = 0

        
class Slingshot(DeathBringers):
    def __init__(self):
        self.description = "Slingshot"
        self.attributes = "Pretend you are named David and you will do much damage"
        self.damage = 3
        self.goldValue = 5


class Sword(DeathBringers):
    def __init__(self):
        self.description = "Sword"
        self.attributes = "A beautiful sword, possibly elven made."
        self.damage = 8
        self.goldValue = 15


class Katana(DeathBringers):
    def __init__(self):
        self.description = "Japanese Katana"
        self.attributes = "What is this EXTREMELY SHARP katana doing here?"
        self.damage = 12
        self.goldValue = 30


class Wand(DeathBringers):
    def __init__(self):
        self.description = "Wizard's Wand"
        self.attributes = "A wand for using powerful spells upon thine enemy."
        self.damage = 15
        self.goldValue = 50


class UsableItems:
    def __init__(self):
        pass
    
    def __str__(self):
        return "{} (+{} Health)".format(self.description, self.healing)


class Cheese(UsableItems):
    def __init__(self):
        self.description = "Cheese your mum made you, you lucky duck!"
        self.healing = 5
        self.goldValue = 1


class Steak(UsableItems):
    def __init__(self):
        self.description = "Prime T-Bone baby!!"
        self.healing = 15
        self.goldValue = 10


class Potion(UsableItems):
    def __init__(self):
        self.description = "A red health elixir"
        self.healing = 30
        self.goldValue = 20


class MajorPotion(UsableItems):
    def __init__(self):
        self.description = "A BIG red health elixir!"
        self.healing = 60
        self.goldValue = 50


class GiganticPotion(UsableItems):
    def __init__(self):
        self.description = "An even BIGGER red health elixir!"
        self.healing = 100
        self.goldValue = 70