import pygame
import time
 
pygame.init()

class Figure: # class for figures
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.interval = 0.2

    def update(self): # to move a figure
        global start_time
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN] == True:
            self.interval = 0.05
        else:
            self.interval = 0.3
        if time.time() - start_time > self.interval:
            start_time = time.time()
            self.y = self.y + bs
        
        

fps = 60
clock = pygame.time.Clock()
 
width, height = 352, 480
screen = pygame.display.set_mode((width, height))

#game settings
bs = 32

figure = Figure(3 * bs, 0)

shape = [(0, 0), (1, 0), (1, 1), (2, 1)]
busy_cells = []
for i in range(width // bs):
    busy_cells.append((i * bs, height))

run = True
# Game loop.
start_time = time.time()
while run:
    screen.fill((255, 255, 255))
    future_x = figure.x
    future_y = figure.y
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                figure.x = figure.x - bs
            elif event.key == pygame.K_RIGHT:
                figure.x = figure.x + bs
            elif event.key == pygame.K_SPACE: 
                end_while = True
                while end_while:
                    # print("sdfsdf")
                    for t in shape:
                        for c in busy_cells:
                            if future_y + t[1] * bs == c[1] - bs and future_x + t[0] * bs == c[0]:
                                new_busy_celss = [(future_x + r[0] * bs, future_y + r[1] * bs) for r in shape]
                                busy_cells.extend(new_busy_celss)
                                figure = Figure(3 * bs, 0)
                                end_while = False
                                break
                        if end_while == False:
                            break
                    future_y = future_y + bs
                    # if future_y < 500:
                    #     print(future_y + t[1] * bs, c[0], c[1])
    figure.update()
    # pygame.draw.rect(screen, (255, 255, 0), figure.y + t[1] * bs == c[1] - bs)
    for t in shape:
        for c in busy_cells:
            if figure.y + t[1] * bs == c[1] - bs and figure.x + t[0] * bs == c[0]:
                new_busy_celss = [(figure.x + r[0] * bs, figure.y + r[1] * bs) for r in shape]
                busy_cells.extend(new_busy_celss)
                figure = Figure(3 * bs, 0)
                break
    for i in range(height // bs):
        pygame.draw.line(screen, (0, 0, 0), (0, i * bs), (width, i * bs)) # horizontal lines 
    for i in range(width // bs):
        pygame.draw.line(screen, (0, 0, 0), (i * bs, 0), (i * bs, height))
    for t in shape:
        pygame.draw.rect(screen, (0, 0, 0), (figure.x + t[0] * bs, figure.y + t[1] * bs, bs, bs))
    for c in busy_cells:
        pygame.draw.rect(screen, (0, 0, 0), (c[0], c[1], bs, bs))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()