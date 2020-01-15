from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Items
sword = Item("Sword", "A long sword.")
coins = Item("Coins", "Money!")
nugget = Item("Chicken Nugget", "Looks good...")
branch = Item("Branch", "A stick.")

room['foyer'].items.update({"sword": sword})
room['overlook'].items.update({"branch": branch})
room['overlook'].items.update({"coins": coins})
room['treasure'].items.update({"nugget": nugget})

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player("Jordan", room['outside'])
playing = True

def prompt(room: Room) -> str:
    ans = input("What direction would you like to go? [N] North [W] West [S] South [E] East [Get ITEM] Get Item [Q] Quit: ").lower()
    new_ans = ans.split(' ')
    if len(new_ans) == 1:
        ans = ans[0]
        if ans == "q":
            return ""
        elif ans == "n" or ans == "s" or ans == "w" or ans == "e":
            return ans
        else:
            print("Invalid action...")
            return prompt(room)
    else:
        if new_ans[0] != "get":
            print("Invalid action...")
            return prompt(room)
        if not room.items.get(new_ans[1]):
            print("Item does not exist")
            return prompt(room)
        else:
            item = room.items.pop(new_ans[1])
            player.items.update({new_ans[1]: item})


def check_room(player: Player, ans: str):
    new_room = getattr(player.current_room, f"{ans}_to")
    if not new_room:
        print("There is nothing here.")
    else:
        player.current_room = new_room


while playing:
    print(player.current_room.name)
    print(player.current_room.description)
    print(player.current_room.listItems())
    ans = prompt(player.current_room)
    if not ans:
        break
    check_room(player, ans)
    print("\n")