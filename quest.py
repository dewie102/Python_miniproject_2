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
        # This determines how many tasks need to be completed to complete the quest
        # -1 means all the tasks, or at least all the required tasks
        self.number_of_necessary_tasks = -1


    def complete_quest(self):
        """If all the tasks are complete, set the quest as complete"""
        for task in self.tasks:
            if not task.complete:
                print("Not all tasks are compete")
                return

        self.is_complete = True


    def set_number_of_necessary_tasks(self):
        """The main purpose of this is to ensure only required tasks are
        counted when completing a quest later on"""
        if self.number_of_necessary_tasks == -1:
            required_tasks = 0
            for task in self.tasks:
                if task.required:
                    required_tasks += 1

            self.number_of_necessary_tasks = required_tasks


    def __repr__(self):
        return f"Quest:\n\tname: {self.name}\n\tdescription: {self.description}\n\trequired: {self.required}\n\ttasks: {self.tasks}"


    def __str__(self):
        return f"Quest:\n\tname: {self.name}\n\tdescription: {self.description}\n\trequired: {self.required}\n\ttasks: {self.tasks}"
