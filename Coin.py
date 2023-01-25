import os
import pygame
from Functions import load_image
from Constants import WIDTH, HEIGHT


class Coin(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, sprite):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image(sprite), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.motion = 0
        self.loop = True
        self.checked = 0
        self.count = 0

    def check(self, player):
        if player.rect.x <= self.rect.x <= (player.rect.x + player.image.get_width()) and player.rect.y <= self.rect.y <= (player.rect.y + player.image.get_height()):
            self.image = pygame.transform.scale(self.image, (0, 0))
            self.checked = 1