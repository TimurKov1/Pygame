import os
import random
import sys
import pygame

from Warrior import Warrior
from Leaf import Leaf
from Monk import Monk
from Functions import load_image
from Constants import WIDTH, HEIGHT


def update():
    screen.fill(pygame.Color("black"))
    pygame.draw.rect(screen, 'white', (20, 20, 300, 25), 1)
    pygame.draw.rect(screen, '#42AAFF', (21, 21, player.power * 3 - 2, 23))
    pygame.draw.rect(screen, 'white', (20, 50, 300, 25), 1)
    pygame.draw.rect(screen, '#E32636', (21, 51, 298, 23))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size, pygame.SCALED, vsync=1)
pygame.display.set_caption('Игра')
screen.fill(pygame.Color("black"))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Leaf(all_sprites)


running = True
loop = True
while running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.type = 'run_right'
        player.direction = 'right'
        loop = False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.type = 'run_left'
        player.direction = 'left'
        loop = False
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player.isJump = True
        loop = False
    if pygame.key.get_pressed()[pygame.K_f]:
        if (not player.isAttack2) and (not player.isAttack3) and player.power >= player.attackEnergy:
            player.isAttack = True
    if pygame.key.get_pressed()[pygame.K_g]:
        if (not player.isAttack) and (not player.isAttack3) and player.power >= player.attack2Energy:
            player.isAttack2 = True
    if pygame.key.get_pressed()[pygame.K_v]:
        if (not player.isAttack) and (not player.isAttack2) and player.power >= player.attack3Energy:
            player.isAttack3 = True
    if loop:
        player.type = 'idle'
    loop = True
    update()

pygame.quit()