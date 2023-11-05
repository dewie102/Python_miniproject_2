"""Module to handle quests"""

from task import Task

class Quest:
    """This is a representation of quests to be completed"""
    def __init__(self):
        self.name = ""
        self.description = ""
        self.required = False
        self.tasks: Task = []
        self.is_complete = False


    def complete_quest(self):
        """If all the tasks are complete, set the quest as complete"""
        for task in self.tasks:
            if not task.complete:
                print("Not all tasks are compete")
                return

        self.is_complete = True


    def __repr__(self):
        return f"Quest:\n\tname: {self.name}\n\tdescription: {self.description}\n\trequired: {self.required}\n\ttasks: {self.tasks}"


    def __str__(self):
        return f"Quest:\n\tname: {self.name}\n\tdescription: {self.description}\n\trequired: {self.required}\n\ttasks: {self.tasks}"
