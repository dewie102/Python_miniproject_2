"""Module to handle tasks for quests"""

from enum import Enum
from typing import List


class TaskType(Enum):
    """This is to represent the type of tasks to figure out how to process complete"""
    INVENTORY = 0
    ACTION = 1


class Task:
    """This is a respresntation for Tasks"""
    def __init__(self):
        self.name: str = ""
        self.required: bool = False
        self.description: str  = ""
        self.complete: bool = False
        self.type = TaskType.INVENTORY
        self.needed_items: List[dict[str, str]] = []


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
