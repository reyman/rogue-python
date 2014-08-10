# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:52:20 2012

@author: srey
"""

import random
from objects import Items,NPC,Player
import sys, pygame
from constants import *

class GameLogic(object):
    def __init__(self, worldmap):
        self.worldmap = worldmap
        # init player
        self.player = Player( "hero", (23,39), "@", (255, 255, 255),self)
        self.movingObject = []
        #used for display only
        self.items = []

        # init items
        self.placeItems()
        self.placeNPC()

    def placeNPC(self):
        oneNPC = NPC( "hero", (24,36), "@", (120, 200, 200),self)
        self.addMovingObject(oneNPC)

    def placeItems(self):
        posItem1 = (22,39)
        item1 = Items("epée de bois", posItem1, "i", (120, 200, 100) )
        self.getTile(posItem1).addItem(item1)
        self.addItems(item1)

    def removeItems(self,item):
        if item in self.items:
            self.items.remove(item)

    def addItems(self,item):
        self.items.append(item)


    def addMovingObject(self,object):
        self.movingObject.append(object)

    def removeMovingObject(self,object):
        if object in self.movingObject:
            self.movingObject.remove(object)

    def getTile(self,(x,y)):
        return self.worldmap[y][x]

    def getRandomLocalTile(self,(x,y)):
        neigbors = []
        if x-1 >= 0 :
            neigbors.append((-1,0))
        if x+1 <= len(self.worldmap) :
            neigbors.append((1,0))
        if y-1 >=0  :
            neigbors.append((0,-1))
        if y+1 <= len(self.worldmap) :
            neigbors.append((0,1))

        return neigbors

    # add and/or remove player from tiles ...
    def movePlayer(self,dx,dy):
        # move if i can
        if not self.isBlocked((dx,dy), self.player):
                self.player.move((dx, dy))

        # decision with npc, with or without move
        for obj in self.movingObject:
            print obj.position ," / " ,self.player.position
            if obj.position == self.player.position:
                self.player.collide(obj)

        # list items on tiles, with or without move
        tileOntoPlayer = self.getTile(self.player.position)
        if len(tileOntoPlayer.items) > 0:
            for i in tileOntoPlayer.items:
                print "Item > ", i.name

    def moveNpc(self):
        for objToMove in self.movingObject:
            listOfNeigboors = self.getRandomLocalTile(objToMove.position)
            random.shuffle(listOfNeigboors)
            for n in listOfNeigboors:
                if self.isBlocked(n, objToMove) == False:
                    objToMove.move(n)
                    break

    def aiTurn(self):
        self.moveNpc()

    def isBlocked(self,pos, objectToMove):
        x,y = objectToMove.position
        dx,dy = pos
        tileToTest = self.getTile((x + dx, y + dy))
        #test tile block (door,etc.)
        if tileToTest.blocked == False:
            return False
        else:
            return True






        
	

		
