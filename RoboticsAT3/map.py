import enemy
import characters
import random


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartingTile(Tile):
    def intro_text(self):
        return """ 
        You must save your brother from the evil Goblin King Bowie! 
        You have snuck in to the dungeon of Bowie's castle.
        There are many paths to take. Choose carefully adventurer.
        """


class EnemyGenerator(Tile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.20:
            self.enemy = enemy.Rat()
            self.battle_text = '\033[1;35m' + """
                               A large, ferocious rat has scurried into your path
                               Its large teeth are huge and razor sharp!
                               """ + '\033[0;37m'
            self.slain_text = """
                              The rat has be slain, good job.
                              """
        elif r < 0.35:
            self.enemy = enemy.Goblin()
            self.battle_text = """
                               One of the Kings goblins blocks your way.
                               It holds an old spear but looks well trained!
                               """
            self.slain_text = """
                              The goblin is dead! One less enemy to worry about.
                              """
        elif r < 0.55:
            self.enemy = enemy.Rogue()
            self.battle_text = """
                               A Rogue!
                               One of the Kings assassins, be careful!
                               """
            self.slain_text = """
                              A well fought battle, the Rogue is no more!
                              """
        elif r < 0.70:
            self.enemy = enemy.DarkElf()
            self.battle_text = """
                               On guard! A Dark Elf challenges you.
                               King Bowie enslaved these creatures to do his evil bidding
                               """
            self.slain_text = """
                               You have realised the Dark Elf from its survitude,
                               The elf thanks you with its dying breath.
                               """
        elif r < 0.80:
            self.enemy = enemy.Wizard()
            self.battle_text = """
                               An all powerful Wizard threatens your life,
                               One of the Kings strongest minions!
                               """
            self.slain_text = """
                              You have won a great victory, the wizard is slain.
                              """
        elif r < 0.90:
            self.enemy = enemy.Demon()
            self.battle_text = """
                               You face a Demon of the underworld,
                               Prepare yourself, you may not survive this encounter
                               """
            self.slain_text = """
                              A great evil has been purged this day, well done adventurer
                              Your name will be remembered always...if anyone saw what happened that is...
                              """
        else:
            self.enemy = enemy.GoblinKing()
            self.battle_text = '\033[1;35m' + """
                               The King himself!
                               He is slow from years of overeating but has great stamina
                               """ + '\033[0;37m'
            self.slain_text = """
                              While you have defeated King Bowie you must be careful.
                              It is rumoured that the King is immortal and will always return.
                              """

        super().__init__(x, y)

    def intro_text(self):
        text = self.battle_text if self.enemy.alive() else self.slain_text
        return text

    def modify_player(self, player):
        if self.enemy.alive():
            player.health = player.health - self.enemy.damage
            print("{} hurts your for {} points of health damage. Your remaining health: {}".format(self.enemy.description, self.enemy.damage, player.health))


class WinTile(Tile):
    def player_win(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You have rescued your brother from the dungeons
        and defeated the evil Goblin King Bowie (may he rest in peace)

        You have won!
        """

class GoldTile(Tile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added to your bag.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            You already looted this room
            """
        else:
            return """
            You have found some gold
            """


class MerchantTile(Tile):
    def __init__(self, x, y):
        self.merchant = characters.Merchant()
        super().__init__(x, y)

    def check_trade(self, player):
        while True:
            print("What would you like to do? (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Please inspect my wares: ")
                self.shop(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("A list of what can be sold: ")
                self.shop(buyer-self.trader, seller=player)
            else:
                print("Please try a different choice.")

    def shop(self, buyer, seller):
        for i, collectable in enumerate(seller.bag, 1):
            print("{}. {} - {} Gold".format(i, collectable.name, collectable.goldValue))
        while True:
            user_input = input("Select an item or press Q to exit the shop: ")
            if user_input in ['Q', "q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    item_to_swap = seller.bag[choice - 1]
                    self.swap(seller, buyer, item_to_swap)
                except ValueError:
                    print("The choice you made is invalid, try again.")

    def swap(self, seller, buyer, collectable):
        if collectable.goldValue > buyer.gold:
            print("Hmm, that item costs too much gold")
            return
        seller.bag.remove(collectable)
        buyer.bag.append(collectable)
        seller.gold = seller.gold + collectable.goldValue
        buyer.gold = buyer.gold - collectable.goldValue
        print("Thanks for doing business!")

    def intro_text(self):
        return """
        A quick-witted looking Merchant eyes you greedily.
        You may buy or sell with this person but you better
        be on your toes!
        """

tile_dictionary = {"WT": WinTile,
                   "ST": StartingTile,
                   "GT": GoldTile,
                   "ET": EnemyGenerator,
                   "MT": MerchantTile,
                   "  ": None}

map_dsl = """
|GT|ET|ET|ET|GT|
|MT|WT|ET|GT|ET|
|ET|GT|GT|ET|MT|
|GT|MT|ET|ST|ET|
|GT|ET|ET|ET|GT|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|WT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

game_map = []

starting_tile = None

def parse_map_dsl():
    if not is_dsl_valid(map_dsl):
        raise SyntaxError("DSL is not valid")

    dsl_lines = map_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_dictionary[dsl_cell]
            if tile_type == StartingTile:
                global starting_tile
                starting_tile = x, y
            row.append(tile_type(x, y) if tile_type else None)

        game_map.append(row)

def player_location(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return game_map[y][x]
    except IndexError:
        return None