"""Module for providing a method to load a level from a JSON file"""
#!/usr/bin/env python3

import json
from typing import List
from pprint import pprint

from monster import Monster
from item import Item
from room import Room


def process_items(item_dict):
    """Takes a dictionary of items from JSON and creates the items
        and returns the list of items in that particular room"""
    items = []
    for item in item_dict:
        item_obj = Item()
        for item_prop in item.items():
            item_obj.name = item_prop[0]
            item_obj.hidden = item_prop[1].get("hidden")
            item_obj.location = item_prop[1].get("location")
            items.append({item_obj.name: item_obj})

    return items


def process_enemy(enemy_dict):
    """Takes a room key, value tuple from JSON and creates the enemy
        and returns the list of enemies in that particular room"""
    enemies = []
    for enemy in enemy_dict:
        enemy_obj = Monster()
        for enemy_prop in enemy.items():
            enemy_obj.name = enemy_prop[0]
            enemy_obj.location = enemy_prop[1].get("location")
            enemy_obj.type = enemy_prop[1].get("type")
            enemies.append({enemy_obj.name: enemy_obj})

    return enemies


def load_level(level_number: int) -> dict[str, Room]:
    """Main function for testing"""
    rooms = {}

    try:
        with open(f"level_{level_number}.json", "r", encoding="UTF-8") as level:
            data = json.load(level) # This is the full json as python object
            for room in data.items():
                room_obj = Room()
                room_obj.name = room[0]

                room_obj.neighboring_rooms = room[1].get("direction")

                items = process_items(room[1].get("items", {}))
                enemies = process_enemy(room[1].get("enemy", {}))

                for item in items:
                    room_obj.items.update(item)

                for enemy in enemies:
                    room_obj.enemies.update(enemy)

                rooms.update({room_obj.name: room_obj})
    except OSError as ex:
        print(f"Something went wrong with opening the file:\n{ex}")

    return rooms


if __name__ == "__main__":
    pprint(load_level(0))
