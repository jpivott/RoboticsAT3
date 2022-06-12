import enemy
import characters
import random


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def modify_player(self, player):
        pass


class StartingTile(Tile):
    def intro_text(self):
        return """ 
        You must find your brother from the evil Goblin King Bowie! 
        You have snuck in to the dungeon of Bowie's castle.
        There are four doors you could take. Choose carefully adventurer.
        """


class EnemyGenerator(Tile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.20:
            self.enemy = enemy.Rat()
            self.battle_text = "A large, ferocious rat has scurried into your path" \
                               "Its large teeth are huge and razor sharp!"
            self.slain_text = "The rat has be slain, good job."
        elif r < 0.35
            self.enemy = enemy.Goblin()
            self.battle_text = "One of the Kings goblins blocks your way" \
                               "Its holds an old spear but looks well trained!"
            self.slain_text = "The goblin is dead! One less enemy to worry about."
        elif r < 0.55
            self.enemy = enemy.Rogue()
            self.battle_text = "A Rogue!" \
                               "One of the Kings assassins, be careful!"
            self.slain_text = "A well fought battle, the Rogue is no more!"
        elif r < 0.70
            self.enemy = enemy.DarkElf()
            self.battle_text = "On guard! A Dark Elf challenges you." \
                               "King Bowie enslaved these creatures to do his evil bidding"
            self.slain_text = "You have realised the Dark Elf from its survitude" \
                              "The elf thanks you with its dying breath."
        elif r < 0.80
            self.enemy = enemy.Wizard()
            self.battle_text = "An all powerful Wizard threatens your life" \
                               "One of the Kings strongest minions"
            self.slain_text = "You have won a great victory, the wizard is slain."
        elif r < 0.90
            self.enemy = enemy.Demon()
            self.battle_text = "You face a Demon of the underworld" \
                               "Prepare yourself, you may not survive this encounter"
            self.slain_text = "A great evil has been purged this day, well done adventurer" \
                              "Your name will be remembered always...if anyone saw what happened that is..."
        else
            self.enemy = enemy.GoblinKing()
            self.battle_text = "The King himself!" \
                               "He is slow from years of overeating but has great stamina"
            self.slain_text = "While you have defeated King Bowie you must be careful" \
                              "It is rumoured that the King is immortal and will always return."

        super().__init__(x, y)

    def enemy_text(self)


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
        super().__init__(x,y )

    def player_gold(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added to your bag.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed #possible error here with colon
            return """
            You already looted this room
            """
        else #possible error here with colon
            return """
            You have found some gold
            """


class MerchantTile(Tile):
    def __init__(self, x, y):
        self.merchant = characters.Merchant()
        super().__init__(x, y)

    def check_trade(self, player):
        while True #possible error here with colon
            print("What would you like to do? (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']
                return
            elif user_input in ['B', 'b']
                print("Please inspect my wares: ")
                self.shop(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']
                print("A list of what can be sold: ")
                self.shop(buyer-self.trader, seller=player)
            else
                print("Please try a different choice.")

    def shop(self, buyer, seller):
        for i, collectable in enumerate(seller.bag, 1):
            print("{}. {} - {} Gold".format(i, collectable.name, collectable.goldValue)
        while True:
            user_input = input("Select an item or press Q to exit the shop: ")
            if user_input in ['Q', "q"]
                return #possible error here with colon
            else
                try:
                    choice = int(user_input)
                    item_to_swap = seller.bag[choice - 1]
                    self.swap(seller, buyer, item_to_swap)
                except ValueError
                    print("The choice you made is invalid, try again.")

    def swap(self, seller, buyer, collectable):
        if collectable.goldValue > buyer.gold
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

