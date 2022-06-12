from collections import OrderedDict
from player import Player
import map
import os
os.system("cls")

def play():
    print('\033[0;32m' + """         #####         #########   ###########  ##### ##### ###########   ##### ######   ##### ########### #####   #####    
        ``###         ###`````### ``###`````###``### ``### ``###`````### ``### ``###### ``### `#```###```#``###   ``###     
         `###        `###    `###  `###    `### ``### ###   `###    `###  `###  `###`### `### `   `###  `  `###    `###     
         `###        `###########  `##########   ``#####    `##########   `###  `###``###`###     `###     `###########     
         `###        `###`````###  `###`````###   ``###     `###`````###  `###  `### ``######     `###     `###`````###     
         `###      # `###    `###  `###    `###    `###     `###    `###  `###  `###  ``#####     `###     `###    `###     
         ########### #####   ##### ###########     #####    #####   ##### ##### #####  ``#####    #####    #####   #####    
        ``````````` `````   ````` ```````````     `````    `````   ````` ````` `````    `````    `````    `````   `````     """ + '\033[0;37m')
    print('\033[0;31m' + "                                      !SAVE YOUR BROTHER FROM THE EVIL GOBLIN KING!" + '\033[0;37m')

    map.parse_map_dsl()
    player = Player()
    while player.alive() and not player.victory:
        location = map.player_location(player.x, player.y)
        print(location.intro_text())
        location.modify_player(player)
        if player.alive() and not player.victory
            player_action(location, player)
        elif not player.alive()
            print("You have died, your brother will rot in the dungeons of King Bowie forever!")

def player_action(location, player):
    action = None
    while not action:
        possible_actions = get_possible_actions(location, player)
        player_choice = input("Action: ")
        action = possible_actions.get(player_choice)
        if action:
            action()
        else:
            print("Your choice was impossible, choose again.")

def get_possible_actions(location, player):
    actions = OrderedDict()
    print("Choose your next move: ")
    if player.bag:
        action_adder(actions, 'b', player.show_bag_contents, "Print bag contents")
    if isinstance(location, map.MerchantTile):
        action_adder(actions, 'm', player.trade, "Trade with Merchant")
    if isinstance(location, map.EnemyGenerator) and location.enemy.alive():
        action_adder(actions, 'a' player.attack, "Attack the enemy")
    else:
        if map.player_location(location.x, location.y - 1):
            action_adder(actions, 'u', player.move_up, "Go up")
        if map.player_location(location.x, location.y + 1):
            action_adder(actions, 'd', player.move_up, "Go down")
        if map.player_location(location.x + 1, location.y):
            action_adder(actions, 'r', player.move_up, "Go right")
        if map.player_location(location.x - 1, location.y):
            action_adder(actions, 'l', player.move_up, "Go left")
    if player.health < 80:
        action_adder(actions, 'h', player.heal, "Heal yourself")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}".format(name))

play()
