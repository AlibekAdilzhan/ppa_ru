import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

run = True
# Game loop.
while run:
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()