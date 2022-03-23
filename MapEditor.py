import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


mapSize = 8
map = [[0 for _ in range(mapSize)] for _ in range(mapSize)]

colors = [
    (0,0,0),
    (255,0,0),
    (0,255,255)
]

map[1][2] = 2
map[3][0] = 1

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        
        screen.fill((255,255,255))

        drawGrid(20,340)
        

        pygame.display.flip()
    pygame.quit()



def isOver(rect,pos):
    return True if rect.collidepoint(pos[0],pos[1]) else False


def drawGrid(start,end):
    scale = (end - start) // mapSize
    for y in range(mapSize):
        for x in range(mapSize):
            square = map[y][x]
            width = 2
            if square > 0:
                width = 0
            

            color = colors[square]

            squareRect = pygame.Rect( (start + x * scale, start + y * scale), (scale,scale) )
            pos = pygame.mouse.get_pos()
            left,middle,right = pygame.mouse.get_pressed()
            if isOver(squareRect,pos) and left: map[y][x] = 1
            pygame.draw.rect(screen,color,squareRect, width)
    




if __name__ == "__main__":
    main()