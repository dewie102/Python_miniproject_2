"""Module representing a Player object"""

from task import Task, TaskType
from item import Item
from quest import Quest
from room import Room

class Player:
    """Class representing a Player"""
    def __init__(self):
        self.name = ""
        self.location: Room = None
        self.inventory: list[Item] = []
        self.quests: list[Quest] = []


    def can_complete_quest(self, quest: Quest):
        """Determines if the quest can be complete"""
        completed_tasks = 0
        for task in quest.tasks:
            if not task.complete:
                if self.can_complete_task(task):
                    task.complete = True
                    completed_tasks += 1

        if completed_tasks >= quest.number_of_necessary_tasks:
            quest.is_complete = True


    def can_complete_task(self, task: Task):
        """Determines if the task can be complete"""
        match task.type:
            case TaskType.INVENTORY:
                for item in task.needed_items:
                    for key, value in item.items():
                        if key in self.inventory and self.inventory[key] == value:
                            task.complete = True


    def show_status(self):
        """print the player's current status"""
        print('---------------------------')
        print('You are in the ' + self.location.name)
        #print the current inventory
        print('Inventory : ' + str(self.inventory))
        #print an item if there is one
        if self.location.items:
            print('You see ' + str.join(", ", self.location.items.keys()))
        print("---------------------------")


    def __repr__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"


    def __str__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"
