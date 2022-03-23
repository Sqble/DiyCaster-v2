from math import radians,sqrt,tan
from operator import index, indexOf
from Game.config import pygame,screen

class RayController:


    def castRays(player,map):

        rayX = RayX(player.x,player.y,player.angle)
        xDistance = rayX.fullCast(player,map)
        
        rayY = RayY(player.x,player.y,player.angle)
        yDistance = rayY.fullCast(player,map)

        if xDistance > yDistance:
            pygame.draw.line(screen, (255,0,0), (player.x, player.y), (rayY.x, rayY.y) )
        else:
            pygame.draw.line(screen, (0,0,255), (player.x, player.y), (rayX.x, rayX.y) )





class Ray:


    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.angle = angle


    def fullCast(self,player,map):
        if self.lookingStraight(): return 100000
        self.initCast(map.mapScale)
        self.castRay(map)
        return self.distance(player.x, player.y)


    def castRay(self,map):
        dist = 0
        while dist < map.mapX or dist < map.mapY:
            dist += 1
            x, y = map.toIndex(self.x,self.y)

            if map.inBounds(x,y) and map.findCoordinate(x,y) > 0:
                return
            else:
                self.move()


    def move(self):
        self.x += self.xOffset
        self.y += self.yOffset

    def distance(self,x,y):
        return sqrt( pow(self.x - x, 2) + pow(self.y - y, 2) )





class RayX(Ray):


    def __init__(self,x,y,angle):
        Ray.__init__(self,x,y,angle)


    def initCast(self,scale):
        xo = 1 / tan(radians(self.angle)) #UNSCALED X-OFFSET
        self.snapGrid(scale,xo)
        self.scaleOffset(scale,xo)
    

    def scaleOffset(self,scale,xo):
        if   self.lookingUp  (): direction =  scale
        elif self.lookingDown(): direction = -scale
        self.xOffset =  direction * xo
        self.yOffset = -direction
    

    def snapGrid(self,scale,xo):
        yo = self.y % scale
        indexOffset = 0
        if self.lookingDown(): yo -= scale
        if self.lookingUp  (): indexOffset = 0.0001
        self.y -= yo + indexOffset
        self.x += yo * xo


    def lookingStraight(self):
        return self.angle == 0 or self.angle == 180

    def lookingUp(self):
        return (0 < self.angle < 180)
    
    def lookingDown(self):
        return (180 < self.angle < 360)





class RayY(Ray):


    def __init__(self,x,y,angle):
        Ray.__init__(self,x,y,angle)


    def initCast(self,scale):
        yo = tan(radians(self.angle)) #UNSCALED Y-OFFSET
        self.snapGrid(scale,yo)
        self.scaleOffset(scale,yo)
    

    def scaleOffset(self,scale,yo):
        if   self.lookingRight(): direction = -scale
        elif self.lookingLeft (): direction =  scale
        self.xOffset = -direction
        self.yOffset =  direction * yo
    

    def snapGrid(self,scale,yo):
        xo = scale - self.x % scale
        indexOffset = 0
        if self.lookingLeft(): indexOffset = 0.0001; xo -= scale
        self.x += xo - indexOffset
        self.y -= xo * yo
        



    def lookingStraight(self):
        return self.angle == 90 or self.angle == 270

    def lookingLeft(self):
        return (90 < self.angle < 270)
        
    def lookingRight(self):
        return (270 < self.angle <= 360 or 0 <= self.angle < 90)