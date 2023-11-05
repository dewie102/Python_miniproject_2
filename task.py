"""Module to handle tasks for quests"""

class Task:
    """This is a respresntation for Tasks"""
    def __init__(self):
        self.name = ""
        self.required = False
        self.description = ""
        self.complete = False
