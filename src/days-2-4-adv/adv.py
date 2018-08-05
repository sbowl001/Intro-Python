from room import Room
from player import Player

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

newplayer = Player(room['outside'])
dir = ''
# Write a loop that:
#
while not dir == "q":
    print(newplayer.room.name)
# * Prints the current room name
    print(newplayer.room.description)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    dir = input("\n Please choose a direction...n, s, e, w, OR q to quit the game.\n ")
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if dir == "n":
        if hasattr(newplayer.room, "n_to"):
            newplayer.room = newplayer.room.n_to
        else: 
            print("Sorry, you've hit a wall")
    elif dir == "s":
        if hasattr(newplayer.room, "s_to"):
            newplayer.room = newplayer.room.s_to
        else: 
            print("Sorry, you've hit a wall")
    elif dir == "w":
        if hasattr(newplayer.room, "w_to"):
            newplayer.room = newplayer.room.w_to
        else: 
            print("Sorry, you've hit a wall")
    elif dir == "e":
        if hasattr(newplayer.room, "e_to"):
            newplayer.room = newplayer.room.e_to
        else: 
            print("Sorry, you've hit a wall")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    elif dir == "q":
        print("Thank you for playing!")
    else:
        print("\nInvalid selection.")
