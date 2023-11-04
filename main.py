"""RPG Text Adventure Main module"""
#!/usr/bin/env python3

import level_loader

def show_instructions():
    """print a main menu and the commands"""
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    ''')

def show_status():
    """print the player's current status"""
    print('---------------------------')
    print('You are in the ' + currentRoom.name)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if currentRoom.items:
        print('You see ' + str.join(", ", currentRoom.items.keys()))
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = level_loader.load_level(0)

#start the player in the Hall
currentRoom = rooms.get("Hall")

show_instructions()

#loop forever
while True:

    show_status()

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
        if move[1] in currentRoom.neighboring_rooms:
            #set the current room to the new room
            currentRoom = rooms.get(currentRoom.neighboring_rooms[move[1]])
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if currentRoom.items and move[1] in currentRoom.items: # don't think this will work
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del currentRoom.items[move[1]]
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## Define how a player can win
    if currentRoom.name == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster
    if currentRoom.enemies and 'monster' in currentRoom.enemies:
        print('A monster has got you... GAME OVER!')
        break
