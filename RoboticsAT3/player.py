import collectables


class Player:
    def __init__(self):
        self.bag = [collectables.Cheese(),
                    collectables.Slingshot(),
                    collectables.Potion()]
        self.health = 80
        self.gold = 10

    def alive(self):
        return self.health > 0

    def heal(self):
        usableItems = [collectable for collectable in self.bag if isintance(item, collectables.UsableItems)]
        if not usableItems:
            (print("Oh no, you're screwed mate. Maybe ask your Kiwi mates for a sheep because you currently have no healing options!"))

        for c, consumable in enumerate(usableItems, 1):
            print("Select which healing item you would like to use in order to extend your miserable existence")
            print("{}. {}".format(c, consumable))

        edible = False
        while not edible:
            choice = input("")
            try:
                eating = usableItems[int(choice) - 1]
                self.health = min(80, self.health + eating.healing_value)
                print("Your current health is now: {}".format(self.health))
                edible = True
            except (ValueError, IndexError):
                print("Your choice either cannot be eaten or is not on the list, try again.")

    def show_bag_contents(self):
        print("Bag Contents:")
        for collectable in self.bag:
            print('* ' + str(collectable))
            print("Gold: {}".format(self.gold))

    def use_best_weapon(self):
        damage = 0
        weapon = None
        for collectable in self.bag:
            try:
                if collectable.damage > damage:
                    weapon = collectable
                    damage = collectable.damage
            except AttributeError:
                pass

        return weapon