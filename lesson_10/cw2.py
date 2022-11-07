import time


class Mob:
    def __init__(self, x, y, hp, mana, damage, type, loot, weapon, skill):
        self.x = x
        self.y = y
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.type = type
        self.loot = loot
        self.weapon = weapon
        self.skill = skill
        self.h_speed = 1
        self.v_speed = 1

    def update(self):
        x_left = 0
        x_right = 7
        y_down = 0
        y_up = 7
        if self.y == y_down and x_left <= self.x < x_right:
            self.x = self.x + self.h_speed
        elif self.x == x_right and y_down <= self.y < y_up:
            self.y = self.y + self.v_speed
        elif self.y == y_up and x_left < self.x <= x_right:
            self.x = self.x - self.h_speed
        elif self.x == x_left and y_down < self.y <= y_up:
            self.y = self.y - self.v_speed


mob_1 = Mob(0, 0, 100, 100, 20, "zombie", 150, "pistol", "bite")
mob_2 = Mob(20, 17, 200, 300, 80, "boss", 1000, "bazooka", "regeniration")


run = True

while run == True:
    map = [[0 for i in range(8)] for i in range(8)]
    mob_1.update()
    map[mob_1.x][mob_1.y] = 1
    for x in map:
        print(x)
    print()
    print()
    print()
    time.sleep(0.2)