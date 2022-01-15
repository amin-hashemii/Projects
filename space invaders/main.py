import pygame as py
import os
import time
import random

py.font.init()
WIDTH, HEIGHT = 500, 700
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Sapce invaders')
#Bots
BLUE_SPACESHIP = py.image.load(os.path.join('asset', 'blue.png'))
RED_SPACESHIP = py.image.load(os.path.join('asset', 'red.png'))
GREEN_SPACESHIP = py.image.load(os.path.join('asset', 'green.png'))


#Player
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 100
PLAYER_SPACESHIP = py.transform.scale(py.image.load(os.path.join('asset', 'spaceship.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


#Lasers
BLUE_LASER = py.image.load(os.path.join('asset', 'pixel_laser_blue.png'))
GREEN_LASER = py.image.load(os.path.join('asset', 'pixel_laser_green.png'))
RED_LASER = py.image.load(os.path.join('asset', 'pixel_laser_red.png'))
YELLOW_LASER = py.image.load(os.path.join('asset', 'pixel_laser_yellow.png'))


#Background
BACK = py.transform.scale(py.image.load(os.path.join('asset', 'back.png')), (WIDTH, HEIGHT))


WHITE = (255, 255, 255)
FONT = py.font.SysFont('Arial', 30)
LOST_FONT = py.font.SysFont('Arial', 50)
PLAYER_VEL = 5


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_laser(self, vel, obj):
        self.countdown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.on_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def countdown(self):
        if self.cool_down_counter >= self.COOLDOWN :
            self.cool_down_counter = 0

        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()



class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=health)
        self.ship_img = PLAYER_SPACESHIP
        self.max_health = health
        self.laser_image = YELLOW_LASER
        self.mask = py.mask.from_surface(self.ship_img)
    
    def move_laser(self, vel, objs):
        self.countdown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.on_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        py.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height()+10, self.ship_img.get_width(), 10))
        py.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height()+10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    COLOR_MAP = {
        'red':(RED_SPACESHIP, RED_LASER), 
        'green': (GREEN_SPACESHIP, GREEN_LASER),
        'blue': (BLUE_SPACESHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health=health)
        self.ship_img, self.laser_image = self.COLOR_MAP[color]
        self.mask = py.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-10, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    
class Laser:
    def __init__(self, x, y, img) -> float:
        self.x = x
        self.y = y
        self.img = img
        self.mask = py.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel
    
    def on_screen(self, height):
        return not(self.y <= height and self.y >= 0)


    def collision(self, obj):
        return collide(obj, self)


    
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def redraw_window(lives, level, lost, enemies, player):
        WIN.blit(BACK, (0, 0))
        lives_label = FONT.render(f'Lives: {lives}', 1, WHITE)
        level_label = FONT.render(f'level: {level}', 1, WHITE)
        WIN.blit(lives_label, (0, lives_label.get_height() - 35))
        WIN.blit(level_label, (WIDTH - level_label.get_width(), level_label.get_height() - 35))

        if lost:
            lost_label = LOST_FONT.render('YOU LOST!', 1, WHITE)
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()/2))

        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)
        py.display.update()


def movement(key_pressed, player):
    if key_pressed[py.K_a] and player.x > 0:
        player.x -= PLAYER_VEL
    if key_pressed[py.K_d] and player.x  + player.get_width() < WIDTH:
        player.x += PLAYER_VEL
    if key_pressed[py.K_w] and player.y  > 0:
        player.y -= PLAYER_VEL
    if key_pressed[py.K_s] and player.y + player.get_height() +20 < HEIGHT:
        player.y += PLAYER_VEL
    if key_pressed[py.K_SPACE]:
        player.shoot()

def main():
    run = True
    FPS = 60
    clock = py.time.Clock()
    level = 0
    lives = 3

    enemies = []
    wave_length = 5
    enemy_vel = 1
    laser_vel = 4
    lost = False
    lost_count = 0
    player = Player(200, 550)

    while run: 
        clock.tick(FPS)
        redraw_window(lives, level, lost, enemies, player)

        if lives <= 0 or player.health <= 0:
            lost= True
            lost_count += 1
        if lost:
            if lost_count >= FPS *3 :
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                color = random.choice(('red', 'green', 'blue'))
                enemy = Enemy(random.randrange(50, WIDTH -100), random.randrange(-1500, -100), color)
                if wave_length > 15 and color == 'red':
                    enemy.health = 200
                elif wave_length > 15 and color == 'green':
                    enemy.health = 150
                enemies.append(enemy)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    run = False
            
        key_pressed = py.key.get_pressed()
        
        movement(key_pressed, player)
        

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_laser(laser_vel, player)
            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            
        player.move_laser(-laser_vel, enemies)
    py.quit()
    quit()



def main_menu():
    title = py.font.SysFont('Arial', 100)
    run = True
    
    while run:
        WIN.blit(BACK, (0, 0))
        text = title.render('Press key to run the game', 1, WHITE)
        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            
            if event.type == py.MOUSEBUTTONDOWN:
                main()
    py.quit()
    quit()

main_menu()