import pygame
pygame.init()

class const:
    WIDTH, HEIGHT, FPS = 640, 360, 40
    #WIDTH, HEIGHT, FPS = 500,500,60

    def findWidth(self):
        return self.WIDTH
    def findHeight(self):
        return self.HEIGHT

from pygame.locals import *

flags = SCALED #| DOUBLEBUF
screen = pygame.display.set_mode( [const.WIDTH,const.HEIGHT], flags )
screen.set_alpha(None)
pygame.display.set_caption("DiyCaster")
background = pygame.Surface((const.WIDTH,const.HEIGHT))