"""RPG Text Adventure Main module"""
#!/usr/bin/env python3

import level_loader
from player import Player
from room import Room
from quest import Quest

def show_instructions():
    """print a main menu and the commands"""
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    look [furniture]
    inventory
    quests
    ''')

# Load the rooms and quests for level 0
rooms = level_loader.load_level(0)

# Instantiate the player
player = Player(rooms.get("Hall", Room()))
player.quests = level_loader.load_quests(0)

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
        if player.location and move[1] in player.location.neighboring_rooms:
            new_room: Room | None = rooms.get(move[1])
            if new_room:
                #set the current room to the new room
                player.location = new_room
            else:
                print("Something went wrong picking that room")
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    elif move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if player.location.items and move[1] in player.location.items:
            # As long as the item isn't hidden, take it
            item = player.location.items.get(move[1])

            if item and not item.hidden:
                #add the item to their inventory
                player.inventory.append({move[1]: player.location.items[move[1]]})
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from the room
                del player.location.items[move[1]]
            else:
                print(f"And where would you like me to find a {move[1]}?")
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    elif move[0] == "look":
        if player.location.furniture:
            player.location.look_at_furniture(move[1])
    elif move[0] == "inventory":
        player.display_inventory()
    elif move[0] == "quests":
        for quest in player.quests.items():
            if not quest[1].is_complete:
                print(quest[1].print_quest())


    for quest in player.quests.items():
        player.can_complete_quest(quest[1])
        if quest[1].is_complete:
            print(f"quest completed!\n{quest[1].print_quest()}")

    ## Define how a player can win
    if player.location.name == 'Garden':
        garden_quest: Quest | None = player.quests.get("End Game")
        if garden_quest and garden_quest.is_complete:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break

    ## If a player enters a room with a monster
    if player.location.enemies and 'monster' in player.location.enemies:
        monster_quest: Quest | None = player.quests.get("Distract The Monster")
        if monster_quest and monster_quest.is_complete:
            print("You dealt with the monster and are free to roam")
            del player.location.enemies["monster"]
        else:
            print('A monster has got you... GAME OVER!')
            break
