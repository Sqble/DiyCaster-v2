import pygame
pygame.init()

class const:
    WIDTH, HEIGHT, FPS = 1280, 720, 60
    #WIDTH, HEIGHT, FPS = 500,500,60

    def findWidth(self):
        return self.WIDTH
    def findHeight(self):
        return self.HEIGHT


screen = pygame.display.set_mode( [const.WIDTH,const.HEIGHT] )
pygame.display.set_caption("DiyCaster")
