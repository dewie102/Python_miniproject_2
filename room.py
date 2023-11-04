"""Module to define a room object"""


class Room:
    """Class representing a room"""

    def __init__(self):
        self.name = ""
        self.neighboring_rooms = {}
        self.items = {}
        self.enemies = {}

    def __repr__(self):
        return f"Room:\n\tname: {self.name}\n\tneighboring_rooms: {self.neighboring_rooms}\n\titems: {self.items}\n\tenemies: {self.enemies}"

    def __str__(self):
        return f"Room:\n\tname: {self.name}\n\tneighboring_rooms: {self.neighboring_rooms}\n\titems: {self.items}\n\tenemies: {self.enemies}"
