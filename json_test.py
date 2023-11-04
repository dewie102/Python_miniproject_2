"""Module providing a testing environment for json reading and writting"""
#!/usr/bin/env python3

import json
from pprint import pprint
import os

from player import Player
from monster import Monster
from item import Item
from room import Room


def main():
    """Main function for testing"""

    os.system("clear")

    rooms = []

    with open("level_0.json", "r") as level:
        data = json.load(level) # This is the full json as python object
        for room_item in data.items():
            room = Room()
            room.name = room_item[0]

            room.neighboring_rooms = room_item[1].get("direction")
            
            for i in room_item[1].get("items"):
                print(i)
                print(type(i))
                print(dir(i))
                item = Item()
                for item_prop in i.items():
                    item.name = item_prop[0]
                    item.hidden = item_prop[1].get("hidden")
                    item.location = item_prop[1].get("location")
            
            pprint(room)
            rooms.append(room)

    pprint(rooms)


if __name__ == "__main__":
    main()
