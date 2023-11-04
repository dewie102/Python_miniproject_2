"""Module representing a Player object"""

class Player:
    """Class representing a Player"""
    def __init__(self):
        self.name = ""
        self.location = ""
        self.inventory = []

    def __repr__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"

    def __str__(self):
        return f"Player:\n\tname: {self.name}\n\tlocation: {self.location}\n\tinventory: {self.inventory}"
