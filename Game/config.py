import pygame
pygame.init()

class const:
    WIDTH, HEIGHT, FPS = 640, 360, 60
    #WIDTH, HEIGHT, FPS = 500,500,60

    def findWidth(self):
        return self.WIDTH
    def findHeight(self):
        return self.HEIGHT

from pygame.locals import *
flags = SCALED
screen = pygame.display.set_mode( [const.WIDTH,const.HEIGHT], flags )
pygame.display.set_caption("DiyCaster")
