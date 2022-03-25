

class Map:
    mapScale = 32

    def __init__(self,map):
        self.map = map
        self.mapY = len(map)
        self.mapX = len(map[0])

    
    def setMapScale(self,scale):
        self.mapScale = scale
    
    def isWall(self,x,y):
        return self.map[y][x] > 0

    def __call__(self,x,y):
        return self.map[y][x]

    def toIndex(self,x,y):
        return int(x - (x % self.mapScale)) // self.mapScale, int(y - (y % self.mapScale)) // self.mapScale
    
    def inBounds(self,x,y):
        return 0 <= x < self.mapX and 0 <= y < self.mapY


map = Map([
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
])