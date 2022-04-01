from Game.config import pygame,screen

class Draw2D:


    def drawEntity(entity):
        color = (255,0,0)
        size = 6
        #Draw Entity
        entityRect = pygame.Rect( (entity.x - size, entity.y - size), (size * 2, size * 2) )
        pygame.draw.rect(screen, color, entityRect)
        #Draw dx,dy
        startPos = (entity.x            , entity.y            )
        endPos   = (entity.x + entity.dx, entity.y + entity.dy)
        pygame.draw.line(screen, color, startPos, endPos, 2)
    

    def drawMap(map):
        scale = map.mapScale
        for y in range(map.mapY):
            for x in range(map.mapX):
                square = map(x,y)
                if square > 0:
                    squareRect = pygame.Rect( (x * scale + 1, y * scale + 1), (scale - 1,scale - 1) )
                    pygame.draw.rect(screen,(100,100,100),squareRect)
    

    def drawRay(ray):
        color = (255,0,0) if ray.type == "x" else (0,0,255)
        pygame.draw.line(screen, color, ray.origin(), ray() )