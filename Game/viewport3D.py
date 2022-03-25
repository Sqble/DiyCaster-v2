from Game.config import pygame,screen,const
from math import cos,radians


class Viewport3D:
    #x, y, startX, startY, angle, texture, type, distance

    def display(player,rays,scale,fov):
        xStep = const.WIDTH // fov

        Viewport3D.drawSky()
        Viewport3D.drawFloor()

        for i,ray in enumerate(rays):
            wallHeight = Viewport3D.calcWallHeight(scale, ray.distance, player.angle, ray.angle)

            lineOffset = Viewport3D.heightBeforeWall(wallHeight)
            
            color = Viewport3D.shade(ray.type)
            
            pygame.draw.rect(screen, color, pygame.Rect( (i * xStep, lineOffset), (xStep, wallHeight) ))
    


    def drawSky():
        pygame.draw.rect(screen, (173,216,230), pygame.Rect( (0,0), (const.WIDTH, const.HEIGHT // 2) ))
    
    def drawFloor():
        pygame.draw.rect(screen, (100,100,100), pygame.Rect( (0, const.HEIGHT // 2), (const.WIDTH, const.HEIGHT) ))
    
    def removeFisheye(distance,angle1, angle2):
        return distance * cos(radians(angle1 - angle2))
    
    def calcWallHeight(scale, distance, angle1, angle2):
        distance = Viewport3D.removeFisheye(distance, angle1, angle2)
        wallHeight = int(scale * const.HEIGHT / (distance+0.0001) )
        if wallHeight > const.HEIGHT: wallHeight = const.HEIGHT
        return wallHeight

    def heightBeforeWall(wallHeight):
        return const.HEIGHT / 2 - wallHeight/2
    
    def shade(rayType):
        return (0,255,0) if rayType == 'x' else (0,200,0)