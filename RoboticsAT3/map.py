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
    def start_dialogue(self):
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