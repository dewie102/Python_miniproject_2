"""Module representing a Player object"""

from task import Task, TaskType
from quest import Quest

class Player:
    """Class representing a Player"""
    def __init__(self):
        self.name = ""
        self.location = ""
        self.inventory = []
        self.quests = []


    def can_complete_quest(self, quest):
        """Determines if the quest can be complete"""
        for task in quest.tasks:
            if not task.complete:
                if self.can_complete_task(task):
                    task.complete = True

    
    def can_complete_task(self, task):
        """Determines if the task can be complete"""
        match task.type:
            case TaskType.INVENTORY:
                print("what")


    def __repr__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"


    def __str__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"
