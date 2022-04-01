from Game.config import pygame,const
from Game.debug import Draw2D
from Game.entity import Entity
from Game.ray import RayController
from Game.map import map
from Game.viewport3D import Viewport3D


clock = pygame.time.Clock()

player = Entity(89,88,60)

running = True
while running:
    dt = clock.tick(40) / 1000

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.moveForward(map,dt)
    if keys[pygame.K_s]: player.moveBackward(map,dt)
    if keys[pygame.K_a]: player.lookLeft(dt)
    if keys[pygame.K_d]: player.lookRight(dt)

    #screen.fill((255,255,255))

    rays = RayController.radiateRayArray(player,map,60)
    Viewport3D.display(player, rays, map)
    #print(clock.get_fps())



    #print(len(rays))
    #for ray in rays: Draw2D.drawRay(ray)
    #Draw2D.drawEntity(player)
    #Draw2D.drawMap(map)

    pygame.display.flip()
pygame.quit()