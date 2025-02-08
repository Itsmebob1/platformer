import pygame
import display_utils

pygame.init()

X = 600
Y = 600
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')
pygame.display.flip()
dirt = pygame.image.load("dirt.png").convert()
grass = pygame.image.load("grass.png").convert()

# paint screen one time
status = True

while (status):
    for i in range(16):
        x = (i-1)*40
        scrn.blit(dirt, (x, 320))
        scrn.blit(dirt, (x, 360))
        scrn.blit(dirt, (x, 400))
    for i in range(16):
        x = (i-1)*40
        scrn.blit(grass, (x, 280))
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()