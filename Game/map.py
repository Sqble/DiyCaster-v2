

class Map:
    mapScale = 32

    def __init__(self,map,floor):
        self.map = map
        self.floor = floor
        self.mapY = len(map)
        self.mapX = len(map[0])

    
    def setMapScale(self,scale):
        self.mapScale = scale
    
    def isWall(self,x,y):
        return self.map[y][x] > 0

    def __call__(self,x,y):
        return self.map[y][x]

    def toIndex(self,x,y):
        return int(x - (x % 32)) // 32, int(y - (y % 32)) // 32
    
    def inBounds(self,x,y):
        return 0 <= x < self.mapX and 0 <= y < self.mapY

#0 = Empty
#1 = Stone Brick
#2 = Colorstone
#3 = Red Brick
#4 = mossy
#5 = Blue stone

map = Map([
    [1,1,1,1,1,1,1,1],
    [5,0,0,0,0,0,0,1],
    [5,0,0,0,3,0,0,4],
    [5,0,0,0,3,0,0,1],
    [5,0,0,0,3,0,0,4],
    [5,0,0,3,3,0,0,1],
    [5,0,0,0,0,0,0,4],
    [1,1,1,1,1,1,1,1]
],[
    [2,2,2,2,2,2,2,2],
    [2,1,1,1,2,2,2,2],
    [2,1,1,1,2,2,2,2],
    [2,1,1,1,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2]
])