from room import Room
from player import Player
from item import Item, Treasure

import crayons
# Declare all the rooms

room = {
    'village':  Room("Village Hidden in the Spring",
                     "The noise of bustling streets warms your heart", []),

    'home':    Room("Home Sweet Home", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Meal", "This item restores your health.")]),

    'attic': Room("Attic Room", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'forest':   Room("Grand Forest", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

   'overlook':   Room("Mountain Overlook", """A steep mountain appears before you. The forest expands in all directions. Perhaps a further look is needed...""", []),

   'peak':   Room("Mountain Peak", """The fresh air soothes your senses, the forest expanse looks peaceful. The village looks minute in the distance.""", []),

   'cave':   Room("North Cave", """Creaking sounds resonate throughout the cave.""", []),

   'underground1':   Room("Underground Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

   'tunnels':   Room("Dark Tunnels", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

   'secret':   Room("Secret Passage", """The passage holds an air of mystery. The walls glimmer with something hidden beneath.""", []),

   'epic':   Room("Epic Treasure", """The room contains the most special of treasure chests. Open it to reveal your prize.""", []),

   'underground2':   Room("Damp Underground Passage", """Moist droplets of water fall from the passage's crevices.""", []),

    'dragon': Room("Dragon Lair", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),

   'swamp':   Room("Sinister Swamp", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

   'mangroves':   Room("Mangrove Forest", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),
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

name = input('Enter your name: ')
newplayer = Player(name, room['village'], [])
cmd = ""
print(crayons.green(f'\n \t Welcome, {newplayer.name}!\n')) #crayons.green(


# Write a loop that:
#
while not cmd == "q":
    print(newplayer.room.name)
# * Prints the current room name
    print(newplayer.room.description)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    newplayer.room.view_items()
    cmd = input("\n Please choose a direction...n, s, e, w, OR q to quit the game.\n ").lower()
#
    parsed_cmd = cmd.split()
    if len(parsed_cmd) > 1:
        action = parsed_cmd[0]
        item = ""
        for i in range(1, len(parsed_cmd)):
            item += parsed_cmd[i] + " "  
        item = item.strip()# array of commands


        if action == "g" or action == "grab":
            for i in newplayer.room.items:
                if i.name.lower() == parsed_cmd[1]:
                    print("\n...grabbing" +".")
                    print(i)
                    newplayer.room.items.remove(i)
                    newplayer.items.append(i)
                    newplayer.score += i.value
                    # print("player items", newplayer.items[0].name)
                    print("player items", newplayer.items[0])
                else: 
                    print("\nitem not available to grab")
            for i in newplayer.room.items:
                print("after", i.name)
        elif action == "d" or action == "drop":
            print("checked", i, newplayer.items[0])
            for i in newplayer.items:
                if i.name.lower() == parsed_cmd[1]:
                     print("\t...dropping .")
                     newplayer.items.remove(i)
                     newplayer.room.items.append(i)   
                else:
                    print("item not available to drop!")

    else: #parsed_cmd length =1
# If the user enters a cardinal direction, attempt to move to the room there.
        if cmd == "n":
            if hasattr(newplayer.room, "n_to"):
                newplayer.room = newplayer.room.n_to
            else: 
                print("Sorry, you can't go that way")
        elif cmd == "score":
            # cmd = input( f'Score: {newplayer.score} \n')
            print( f'Score: {newplayer.score} \n')
        # elif cmd == "?"
        #     cmd = print_help()
        elif cmd == "i" or cmd =="inventory":
            if len(newplayer.items) == 0:
                print("Inventory is empty")
            else: 
                print("You are carrying: \n")
                for item in newplayer.items:
                    print("\t" + str(item))
        elif cmd == "s":
            if hasattr(newplayer.room, "s_to"):
                newplayer.room = newplayer.room.s_to
            else: 
                print("Sorry, you can't go that way")
        elif cmd == "w":
            if hasattr(newplayer.room, "w_to"):
                newplayer.room = newplayer.room.w_to
            else: 
                print("Sorry, you can't go that way")
        elif cmd == "e":
            if hasattr(newplayer.room, "e_to"):
                newplayer.room = newplayer.room.e_to
            else: 
                print("Sorry, you can't go that way")
        elif cmd == "u":
            if hasattr(newplayer.room, "u_to"):
                newplayer.room = newplayer.room.u_to
            else:
                print("Sorry, you can't go that way")
        elif cmd == "d":
            if hasattr(newplayer.room, "d_to" ):
                newplayer.room = newplayer.room.d_to
            else: 
                print("Sorry, you can't go that way")
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
        elif cmd == "q":
            print("Thank you for playing!")
        else:
            print("\nInvalid selection.")
