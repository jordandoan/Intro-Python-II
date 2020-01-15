# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.e_to = None
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.items = {}

    def listItems(self) -> [str]:
        if not(len(self.items)):
            return ['No items']
        arr = [0]*len(self.items)
        count = 0
        for key in self.items:
            arr[count] = self.items[key].name
            count += 1
        return arr