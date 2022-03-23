from Game.config import pygame,screen,const

class Draw2D:


    def drawEntity(entity):
        color = (255,0,0)
        size = 6
        #Draw Entity
        entityRect = pygame.Rect( (entity.x - size, entity.y - size), (size * 2, size * 2) )
        pygame.draw.rect(screen, color, entityRect)
        #Draw dx,dy
        startPos = (entity.x               , entity.y               )
        endPos   = (entity.x + entity.dx * 8, entity.y + entity.dy * 8)
        pygame.draw.line(screen, color, startPos, endPos, 2)
    

    def drawMap(map):
        scale = map.mapScale
        for y in range(map.mapY):
            for x in range(map.mapX):
                square = map.findCoordinate(x,y)
                if square > 0:
                    squareRect = pygame.Rect( (x * scale + 1, y * scale + 1), (scale - 1,scale - 1) )
                    pygame.draw.rect(screen,(100,100,100),squareRect)