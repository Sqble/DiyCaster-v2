from Game.config import pygame,screen,const,background
from math import cos,sin,radians
from Game.textures import colors, textures

#from numpy import cos


planeDistance = 554.2562
shadeLUT = {}

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

            #Draw Wall
            for textureY in range(0,32):
                color = colors[ textures[ray.texture] [textureY][textureX] ]
                color = Viewport3D.shade(ray.type, color)

                pygame.draw.rect(background, color, pygame.Rect( (i * xStep, textureY * yStep + lineOffset), (xStep, yStep + 1) ) )
                
                #drawX = (i * xStep) + (xStep // 2)
                #drawY = textureY * yStep + lineOffset
                #pygame.draw.line(screen,color, (drawX, drawY), (drawX, drawY + yStep), xStep)
            
            
            #Draw Floor and ceiling
            #I would make this look nice but im scared it will break...
            #EXTREMELY crucial it stays exactly like this because this gets run 16000 times a frame
            if wallHeight != const.HEIGHT:
                beta = cos(radians(player.angle - ray.angle + 0.0001))
                coss = cos(radians(ray.angle))
                sinn = sin(radians(ray.angle))
                realPlaneDistance = planeDistance * 10 / beta
                for y_pixel in range( max(int(lineOffset + wallHeight)+1,261) ,const.HEIGHT, 2): 
                    
                    d =  realPlaneDistance / (y_pixel - 180)
                    tx = int(player.x + coss * d) % 32
                    ty = int(player.y - sinn * d) % 32

                    color = colors[ textures[2] [ty][tx] ]
                    shade = Viewport3D.shadeLUT(y_pixel)
                    color = ( color[0] * shade, color[1] * shade, color[2] * shade)

                    pygame.draw.line(background, color, (i*xStep, y_pixel), (i*xStep+xStep, y_pixel),2 )
                    pygame.draw.line(background, color, (i*xStep, 360 - y_pixel), (i*xStep+xStep, 360 - y_pixel),2 )
                    


        screen.blit(background,(0,0))
    

    def shadeLUT(y_pixel):
        if y_pixel not in shadeLUT:
            shadeLUT[y_pixel] = min( 1, ((y_pixel - 260) / 60)**2 )
        return shadeLUT[y_pixel]

    def drawSky(): #(173,216,230)
        pygame.draw.rect(background, (0,0,0), pygame.Rect( (0,100), (const.WIDTH, const.HEIGHT // 2 - 10) ))
    
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


