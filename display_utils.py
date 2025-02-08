import pygame

def setup_scene():
    X = 600
    Y = 600
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('image')
    pygame.display.flip()   
    dirt = pygame.image.load("dirt.png").convert()
    grass = pygame.image.load("grass.png").convert()

    for i in range(16):
        x = (i-1)*40
        scrn.blit(dirt, (x, 320))
        scrn.blit(dirt, (x, 360))
        scrn.blit(dirt, (x, 400))
    for i in range(16):
        x = (i-1)*40
        scrn.blit(grass, (x, 280))
