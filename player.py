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
        self.quests: dict[str, Quest] = {}
        #self.completed_quests: list[Quest] = []


    def can_complete_quest(self, quest_key: str, quest: Quest):
        """Determines if the quest can be complete"""
        completed_tasks = 0
        for task in quest.tasks:
            if not task.complete:
                if self.can_complete_task(task):
                    completed_tasks += 1
            elif task.complete:
                completed_tasks += 1

        if completed_tasks >= quest.number_of_necessary_tasks:
            quest.is_complete = True
            """ self.completed_quests.append({quest_key: quest})
            self.quests.pop(quest_key) """



    def can_complete_task(self, task: Task):
        """Determines if the task can be complete"""
        match task.type:
            case TaskType.INVENTORY:
                for item in task.needed_items:
                    item_type = list(item.keys())[0]
                    for inventory_item in self.inventory:
                        if item_type == list(inventory_item.keys())[0]:
                            if list(item.values())[0].lower() == list(inventory_item.values())[0].name.lower():
                                task.complete = True
                                return True
        
        return False


    def show_status(self):
        """print the player's current status"""
        print('---------------------------')
        print('You are in the ' + self.location.name)
        #print the current inventory
        inv = []
        for item in self.inventory:
            inv.append(list(item.keys())[0])
        print("Inventory : " + str(inv))
        #print('Inventory : ' + str(self.inventory))
        #print an item if there is one
        if self.location.items:
            print('You see ' + str.join(", ", self.location.items.keys()))
        print("---------------------------")


    def __repr__(self):
        return f'''
        Player:
            name: {self.name}
            location: {self.location}
            inventory: {self.inventory}
            quests: {self.quests}
        '''


    def __str__(self):
        return f'''
        Player:
            name: {self.name}
            location: {self.location}
            inventory: {self.inventory}
            quests: {self.quests}
        '''
