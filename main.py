"""RPG Text Adventure Main module"""
#!/usr/bin/env python3

import level_loader
from player import Player

def show_instructions():
    """print a main menu and the commands"""
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    quests
    ''')

# Instantiate the player
player = Player()

# Load the rooms and quests for level 0
rooms = level_loader.load_level(0)
player.quests = level_loader.load_quests(0)

# start the player in the Hall
player.location = rooms.get("Hall")

show_instructions()

#loop forever
while True:

    player.show_status()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in player.location.neighboring_rooms:
            #set the current room to the new room
            player.location = rooms.get(player.location.neighboring_rooms[move[1]])
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if player.location.items and move[1] in player.location.items: # don't think this will work
            #add the item to their inventory
            player.inventory.append({move[1]: player.location.items[move[1]]})
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del player.location.items[move[1]]
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == "quests":
        for quest in player.quests.items():
            if not quest[1].is_complete:
                print(quest[1].print_quest())


    for quest in player.quests.items():
        player.can_complete_quest(quest[1])
        if quest[1].is_complete:
            print(f"quest completed!\n{quest[1].print_quest()}")

    ## Define how a player can win
    if player.location.name == 'Garden' and player.quests.get("End Game").is_complete:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster
    if player.location.enemies and 'monster' in player.location.enemies:
        if player.quests.get("Distract The Monster").is_complete:
            print("You dealt with the monster and are free to roam")
            del player.location.enemies["monster"]
        else:
            print('A monster has got you... GAME OVER!')
            break
