# -*- coding: utf-8 -*-
import sys, pygame
from fontrenderer import FontRenderer
from logic import *
import constants as c


class GameScreen(object):
    def __init__(self, game):
        self.game = game

        self.sceneArea = pygame.Surface(SCENEAREA, pygame.HWSURFACE, 32)
        self.messageArea = pygame.Surface(MESSAGEAREA, pygame.HWSURFACE, 32)
        flags = pygame.HWSURFACE
        self.screen = pygame.display.set_mode(RESOLUTION, flags, 32)

        self.screen.blit(self.sceneArea, (0, 0))
        self.screen.blit(self.messageArea, (0, SCENEAREA[1]))
        self.screen.fill(cBlack)
        self.fontCache = FontRenderer()

    def createTileSurface(self, tile):
        s = pygame.Surface((TILESIZE, TILESIZE), pygame.HWSURFACE, 32)
        sText = self.fontCache.render(tile.char, tile.color)
        rectText = sText.get_rect()
        rectText.center = s.get_rect().center
        s.fill((tile.bgcolor))
        s.blit(sText, rectText)
        return s

    def drawTiles(self,screen, worldmap, cameraPosition):
        for row in xrange(len(worldmap)):
            for column in xrange(len(worldmap[0])):
                tile = worldmap[row][column]
                absolute_pos = self.getAbsolutposition(tile.position, cameraPosition)
                surfTile = self.createTileSurface(tile)
                screen.blit(surfTile, absolute_pos)

    def drawItems(self,screen, items,cameraPosition):
        if items:
            self.drawObject(screen,items,cameraPosition)

    def drawObject(self,screen,objToDisplay,cameraPosition):
        for obj in objToDisplay:
            s = pygame.Surface((TILESIZE, TILESIZE), pygame.HWSURFACE, 32)
            sText = self.fontCache.render(obj.char, obj.color)
            rectText = sText.get_rect()
            rectText.center = s.get_rect().center
            s.blit(sText, rectText)
            screen.blit(s, self.getAbsolutposition(obj.position, cameraPosition))

    def drawPlayers(self, screen, movingObj, player, cameraPosition):

        if len(movingObj) > 0:
            objToDisplay = movingObj[:]
            objToDisplay.append(player)
        else:
            objToDisplay = [player]

        self.drawObject(screen,objToDisplay,cameraPosition)


    def redraw(self):

        # redraw messageArea = Inventory / Message / etc.

        # redraw Tiles and Objects
        cameraPosition = self.game.player.position
        self.drawTiles(self.screen,self.game.worldmap, self.game.player.position)
        self.drawItems(self.screen,self.game.items, self.game.player.position)
        self.drawPlayers(self.screen, self.game.movingObject, self.game.player, cameraPosition)

    def getAbsolutposition(self, position, centerPosition):
        x, y = position
        ox,oy =  centerPosition
        return (x - ox + MAPWIDTH / 2) * TILESIZE, (y - oy + MAPHEIGHT / 2) * TILESIZE

