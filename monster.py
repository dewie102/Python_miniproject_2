"""Module representing a Monster object"""
from player import Player

class Monster(Player):
    """Class representing a Monster"""
    def __init__(self):
        super().__init__()
        self.type = ""

    def __repr__(self):
        return super().__repr__() + f"\n\ttype: {self.type}"

    def __str__(self):
        return super().__repr__() + f"\n\ttype: {self.type}"
