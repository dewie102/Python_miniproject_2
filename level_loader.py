"""Module for providing a method to load a level from a JSON file"""
#!/usr/bin/env python3

import json
from pprint import pprint
from typing import List, Dict, TypedDict

from monster import Monster
from item import Item
from room import Room
from quest import Quest
from task import Task


Item_Dict = TypedDict('Item', {"name": str, "hidden": bool, "location": str})
Enemy_Dict = TypedDict('Enemy', {"type": str, "sublocation": str})
Task_Dict = TypedDict("Task", {"name": str, "description": str, "required": bool, "needed_items": List[Dict[str, str]]})


def process_items(item_list: List[Dict[str, Item_Dict]]) -> list[Dict[str, Item]]:
    """Takes a dictionary of items from JSON and creates the items
        and returns the list of items in that particular room"""
    items: List[Dict[str, Item]] = []
    for item in item_list:
        item_obj: Item = Item()
        for item_prop in item.items():
            item_obj.type = item_prop[0]
            item_obj.name = item_prop[1].get("name", item_prop[0])
            item_obj.hidden = item_prop[1].get("hidden")
            item_obj.location = item_prop[1].get("location")
            items.append({item_obj.type: item_obj})

    return items


def process_enemy(enemy_list: List[Dict[str, Enemy_Dict]]) -> List[Dict[str, Monster]]:
    """Takes a room key, value tuple from JSON and creates the enemy
        and returns the list of enemies in that particular room"""
    enemies: List[Dict[str, Monster]] = []
    for enemy in enemy_list:
        enemy_obj = Monster()
        for enemy_prop in enemy.items():
            enemy_obj.name = enemy_prop[0]
            enemy_obj.sublocation = enemy_prop[1].get("sublocation")
            enemy_obj.type = enemy_prop[1].get("type")
            enemies.append({enemy_obj.name: enemy_obj})

    return enemies


def process_tasks(task_list: List[Task_Dict]) -> list[Task]:
    """Takes a list of tasks from JSON and creates the tasks
        and returns the list objects for that particular quest"""
    tasks: List[Task] = []
    for task in task_list:
        task_obj: Task = Task()
        task_obj.name = task.get("name")
        task_obj.description = task.get("description")
        task_obj.required = task.get("required")
        needed_items: List[Dict[str, str]] = []
        for item in task.get("needed_items", []):
            needed_items.append(item)

        task_obj.needed_items = needed_items

        tasks.append(task_obj)

    return tasks


def load_quests(level_number: int) -> Dict[str, Quest]:
    """Basic method for loading the quests for the level"""
    quests: Dict[str, Quest] = {}

    try:
        with open(f"quests_{level_number}.json", "r", encoding="UTF-8") as quest_file:
            data = json.load(quest_file)
            for quest in data.items():
                quest_obj = Quest()
                quest_obj.name = quest[1].get("name")
                quest_obj.description = quest[1].get("description")
                quest_obj.required = quest[1].get("required")
                quest_obj.number_of_necessary_tasks = quest[1].get("number_of_necessary_tasks")

                tasks: list[Task] = process_tasks(quest[1].get("tasks", []))
                quest_obj.tasks = tasks


                quest_obj.set_number_of_necessary_tasks()
                quests.update({quest[0]: quest_obj})
    except OSError as ex:
        print(f"Something went wrong with opening the file:\n{ex}")

    return quests


def load_level(level_number: int) -> Dict[str, Room]:
    """Basic method for loading the level"""
    rooms: Dict[str, Room] = {}

    try:
        with open(f"level_{level_number}.json", "r", encoding="UTF-8") as level_file:
            data = json.load(level_file) # This is the full json as python object
            for room in data.items():
                room_obj = Room()
                room_obj.name = room[0]

                room_obj.neighboring_rooms = room[1].get("direction")

                items = process_items(room[1].get("items", []))
                enemies = process_enemy(room[1].get("enemy", {}))

                for item in items:
                    room_obj.items.update(item)

                for enemy in enemies:
                    room_obj.enemies.update(enemy)

                room_obj.furniture = room[1].get("furniture", {})
                room_obj.base_description = room[1].get("base_description", "")

                rooms.update({room_obj.name: room_obj})
    except OSError as ex:
        print(f"Something went wrong with opening the file:\n{ex}")

    return rooms


if __name__ == "__main__":
    pprint(load_level(0))
