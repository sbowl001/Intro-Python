import crayons

class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description 
    
    def __str__(self):
        return self.name + ": " + self.description

    def grab_item(self, newplayer):
        print(crayons.blue("\n...grabbing" +"."))
        newplayer.room.items.remove(self)
        newplayer.items.append(self)

class Treasure(Item):
    def __init__( self, name, description, value):
        super().__init__(name, description)
        self.value = value 
        self.picked_up = False
    def grab_item(self, newplayer):
        super().grab_item(newplayer)
        if self.picked_up == False:
            newplayer.score += self.value
            self.picked_up = True
            
