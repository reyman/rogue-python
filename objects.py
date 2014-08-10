# -*- coding: utf-8 -*-

#################
# CLASSE PARENTE DE TOUT LES OBJETS DU JEU
#################
class GameObject(object):
    def __init__(self, name, position ,char,color):
        self.name = name
        self.position = position
        self.in_FOV = False
        self.color = color
        self.char = char


#################
# ITEMS
#################

#################
# ACTEURS
#################

class Actor(GameObject):
    def __init__(self, name, position, char, color, game):
        super(Actor, self).__init__(name, position, char, color)
        self.items = []
        self.game = game

    def addItem(self,item):
        self.items.append(item)

    def dropItem(self,object):
        try:
            self.items.remove(object)
        except ValueError:
            pass

    def move(self, (dx, dy)):
        x, y = self.position
        self.position = (dx + x, dy + y)

class Player(Actor):
    def __init__(self, name, position, char, color,game):
       super(Player, self).__init__( name, position, char, color,game)

    def take(self):
        listItems= self.game.getTile(self.position).items
        if listItems:
            lastitem = listItems.pop()
            if hasattr(lastitem,"catch"):
                # call catch item
                item = lastitem.catch(self)
                #add item returned to my list
                self.addItem(item)
                # remove item from display list into game logic
                self.game.removeItems(lastitem)

    def collide(self, object):

        if hasattr(object,"talk"):
            print object.talk()

        if hasattr(object,"attaque"):
            print "attaque  !"
            #remove dead monster of tile ...


class NPC(Actor):
    def __init__(self, name, position, char, color,game):
       super(NPC, self).__init__( name, position, char, color, game)

    def talk(self):
        print "Bonjour ! "

class Monster(Actor):
    def __init__(self, name, position, char, color):
       super(Monster, self).__init__( name, position, char, color)

    def attack(self, ennemi):
        print "Attaque "

#################
# ITEMS
#################
class Items(GameObject):
    def __init__(self, name, position, char, color, owner = None):
       super(Items, self).__init__( name, position, char, color)
       self.owner= owner

       if self.owner:
           if hasattr(self.owner,"addItem"):
               self.owner.addItem(self)

    def catch(self,objectWhichTake):
        if self.owner:
            if hasattr(self.owner,"dropItem"):
                # find and remove me from owner (tile or other)
                self.owner.dropItem(self)
                self.owner = objectWhichTake
                return self
        return None

    def use(self):
        print "use"

#################
# TYPE DE TUILES
#################
class Tile(GameObject):
    def __init__(self, name, position, char, color, blocked, bgcolor):
        super(Tile, self).__init__(name, position, char, color)
        self.bgcolor = bgcolor
        self.blocked = blocked
        # liste contenant les possibles autres objets
        self.items = []

    def addItem(self,item):
        self.items.append(item)

    def dropItem(self,object):
        try:
            self.items.remove(object)
        except ValueError:
            pass

class Floor(Tile):
    def __init__(self, name, position, char, color=(255, 255, 255), blocked=False, bgcolor=(0, 0, 0)):
        super(Floor, self).__init__(name, position, char, color, blocked, bgcolor)
        self.objects = []

# Other composition to do here
class Door(Tile):
    def __init__(self, key, name, position, char, color=(255, 255, 255), bgcolor=(0, 0, 0), blocked=False, state=False):
        super(Door, self).__init__(name, position, char, color, blocked, bgcolor)
        self.state = state
        self.key = key

    def opening(self, key):
        if self.key == key:
            self.state = True