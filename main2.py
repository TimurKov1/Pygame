import os
import random
import sys
import pygame

from Classes.Warrior import Warrior
from Classes.Leaf import Leaf
from Classes.Monk import Monk
from Classes.Demon import Demon
from Classes.Functions import load_image
from Classes.Constants import WIDTH, HEIGHT
from Classes.Camera import Camera
from Classes.Coin import Coin
from Classes.Camera import Camera
from Classes.Enemy1 import Enemy1
from Classes.Enemy2 import Enemy2


def update():
    global coin_count
    # if not player.isAttack and not player.isAttack2 and not player.isAttack3:
    #     camera.update(player)
    #     for sprite in all_sprites:
    #         camera.apply(sprite)
    count = 0
    for enemy in range(len(enemies)):
        if enemies[enemy] != '':
            if enemies[enemy].isDead:
                enemies[enemy] = ''
                continue
            enemies[enemy].check(player)
    for enemy in enemies:
        if enemy == '':
            enemies.remove(enemy)
    coin_count = count
    screen.fill(pygame.Color("black"))
    font = pygame.font.Font(None, 50)
    text = font.render(f"{coin_count}", True, (255, 255, 255))
    screen.blit(text, (WIDTH - 50, 30))
    pygame.draw.rect(screen, 'white', (20, 20, 300, 25), 1)
    pygame.draw.rect(screen, '#42AAFF', (21, 21, player.power * 3 - 2, 23))
    pygame.draw.rect(screen, 'white', (20, 50, 300, 25), 1)
    pygame.draw.rect(screen, '#E32636', (21, 51, player.hp * 3 - 2, 23))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.init()
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size, pygame.SCALED, vsync=1)
pygame.display.set_caption('Игра')
screen.fill(pygame.Color("black"))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
coin_count = 0
running = True
loop = True 
# camera = Camera()
enemies = []
boss = Demon(all_sprites, screen, 600)
player = Leaf(all_sprites, enemies)
enemies.append(boss)
for enemy in enemies:
    enemy.player = player


while running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not player.isDead:
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if player.type != 'run_right':
                player.changeLoop = True
            else:
                player.changeLoop = False
            player.type = 'run_right'
            player.direction = 'right'
            loop = False
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if player.type != 'run_left':
                player.changeLoop = True
            else:
                player.changeLoop = False
            player.type = 'run_left'
            player.direction = 'left'
            loop = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player.isJump = True
            loop = False
        if pygame.key.get_pressed()[pygame.K_f]:
            if (not player.isAttack2) and (not player.isAttack3) and player.power >= player.attackEnergy:
                if player.type != 'attack1':
                    player.changeLoop = True
                else:
                    player.changeLoop = False
                player.type = 'attack1'
                player.isAttack = True
        if pygame.key.get_pressed()[pygame.K_g]:
            if (not player.isAttack) and (not player.isAttack3) and player.power >= player.attack2Energy:
                if player.type != 'attack2':
                    player.changeLoop = True
                else:
                    player.changeLoop = False
                player.type = 'attack2'
                player.isAttack2 = True
        if pygame.key.get_pressed()[pygame.K_v]:
            if (not player.isAttack) and (not player.isAttack2) and player.isAttack3 != None and player.power >= player.attack3Energy:
                if player.type != 'attack3':
                    player.changeLoop = True
                else:
                    player.changeLoop = False
                player.type = 'attack3'
                player.isAttack3 = True
        if loop:
            if player.type != 'idle':
                player.changeLoop = True
            else:
                player.changeLoop = False
            player.type = 'idle'
    if player.hp <= 0:
        if not player.isDead:
            player.changeLoop = True
            player.isDead = True
            player.current_frame = 0
        if player.current_frame == len(player.frames):
            pygame.init()
            size = width, height = WIDTH, HEIGHT
            screen = pygame.display.set_mode(size, pygame.SCALED, vsync=1)
            pygame.display.set_caption('Игра')
            screen.fill(pygame.Color("black"))
            clock = pygame.time.Clock()
            all_sprites = pygame.sprite.Group()
            coin_count = 0
            running = True
            loop = True
            camera = Camera()
            coins = []
            for i in range(1, 5):
                coin = Coin(all_sprites, i * 1000, 550, "coin.png")
                coins.append(coin)
            player = Leaf(all_sprites)
    loop = True
    update()

pygame.quit()