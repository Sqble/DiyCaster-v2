from Game.config import pygame,screen,const,background
from math import cos,sin,radians
from Game.textures import textures


planeDistance = 831.38438#554.2562
shadeLUT = {}

class Viewport3D:
    #Ray variables: x, y, startX, startY, angle, texture, type, distance

    def display(player,rays,map):
        xStep = const.WIDTH // len(rays)

        for i,ray in enumerate(rays):
            wallHeight = Viewport3D.calcWallHeight(map.mapScale, ray.distance, player.angle, ray.angle)
            yStep = wallHeight / 32

            lineOffset = Viewport3D.heightBeforeWall(wallHeight)
            
            textureX = Viewport3D.findTextureX(ray)

            if wallHeight > const.HEIGHT: wallHeight = const.HEIGHT

            #Draw Wall
            for textureY in range(0,32):
                color = textures[ray.texture] [textureY * 32 + textureX]
                color = Viewport3D.shade(ray.type, color)

                pygame.draw.rect(background, color, pygame.Rect( (i * xStep, textureY * yStep + lineOffset), (xStep, yStep + 1) ) )
                
            
            #Draw Floor and ceiling
            #I would make this look nice but im scared it will break...
            #EXTREMELY crucial it runs as fast as possible because this gets run tens of thousands of times per frame
            if wallHeight != const.HEIGHT:
                beta = cos(radians(player.angle - ray.angle + 0.0001))
                coss = cos(radians(ray.angle))
                sinn = sin(radians(ray.angle))
                realPlaneDistance = 10 * planeDistance / beta
                step = i*xStep
                for y_pixel in range( int(lineOffset + wallHeight)+1 ,const.HEIGHT, 2): 
                    
                    d =  realPlaneDistance / (y_pixel - 270) #270 is half of the screen height
                    tx = int(player.x + coss * d)
                    ty = int(player.y - sinn * d)

                    color = textures[ map.floor[ty >> 6 - 1][tx >> 6 - 1] ] [(ty&31) * 32 + (tx&31)] #if it works dont touch it
                    
                    pygame.draw.line(background, color, (step,       y_pixel), (step+xStep,       y_pixel), 2)
                    pygame.draw.line(background, color, (step, 540 - y_pixel), (step+xStep, 540 - y_pixel), 2)
            

        screen.blit(background,(0,0))
    

    def drawSky():
        pygame.draw.rect(background, (173,216,230), pygame.Rect( (0,0), (const.WIDTH, const.HEIGHT // 2 - 10) ))
    
    def drawFloor():
        pygame.draw.rect(background, (0,0,0), pygame.Rect( (0, const.HEIGHT // 2 + 10), (const.WIDTH, 260) ))
    
    def removeFisheye(distance,angle1, angle2):
        return distance * cos(radians(angle1 - angle2))
    
    def heightBeforeWall(wallHeight):
        return (const.HEIGHT - wallHeight) / 2
    
    def shade(rayType, color):
        newColor = (int(color[0] * 0.7), int(color[1] * 0.7), int(color[2] * 0.7))
        return color if rayType == 'x' else newColor

    def calcWallHeight(scale, distance, angle1, angle2):
        distance = Viewport3D.removeFisheye(distance, angle1, angle2)
        wallHeight = int(32 * const.HEIGHT / (distance+0.0001) )
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
