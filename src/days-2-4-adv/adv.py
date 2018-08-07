from room import Room
from player import Player

# Declare all the rooms

room = {
    'village':  Room("Village Hidden in the Spring",
                     "The noise of bustling streets warm your heart"),

    'home':    Room("Home Sweet Home", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'attic': Room("Attic Room", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'forest':   Room("Grand Forest", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

   'overlook':   Room("Mountain Overlook", """A steep mountain appears before you. The forest expands in all directions. Perhaps a further look is needed..."""),

   'peak':   Room("Mountain Peak", """The fresh air soothes your senses, the forest expanse looks peaceful. The village looks minute in the distance."""),

   'cave':   Room("North Cave", """Creaking sounds resonate throughout the cave."""),

   'underground1':   Room("Underground Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

   'tunnels':   Room("Dark Tunnels", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

   'secret':   Room("Secret Passage", """The passage holds an air of mystery. The walls glimmer with something hidden beneath."""),

   'epic':   Room("Epic Treasure", """The room contains the most special of treasure chests. Open it to reveal your prize."""),

   'underground2':   Room("Damp Underground Passage", """Moist droplets of water fall from the passage's crevices."""),

    'dragon': Room("Dragon Lair", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

   'swamp':   Room("Sinister Swamp", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

   'mangroves':   Room("Mangrove Forest", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
}


# Link rooms together

room['village'].n_to = room['forest']
room['forest'].s_to = room['village']
room['village'].s_to = room['home']
room['home'].n_to = room['village']
room['home'].u_to = room['attic']
room['attic'].d_to = room['home']
room['forest'].w_to = room['overlook']
room['overlook'].e_to = room['forest']
room['overlook'].u_to = room['peak']
room['peak'].d_to = room['overlook']
room['forest'].e_to = room['mangroves']
room['mangroves'].w_to = room['forest']
room['forest'].n_to = room['cave']
room['cave'].s_to = room['forest']
room['cave'].d_to = room['underground1']
room['underground1'].u_to = room['cave']
room['underground1'].e_to = room['tunnels']
room['tunnels'].w_to = room['underground1']
room['tunnels'].e_to = room['dragon']
room['dragon'].w_to = room['tunnels']
room['tunnels'].n_to = room['secret']
room['secret'].s_to = room['tunnels']
room['tunnels'].s_to = room['underground2']
room['underground2'].n_to = room['tunnels']
room['underground2'].u_to = room['swamp']
room['swamp'].d_to = room['underground2']
room['swamp'].n_to = room['mangroves']
room['mangroves'].s_to = room['swamp']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

newplayer = Player(room['village'])
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
    elif dir == "u":
        if hasattr(newplayer.room, "u_to"):
            newplayer.room = newplayer.room.u_to
        else:
            print("Sorry, you've hit a wall")
    elif dir == "d":
        if hasattr(newplayer.room, "d_to" ):
            newplayer.room = newplayer.room.d_to
        else: 
            print("Sorry, you've hit a wall")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    elif dir == "q":
        print("Thank you for playing!")
    else:
        print("\nInvalid selection.")
