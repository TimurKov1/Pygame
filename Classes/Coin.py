import os
import pygame
from .Functions import load_image
from .Constants import WIDTH, HEIGHT


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(load_image('Graphics/coin.png'), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.motion = 0
        self.loop = True
        self.checked = 0
        self.count = 0
        self.speed = 0

    def update(self, shift):
        self.rect.x += shift

    def change(self):
        if self.count == 15:
            self.count = 0
            if self.motion > 0:
                self.motion = -1
            else:
                self.motion = 1
        if self.speed % 2 == 0:
            self.count += 1
            self.rect.y += self.motion
        self.speed += 1

    def check(self, player):
        if player.rect.x <= self.rect.x <= (player.rect.x + player.image.get_width()) and player.rect.y <= self.rect.y <= (player.rect.y + player.image.get_height()):
            self.image = pygame.transform.scale(self.image, (0, 0))
            self.checked = 1