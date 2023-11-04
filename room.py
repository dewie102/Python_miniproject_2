"""Module to define a room object"""

class Room:
    """Class representing a room"""
    def __init__(self):
        self.name = ""
        self.neighboring_rooms = {}
        self.items = {}
        self.enemies = {}
