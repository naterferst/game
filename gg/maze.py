from colorama import init 
init()
from pygame import *
import math

font.init()
kick.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()

        if  keys_pressed[K_UP] and self.rect.y > 40:
            self.rect.y -= self.speed
        if  keys_pressed[K_DOWN] and self.rect.y < 910:
            self.rect.y += self.speed
        if  keys_pressed[K_LEFT] and self.rect.x > 80:
            self.rect.x -= self.speed
        if  keys_pressed[K_RIGHT] and self.rect.x < 1850:
            self.rect.x += self.speed

class Enemy(GameSprite):

    direction = 'left'

    def update(self):
        if self.rect.x <= 600:
            self.direction = 'right'
        if self.rect.x >= 1300:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, w, h, x, y):
        super().__init__()
        self.color1 = color1  
        self.color2 = color2  
        self.color3 = color3
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player("hero.png", 50, 50, 10)
enemy = Enemy("cyborg.png", 950, 345, 5)
treasure = GameSprite("treasure.png", 950, 445, 5)

win_width = 1965
win_height = 1000
FPS = 60

window = display.set_mode((win_width, win_height))
display.set_caption("Temples")

background = transform.scale(image.load("background.jpg"), (win_width, win_height))

clock = time.Clock()

w1 = Wall(255, 0, 0, 200, 10, 100, 100)
w2 = Wall(255, 0, 0, 40, 200, 100, 150)
w3 = Wall(255, 0, 0, 200, 40, 100, 300)

game = True
while game:
    window.blit(background, (0,0))

    player.reset()
    enemy.reset()
    treasure.reset()
    player.move()
    enemy.update()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()


    for e in event.get():
        if e.type == QUIT:
            game = False


font = font.Font(None, 70)

win = font.render(
    'YOU WIN!', True, (255, 215, 0)

)

#lose = 

kick = mixer.Sound('Kick.ogg')
#money = #  клас соунд

#finish = # для завершения игры

        if finish != True:
            if sprite.collide_rect(packman, final)

        window.blit(background,(0, 0))
        packman.update()
        monster.update()
        packman.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        kick.play()

        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1):
            window.blit(win, (200,200))

            kick.play()=    
    clock.tick(80)
    display.update()