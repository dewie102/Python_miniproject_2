"""Module to define a room object"""


class Room:
    """Class representing a room"""

    def __init__(self):
        self.name = ""
        self.neighboring_rooms = {}
        self.items = {}
        self.enemies = {}

    def __repr__(self):
        return f'''
                Room:
                    name: {self.name}
                    neighboring_rooms: {self.neighboring_rooms}
                    items: {self.items}
                    enemies: {self.enemies}
                '''

    def __str__(self):
        return f'''
                Room:
                    name: {self.name}
                    neighboring_rooms: {self.neighboring_rooms}
                    items: {self.items}
                    enemies: {self.enemies}
                '''
