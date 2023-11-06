"""Module to define a room object"""


class Room:
    """Class representing a room"""
    def __init__(self):
        self.name = ""
        self.neighboring_rooms = {}
        self.items = {}
        self.enemies = {}
        self.furniture = {}
        self.base_description = ""


    def print_description(self):
        """This method prints out the description of the room with the description of furniture"""
        print(self.base_description)
        if self.furniture:
            print("Inside the room you see: ", end ="")
            furniture_descriptions = ""
            for furn in self.furniture.items():
                furniture_descriptions += furn[1][0] + ", "
            print(furniture_descriptions[:-2]) # Gets rid of the last ', '
        if self.items:
            print("You also see the following items : [", end="")
            items = []
            for item in self.items.items():
                if not item[1].hidden:
                    items.append(item[0])

            print(f"{str.join(', ', items)}]")


    def look_at_furniture(self, furniture_key: str):
        """Method to print the look description/ dialog of furniture_key"""
        furn_desc_list = self.furniture.get(furniture_key, [])
        if furn_desc_list:
            print(self.furniture.get(furniture_key)[1])

            for item in self.items.items():
                if item[1].hidden and item[1].location == furniture_key:
                    item[1].hidden = False
        else:
            print(f"I can't describe the {furniture_key}")


    def __repr__(self):
        return f'''
        Room:
            name: {self.name}
            neighboring_rooms: {self.neighboring_rooms}
            items: {self.items}
            enemies: {self.enemies}
            furniture: {self.furniture}
        '''


    def __str__(self):
        return f'''
        Room:
            name: {self.name}
            neighboring_rooms: {self.neighboring_rooms}
            items: {self.items}
            enemies: {self.enemies}
            furniture: {self.furniture}
        '''
