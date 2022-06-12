import collectables


class Characters():
    def __init__(self):
        pass

    def __str__(self):
        return self.description


class Merchant(Characters):
    def __init__(self):
        self.description = "Merchant"
        self.gold = 200
        self.items = [collectables.Katana(),
                      collectables.Steak(),
                      collectables.Sword(),
                      collectables.Potion(),
                      collectables.MajorPotion(),
                      collectables.GiganticPotion()]