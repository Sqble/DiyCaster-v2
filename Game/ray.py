from math import radians,sqrt,tan

def floatRange(start,stop,step):
    y = start
    while y >= stop:
        yield y
        y+=step

class RayController:


    def cast_XY_Rays(player,map,angle):

        rayX = RayX(player.x,player.y,angle)
        xDistance = rayX.fullCast(player,map)
        
        rayY = RayY(player.x,player.y,angle)
        yDistance = rayY.fullCast(player,map)

        if xDistance > yDistance:
            rayY.distance = yDistance
            return rayY
        else:
            rayX.distance = xDistance
            return rayX
    

    def radiateRayArray(player,map,fov):
        finalRays = []
        startAngle = player.angle + (fov // 2) + 360
        endAngle   = player.angle - (fov // 2) + 360
        for angle in floatRange(startAngle,endAngle, - (fov / 319.5) ): #-0.47244 -0.18808
        #for angle in range(startAngle, endAngle, -1): 
            angle %= 360
            finalRays.append(RayController.cast_XY_Rays(player,map,angle))
        return finalRays




#x, y, startX, startY, angle, texture, type, distance
class Ray:


    def __init__(self,x,y,angle):
        self.x = self.startX = x
        self.y = self.startY = y
        self.angle = angle
    
    def __call__(self):
        return self.x, self.y


    def fullCast(self,player,map):
        if self.lookingStraight(): return 100000
        offset = self.prepareOffset()
        self.snapGrid(map.mapScale,offset)
        self.scaleOffset(map.mapScale,offset)
        self.texture = self.castRay(map)

        del self.xOffset, self.yOffset
        return self.distance(player.x, player.y)


    def castRay(self,map):
        dist = 0
        while dist < map.mapX or dist < map.mapY:
            dist += 1
            x, y = map.toIndex(self.x,self.y)

            if map.inBounds(x,y) and map(x,y) > 0:
                return map(x,y)
            else:
                self.move()


    def move(self):
        self.x += self.xOffset
        self.y += self.yOffset

    def distance(self,x,y):
        return sqrt( pow(self.x - x, 2) + pow(self.y - y, 2) )
    
    def origin(self):
        return self.startX, self.startY





class RayX(Ray):


    def __init__(self,x,y,angle):
        self.type = "x"
        Ray.__init__(self,x,y,angle)
    

    def scaleOffset(self,scale,xo):
        if   self.lookingUp  (): direction =  scale
        elif self.lookingDown(): direction = -scale
        self.xOffset =  direction * xo
        self.yOffset = -direction
    

    def snapGrid(self,scale,xo):
        yo = self.y % scale
        indexOffset = 0
        if self.lookingDown(): yo -= scale
        elif self.lookingUp(): indexOffset = 0.0001
        self.y -= yo + indexOffset
        self.x += yo * xo




    def lookingStraight(self):
        return self.angle == 0 or self.angle == 180

    def lookingUp(self):
        return (0 < self.angle < 180)
    
    def lookingDown(self):
        return (180 < self.angle < 360)

    def prepareOffset(self):
        return 1 / tan(radians(self.angle)) #UNSCALED X-OFFSET





class RayY(Ray):


    def __init__(self,x,y,angle):
        self.type = "y"
        Ray.__init__(self,x,y,angle)
    

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

    def prepareOffset(self):
        return tan(radians(self.angle)) #UNSCALED Y-OFFSET