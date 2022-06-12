import collectables
import map


class Player:
    def __init__(self):
        self.bag = [collectables.Cheese(),
                    collectables.Slingshot(),
                    collectables.Potion()]
        self.health = 80
        self.gold = 10
        self.victory = False
        self.x = map.starting_tile[0]
        self.y = map.starting_tile[1]

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

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_up(self):
        self.move(dx= 0, dy = 1)

    def move_down(self):
        self.move(dx= 0, dy = -1)

    def move_left(self):
        self.move(dx = -1, dy = 0)

    def move_right(self):
        self.move(dx = 1, dy = 0)

    def attack(self):
        weapon = self.use_best_weapon()
        location = map.player_location
        enemy = location.enemy
        print("You use your {} to attack {}.".format(weapon.description, enemy.decription))
        enemy.health -= weapon.damage
        if not enemy.alive():
            print("You have killed the {}.".format(enemy.description))
        else:
            print("Health remaining for the {} is {} points".format(enemy.description, enemy.health))

    def trade(self):
        location = map.player_location(self.x, self.y)
        location.check_trade(self)