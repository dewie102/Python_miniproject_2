"""Module to define an item object"""

class Item:
    """Class representing an item"""
    def __init__(self):
        self.name = ""
        self.type = ""
        self.hidden = False
        self.location = ""


    def __repr__(self):
        return f"Item:\n\tname: {self.name}\n\tlocation: {self.location}\n\thidden: {self.hidden}"


    def __str__(self):
        return f"Item:\n\tname: {self.name}\n\tlocation: {self.location}\n\thidden: {self.hidden}"
