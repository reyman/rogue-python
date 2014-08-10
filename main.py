# -*- coding: utf-8 -*-

import sys, pygame
from pygame.constants import *
from constants import *
from logic import *
from map import *
from screen import GameScreen


class Game(object):

    def __init__(self):

        pygame.init()
        #screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)


        self.gameLogic = GameLogic(self.load(mapOfWorld))

        self.screenLogic = GameScreen(self.gameLogic)

    def load(self, mymap):
        tileMap = []
        x, y = (0,0)
        for line in mymap:
            tileLine = []
            for value in line:

                try:
                    tile = tilesObject[value]
                except KeyError:
                    return "Error on key"
                    # problem due to DOOR and polymorphism ... :/
                #print tile["bgcolor"]
                obj = tile['cls'] (char = value , position = (x,y), **tile ['args'] )

                #obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],  bgcolor=tile["bgcolor"])
                x += 1
                tileLine.append(obj)
            x = 0
            y += 1
            tileMap.append(tileLine)
        return tileMap

    def handle_event(self):

        event = pygame.event.wait()

        if event.type == KEYDOWN:
            key = event.key
            if key == K_UP:
                self.gameLogic.movePlayer(0, -1)
            elif key == K_RIGHT:
                self.gameLogic.movePlayer(1, 0)
            elif key == K_DOWN:
                self.gameLogic.movePlayer(0, 1)
            elif key == K_LEFT:
                self.gameLogic.movePlayer(-1, 0)
            else:
                if key == K_i:
                    print "gestion inventaire"
                elif key == K_e:
                    self.gameLogic.player.take()

                return "notEndOfTurn"

        elif event.type == QUIT:
                    return "endOfGame"

    def run(self):

        state=None
        pygame.event.set_allowed(None)
        pygame.event.set_allowed([KEYDOWN,QUIT])
        count = 0
        while state != "endOfGame":

            # redraw screen
            self.screenLogic.redraw()
            pygame.display.update()
            self.clock.tick(60)

            # state ?
            state = self.handle_event()

            if state != "notEndOfTurn":
                # ai Turn
                self.gameLogic.aiTurn()

            count +=1
            #pygame.display.flip()

        pygame.quit()

clear = lambda: os.system('clear')

if __name__ == "__main__":
    Game().run()
    pygame.quit()