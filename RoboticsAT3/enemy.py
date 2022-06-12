class Enemy:
    def __init__(self):
        pass

    def __str__(self):
        return self.description

    def alive(self):
        return self.health > 0


class Rat(Enemy):
    def __init__(self):
        self.description = "Rat"
        self.health = 10
        self.damage = 1


class Goblin(Enemy):
    def __init__(self):
        self.description = "Goblin"
        self.health = 20
        self.damage = 4


class Rogue(Enemy):
    def __init__(self):
        self.description = "Rogue"
        self.health = 40
        self.damage = 6


class DarkElf(Enemy):
    def __init__(self):
        self.description = "Dark Elf"
        self.health = 60
        self.damage = 8


class Wizard(Enemy):
    def __init__(self):
        self.description = "Wizard"
        self.health = 80
        self.damage = 10


class Demon(Enemy):
    def __init__(self):
        self.description = "Demon"
        self.health = 100
        self.damage = 12


class GoblinKing(Enemy):
    def __init__(self):
        self.description = "Goblin King"
        self.health = 150
        self.damage = 5