from math import sin,cos,radians

class Entity:


    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.angle = a
        self.__calcSpeeds()


    def __calcSpeeds(self):
        speed = 70
        self.dx =  cos(radians(self.angle)) * speed
        self.dy = -sin(radians(self.angle)) * speed
    

    def coordIsWall(self,map,x,y):
        xi, yi = map.toIndex(x,y)
        return map.isWall(xi,yi)


    def moveForward(self,map,dt):
        if not self.coordIsWall(map, self.x + self.dx * dt, self.y):
            self.x += self.dx * dt
        if not self.coordIsWall(map, self.x, self.y + self.dy * dt):
            self.y += self.dy * dt


    def moveBackward(self,map,dt):
        if not self.coordIsWall(map, self.x - self.dx * dt, self.y):
            self.x -= self.dx * dt
        if not self.coordIsWall(map, self.x, self.y - self.dy * dt):
            self.y -= self.dy * dt
    

    def lookLeft(self,dt):
        self.angle = (self.angle + 90 * dt) % 360
        self.__calcSpeeds()
    

    def lookRight(self,dt):
        self.angle = (self.angle - 90 * dt) % 360
        self.__calcSpeeds()