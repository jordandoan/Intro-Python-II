# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.current_room = location
        self.items = {}

    def listItems(self) -> str:
        if not(len(self.items)):
            return ['No items']
        arr = [0]*len(self.items)
        count = 0
        for key in self.items:
            arr[count] = self.items[key].name
            count += 1
        return f"Inventory: {arr}"
