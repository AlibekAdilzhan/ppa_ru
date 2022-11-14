import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()
 
# game settings
block_size = 64

width, height = 640, 700
screen = pygame.display.set_mode((width, height))

snowman = pygame.image.load("SnowMan1_right.png")
snowman = pygame.transform.scale(snowman, (block_size, block_size))
enemy = pygame.image.load("stay_right.png")
enemy = pygame.transform.scale(enemy, (block_size, block_size))
block = pygame.image.load("mario_block.png")
block = pygame.transform.scale(block, (block_size, block_size))

game_map = [
    ".................................................",
    ".................................................",
    ".................................................",
    ".................................................",
    ".................................................",
    "...bbbbb..........................................",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
]

hero_x = 50
hero_y = 50
hero_old_x = hero_x
hero_old_y = hero_y
enemy_x = 300
enemy_y = 50
enemy_old_x = enemy_x
enemy_old_y = enemy_y
h_speed = 10
h_speed_enemy = 2
v_speed = 0
v_speed_enemy = 0
g = 2
can_jump = False
can_jump_enemy = False

hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
enemy_rect = pygame.Rect(enemy_x, enemy_y, block_size, block_size)

rects = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)

run = True
# Game loop.
while run:
    screen.fill((50, 200, 255))
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and can_jump == True:
                v_speed = v_speed - 30
                can_jump = False
    hero_old_x = hero_x
    hero_old_y = hero_y
    enemy_old_x = enemy_x
    enemy_old_y = enemy_y
    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + h_speed
    elif keystate[pygame.K_LEFT] == True:
        hero_x = hero_x - h_speed
    if hero_x > enemy_x:
        enemy_x = enemy_x + h_speed_enemy
    else:
        enemy_x = enemy_x - h_speed_enemy
    v_speed = v_speed + g
    hero_y = hero_y + v_speed
    v_speed_enemy = v_speed_enemy + g
    enemy_y = enemy_y + v_speed_enemy
    if enemy_y >= 600:
        enemy_y = 600
        v_speed_enemy = 0
        can_jump_enemy = True
    if hero_x >= width:
        hero_x = -block_size
    elif hero_x < -block_size:
        hero_x = width
    hero_rect.x = hero_x
    hero_rect.y = hero_y
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y
    for rect in rects:
        if hero_rect.colliderect(rect) == True and abs(rect.y - hero_y) <= block_size // 2:
            hero_x = hero_old_x
        if hero_rect.colliderect(rect) == True:
            hero_y = rect.y - block_size
            v_speed = 0
            can_jump = True
        if enemy_rect.colliderect(rect) == True and abs(rect.y - enemy_y) <= block_size // 2:
            enemy_x = enemy_old_x
        if enemy_rect.colliderect(rect) == True:
            enemy_y = rect.y - block_size
            v_speed_enemy = 0
            can_jump_enemy = True
    
    # if hero_rect.colliderect(enemy_rect) == True:
    #     run = False
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "b":
                screen.blit(block, (j * block_size, i * block_size))
    screen.blit(snowman, (hero_x, hero_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    pygame.display.flip()
    clock.tick(fps)
         
pygame.quit()