"""Module to handle tasks for quests"""

from enum import Enum


class TaskType(Enum):
    """This is to represent the type of tasks to figure out how to process complete"""
    INVENTORY = 0


class Task:
    """This is a respresntation for Tasks"""
    def __init__(self):
        self.name = ""
        self.required = False
        self.description = ""
        self.complete = False
        self.type = TaskType.INVENTORY
        self.needed_items = []


    def __repr__(self):
        return f'''
                Task:
                    name: {self.name}
                    description: {self.description}
                    required: {self.required}
                    type: {self.type}
                    complete: {self.complete}
                '''


    def __str__(self):
        return f'''
                Task:
                    name: {self.name}
                    description: {self.description}
                    required: {self.required}
                    type: {self.type}
                    complete: {self.complete}
                '''
