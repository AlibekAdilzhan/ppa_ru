import pygame
import time
 
pygame.init()
pygame.font.init()
pygame.mixer.init()

# font object..................................
def create_font(t, c=(255,255,0)):
    font = pygame.font.SysFont("Arial", 36, bold=False, italic=False)
    text = font.render(t, True, c)
    return text

music = pygame.mixer.music.load("music_1.ogg")
sound_coin = pygame.mixer.Sound("sound_coin.wav")
pygame.mixer.music.play(-1)
class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, block_size // 2, block_size // 2)
        self.image = coin_image


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
coin_image = pygame.image.load("coin1.png")
coin_image = pygame.transform.scale(coin_image, (block_size // 2, block_size // 2))
batoot_image = pygame.image.load("trampoline.png")
batoot_image = pygame.transform.scale(batoot_image, (block_size, block_size // 3))


game_map = [
    ".................................................",
    ".................................................",
    "................................................",
    "........b..........$.............................",
    "....$..ybb.........$.............................",
    "..$bbbbbbbb...$..$.$$..$....$$$$...................",
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
coins_counter = 0

camera_x = 0 # peremennaya chtoby menyat' kameru

hero_rect = pygame.Rect(hero_x, hero_y, block_size, block_size)
enemy_rect = pygame.Rect(enemy_x, enemy_y, block_size, block_size)

rects = []
coins = []
batoots = []
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)
        if game_map[i][j] == "$":
            coin = Coin(j * block_size, i * block_size)
            coins.append(coin)
        if game_map[i][j] == "y":
            batoot_rect = pygame.Rect(j * block_size, i * block_size + 2 * block_size // 3, block_size, block_size // 3)
            batoots.append(batoot_rect)

start_batoot = time.time()

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
    # if hero_x >= width:
    #     hero_x = -block_size
    # elif hero_x < -block_size:
    #     hero_x = width
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
    if hero_x - camera_x >= 0.5 * width: # esli igrok dohodit do poloviny shiriny ekrana, to kamera dvigaetsya
        camera_x = camera_x + h_speed
    elif hero_x - camera_x <= 0.3 * width: # to je samoe (pochti)
        camera_x = camera_x - h_speed
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "b":
                screen.blit(block, (j * block_size - camera_x, i * block_size))
            if game_map[i][j] == "y":
                screen.blit(batoot_image, (j * block_size - camera_x, i * block_size + 2 * block_size // 3))
    for coin in coins:
        screen.blit(coin.image, (coin.x - camera_x + block_size // 4, coin.y + block_size // 4))
        if hero_rect.colliderect(coin):
            coins_counter += 1
            coins.remove(coin)
            del coin
            pygame.mixer.Sound.play(sound_coin)
    for batoot in batoots:
        if hero_rect.colliderect(batoot) and time.time() - start_batoot > 0.25:
            start_batoot = time.time()
            v_speed = v_speed - 30
            can_jump = False
    coins_amount = create_font("COINS:" + str(coins_counter))
    screen.blit(snowman, (hero_x - camera_x, hero_y))
    screen.blit(enemy, (enemy_x - camera_x, enemy_y))
    screen.blit(coins_amount, (60, 10))
    screen.blit(coin_image, (10, 10))
    pygame.display.flip()
    clock.tick(fps)
         
pygame.quit()