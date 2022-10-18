import pygame
from pygame import *
from random import randint
import time
mixer.init()
mixer.music.load("space.ogg")
# mixer.music.play()

font.init()
font1 = font.SysFont("Arial", 50) 

lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = -5
            self.rect.x = randint(0, 630)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = -5
            self.rect.x = randint(0, 630)

monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()

for i in range(4):
    asteroid = Enemy("asteroid.png", randint(0, 630), -5, 65, 65, randint(2,3))
    asteroid.add(asteroids)

for i in range(6):
    enemy = Enemy("ufo.png", randint(0, 630), -5, 65, 65, randint(3,5)) #Меняется только Х( будет рандомным ) randint(x1,x2)
    monsters.add(enemy)


player = Player("rocket.png", 350, 400, 65, 65, 10)


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space defender")

background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

clock = pygame.time.Clock()

score = 0

num_fire = 0
rel_time = False

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and num_fire < 5:
                player.fire()
                num_fire += 1

                if num_fire >= 5:
                    rel_time = True
                    start_time = time.time() 

    if finish != True:
        window.blit(background, (0,0))
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        asteroids.draw(window)
        asteroids.update()

        if rel_time == True:
            current_time = time.time()
            if current_time - start_time < 3:
                reload_text = font1.render("Перезарядка..." + str(score), 1, (255,0,0))
                window.blit(reload_text, (400, 300))
            else:
                num_fire = 0
                rel_time = False

        #Шаблон для касаний и условий завершения
        sprites_list = sprite.groupcollide(bullets, monsters, True, True) #Групповое столкновения груп монстров и пуль
        #Цикл для проверки сколько монстров было сбито и нужно создать новых
        for m in sprites_list:
            enemy = Enemy("ufo.png", randint(0, 630), -5, 65, 65, randint(3,4)) #Меняется только Х( будет рандомным ) randint(x1,x2)
            monsters.add(enemy)
            #Увеличиваете счеткик очков на +1
            score += 1
        
        if score >= 10:
            finish = True
            win = font1.render("Ты выиграл!", 1, (0, 255, 0))
            window.blit(win, (300, 250))
        
        if lost >= 3:
            finish = True
            game_over = font1.render("Ты проиграл!", 1, (255, 0, 0))
            window.blit( game_over, (300, 250))

        score_text = font1.render("Очки:" + str(score), 1, (255,255,255))
        window.blit(score_text, (10,10))

        text_lost = font1.render("Пропущено: " + str(lost), 1, (255,255,255))
        window.blit(text_lost, (10, 40))

    clock.tick(40)
    display.update()