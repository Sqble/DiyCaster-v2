from Game.config import pygame,screen,const
from math import cos,radians


class Viewport3D:
    #x, y, startX, startY, angle, texture, type, distance

    def display(player,rays,scale,fov):
        xStep = const.WIDTH // fov


        pygame.draw.rect(screen, (173,216,230), pygame.Rect( (0,0), (const.WIDTH, const.HEIGHT // 2) ))

        pygame.draw.rect(screen, (100,100,100), pygame.Rect( (0, const.HEIGHT // 2), (const.WIDTH, const.HEIGHT) ))

        for i,ray in enumerate(rays):
            distance = ray.distance * cos(radians(player.angle - ray.angle))
            lineHeight = int(scale * const.HEIGHT / (distance+0.0001) )
            if lineHeight > const.HEIGHT: lineHeight = const.HEIGHT

            lineOffset = const.HEIGHT / 2 - lineHeight/2
            
            color = (0,255,0) if ray.type == 'x' else (0,200,0)
            pygame.draw.rect(screen, color, pygame.Rect( (i * xStep, lineOffset), (xStep, lineHeight) ))