from Game.config import pygame,screen,const
from math import cos,radians
from Game.textures import colors, textures

class Viewport3D:
    #Ray variables: x, y, startX, startY, angle, texture, type, distance

    def display(player,rays,scale):
        xStep = const.WIDTH // len(rays)

        Viewport3D.drawSky()
        Viewport3D.drawFloor()

        for i,ray in enumerate(rays):
            wallHeight = Viewport3D.calcWallHeight(scale, ray.distance, player.angle, ray.angle)
            yStep = wallHeight / 32

            lineOffset = Viewport3D.heightBeforeWall(wallHeight)
            
            textureX = Viewport3D.findTextureX(ray)

            if wallHeight > const.HEIGHT: wallHeight = const.HEIGHT

            for textureY in range(0,32):
                color = colors[ textures[ray.texture] [textureY][textureX] ]
                color = Viewport3D.shade(ray.type, color)

                pygame.draw.rect(screen, color, pygame.Rect( (i * xStep, textureY * yStep + lineOffset), (xStep, yStep + 1) ))
    


    def drawSky():
        pygame.draw.rect(screen, (173,216,230), pygame.Rect( (0,0), (const.WIDTH, const.HEIGHT // 2) ))
    
    def drawFloor():
        pygame.draw.rect(screen, (100,100,100), pygame.Rect( (0, const.HEIGHT // 2), (const.WIDTH, const.HEIGHT) ))
    
    def removeFisheye(distance,angle1, angle2):
        return distance * cos(radians(angle1 - angle2))
    
    def heightBeforeWall(wallHeight):
        return const.HEIGHT / 2 - wallHeight/2
    
    def shade(rayType, color):
        newColor = (int(color[0] * 0.7), int(color[1] * 0.7), int(color[2] * 0.7))
        return color if rayType == 'x' else newColor

    def calcWallHeight(scale, distance, angle1, angle2):
        distance = Viewport3D.removeFisheye(distance, angle1, angle2)
        wallHeight = int(scale * const.HEIGHT / (distance+0.0001) )
        return wallHeight
    
    def findTextureX(ray):
        if ray.type == 'x':
            x = int(ray.x) % 32
            if ray.lookingDown():
                x = 31-x
        if ray.type == 'y':
            x = int(ray.y) % 32
            if ray.lookingLeft():
                x = 31-x
        return x