import os
import random
import sys
import pygame
import pygame_menu
from settings import *
from Level import Level
from pygame_menu import themes, Theme
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
    global all_sprites, camera, screen, enemies, level, hero, coins, coin_count, size, player, x, loop, boss
    if 4730 < x < 4750:
        loop = True
    if player.rect.y > 1000:
        player.hp = 0
    if not player.isAttack and not player.isAttack2 and not player.isAttack3 and not loop:
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
    count = 0
    for coin in coins:
        coin.check(player)
        count += coin.checked
        coin.change()
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
    if player.type == 'run_right':
        x += player.speed
    elif player.type == 'run_left':
        x -= player.speed
    if not loop:
        level.run()
    else:
        level.run(loop=True)
    if loop and not boss:
        boss = Demon(all_sprites, screen, 1000)
        boss.player = player
        enemies.append(boss)
    if boss:
        boss.check(player)
    font = pygame.font.Font(None, 50)
    text = font.render(f"{coin_count}", True, (0, 0, 0))
    screen.blit(text, (WIDTH - 50, 30))
    pygame.draw.rect(screen, 'white', (20, 20, 300, 25), 1)
    pygame.draw.rect(screen, '#42AAFF', (21, 21, player.power * 3 - 2, 23))
    pygame.draw.rect(screen, 'white', (20, 50, 300, 25), 1)
    pygame.draw.rect(screen, '#E32636', (21, 51, player.hp * 3 - 2, 23))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


def set_character(value, difficulty):
    global hero
    if difficulty == 1:
        hero = 'Warrior'
    elif difficulty == 2:
        hero = 'Monk'
    else:
        hero = 'Leaf'


def level_menu():
    mainmenu._open(menu)


def menu():
    global mainmenu, menu

    mainmenu = pygame_menu.Menu('The last battle', 600, 400, theme=mytheme)
    mainmenu.add.button('Play', main)
    mainmenu.add.button('Character', level_menu)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)

    menu = pygame_menu.Menu('Select a character', 600, 400, theme=mytheme)
    menu.add.selector('Select character :', [('Warrior', 1), ('Monk', 2),  ('Leaf', 3)], onchange=set_character)

    mainmenu._open(mainmenu)
    mainmenu.mainloop(surface)


def main():
    global all_sprites, camera, screen, enemies, level, hero, coins, coin_count, size, player, mainmenu
    pygame.init()
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size, pygame.SCALED, vsync=1)
    all_sprites = pygame.sprite.Group()
    coins = []
    coin_count = 0
    x = 0
    enemies = [Enemy1(all_sprites, -600, 1000), Enemy2(all_sprites, -900, 3600)]
    pygame.display.set_caption('Игра')
    level = Level(level_1, screen, coins)
    screen.fill(pygame.Color("black"))
    clock = pygame.time.Clock()
    running = True
    loop = True
    if hero == 'Leaf':
        player = Leaf(all_sprites, enemies, level.grass_sprites, level.flying_terrain_sprites, level.flying_terrain_tileset4_sprites)
    elif hero == 'Warrior':
        player = Warrior(all_sprites, enemies, level.grass_sprites, level.flying_terrain_sprites, level.flying_terrain_tileset4_sprites)
    elif hero == 'Monk':
        player = Monk(all_sprites, enemies, level.grass_sprites, level.flying_terrain_sprites, level.flying_terrain_tileset4_sprites)
    player.rect.y = 100
    level.player = player
    level.run(move=True)
    for enemy in enemies:
        enemy.player = player

    while running:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if player.hp <= 0:
            surface = pygame.display.set_mode((600, 400))
            font = pygame_menu.font.FONT_MUNRO
            mytheme = Theme(widget_font=font,
                            background_color=(0, 0, 0, 0), # transparent background
                            title_background_color=(4, 47, 126),
                            title_font_shadow=True,
                            widget_padding=25)


            mainmenu = pygame_menu.Menu("You've lost", 600, 400, theme=mytheme)
            mainmenu.add.button('Try again', main)
            mainmenu.add.button('Quit lobby', menu)
            mainmenu.add.button('Quit', pygame_menu.events.EXIT)
            mainmenu.mainloop(surface)
        else:
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
            loop = True
            update()

    pygame.quit()


pygame.init()

size = width, height = 0, 0
screen = 0
x = 0
boss = 0
loop = False
all_sprites = pygame.sprite.Group()
camera = Camera()
enemies = []
coins = []
coin_count = 0
player = 0
level = 0
hero = "Warrior"

surface = pygame.display.set_mode((600, 400))
font = pygame_menu.font.FONT_MUNRO
mytheme = Theme(widget_font=font,
                background_color=(0, 0, 0, 0),
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                widget_padding=25)

mainmenu = pygame_menu.Menu('The last battle', 600, 400, theme=mytheme)
mainmenu.add.button('Play', main)
mainmenu.add.button('Character', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

menu = pygame_menu.Menu('Select a character', 600, 400, theme=mytheme)
menu.add.selector('Select character :', [('Warrior', 1), ('Monk', 2),  ('Leaf', 3)], onchange=set_character)

mainmenu.mainloop(surface)