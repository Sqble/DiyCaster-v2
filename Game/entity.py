from math import sin,cos,radians

class Entity:


    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.angle = a
        self.__calcSpeeds()


    def __calcSpeeds(self):
        speed = 2
        self.dx =  cos(radians(self.angle)) * speed
        self.dy = -sin(radians(self.angle)) * speed
    

    def coordIsWall(self,map,x,y):
        xi, yi = map.toIndex(x,y)
        return map.isWall(xi,yi)


    def moveForward(self,map):
        if not self.coordIsWall(map, self.x + self.dx, self.y):
            self.x += self.dx
        if not self.coordIsWall(map, self.x, self.y + self.dy):
            self.y += self.dy


    def moveBackward(self,map):
        if not self.coordIsWall(map, self.x - self.dx, self.y):
            self.x -= self.dx
        if not self.coordIsWall(map, self.x, self.y - self.dy):
            self.y -= self.dy
    

    def lookLeft(self):
        self.angle = (self.angle + 3) % 360
        self.__calcSpeeds()
    

    def lookRight(self):
        self.angle = (self.angle - 3) % 360
        self.__calcSpeeds()