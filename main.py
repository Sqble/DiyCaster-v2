from Game.config import pygame,const
from Game.debug import Draw2D
from Game.entity import Entity
from Game.ray import RayController
from Game.map import map
from Game.viewport3D import Viewport3D

clock = pygame.time.Clock()

player = Entity(49,48,330)

running = True
while running:
    clock.tick(const.FPS)

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.moveForward(map)
    if keys[pygame.K_s]: player.moveBackward(map)
    if keys[pygame.K_a]: player.lookLeft()
    if keys[pygame.K_d]: player.lookRight()

    #screen.fill((255,255,255))

    rays = RayController.radiateRayArray(player,map,60)
    Viewport3D.display(player, rays, map.mapScale)
    #print(clock.get_fps())



    #print(len(rays))
    #for ray in rays: Draw2D.drawRay(ray)
    #Draw2D.drawEntity(player)
    #Draw2D.drawMap(map)

    pygame.display.flip()
pygame.quit()