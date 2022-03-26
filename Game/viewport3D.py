from Game.config import pygame,screen,const,background
from math import cos,sin,radians
from Game.textures import colors, textures




planeDistance = 554.2562

class Viewport3D:
    #Ray variables: x, y, startX, startY, angle, texture, type, distance

    def display(player,rays,scale):
        xStep = const.WIDTH // len(rays)

        Viewport3D.drawSky()
        #Viewport3D.drawFloor()

        for i,ray in enumerate(rays):
            wallHeight = Viewport3D.calcWallHeight(scale, ray.distance, player.angle, ray.angle)
            yStep = wallHeight / 32

            lineOffset = Viewport3D.heightBeforeWall(wallHeight)
            
            textureX = Viewport3D.findTextureX(ray)

            if wallHeight > const.HEIGHT: wallHeight = const.HEIGHT

            #Draw Wall
            for textureY in range(0,32):
                color = colors[ textures[ray.texture] [textureY][textureX] ]
                color = Viewport3D.shade(ray.type, color)

                pygame.draw.rect(background, color, pygame.Rect( (i * xStep, textureY * yStep + lineOffset), (xStep, yStep + 1) ) )
                
                #drawX = (i * xStep) + (xStep // 2)
                #drawY = textureY * yStep + lineOffset
                #pygame.draw.line(screen,color, (drawX, drawY), (drawX, drawY + yStep), xStep)
            
            
            #Draw Floor
            if wallHeight != const.HEIGHT:
                for y_pixel in range(int(lineOffset + wallHeight)+2 ,const.HEIGHT): 
                    dy = y_pixel - const.HEIGHT/2

                    d = planeDistance * 10 / dy / cos(radians(player.angle - ray.angle + 0.0001))
                    tx = int(player.x + cos(radians(ray.angle)) * d)
                    ty = int(player.y - sin(radians(ray.angle)) * d)

                    color = colors[ textures[2] [ty%32][tx%32] ]


                    pygame.draw.line(background, color, (i*xStep, y_pixel), (i*xStep+xStep, y_pixel))
                #pygame.draw.line(background, (100,100,100), (i*xStep, const.HEIGHT-1), (i*xStep+xStep, const.HEIGHT-1), 3)


        screen.blit(background,(0,0))
    


    def drawSky():
        pygame.draw.rect(background, (173,216,230), pygame.Rect( (0,0), (const.WIDTH, const.HEIGHT // 2) ))
    
    def drawFloor():
        pygame.draw.rect(background, (255,255,255), pygame.Rect( (0, const.HEIGHT // 2), (const.WIDTH, const.HEIGHT) ))
    
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


