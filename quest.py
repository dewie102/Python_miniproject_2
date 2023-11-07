"""Module to handle quests"""

from textwrap import dedent
from typing import List

from task import Task

class Quest:
    """This is a representation of quests to be completed"""
    def __init__(self):
        self.name = ""
        self.description = ""
        self.required = False
        self.tasks: List[Task] = []
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


    def print_quest(self):
        """Method to print out the quest nicely"""
        return dedent(f'''
        Quest:
            name: {self.name}
            description: {self.description}
            Quest Complete: {self.is_complete}
        ''')


    def __repr__(self):
        return f'''
        Quest:
            name: {self.name}
            description: {self.description}
            required: {self.required}
            tasks: {self.tasks}
            is_complete: {self.is_complete}
            number_of_necessary_tasks: {self.number_of_necessary_tasks}
        '''


    def __str__(self):
        return f'''
        Quest:
            name: {self.name}
            description: {self.description}
            required: {self.required}
            tasks: {self.tasks}
            is_complete: {self.is_complete}
            number_of_necessary_tasks: {self.number_of_necessary_tasks}
        '''
