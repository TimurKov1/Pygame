import os
import pygame
from .Functions import load_image
from .Constants import WIDTH, HEIGHT


class Bullet(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, speed, damage, direction, sprite):
        super().__init__(all_sprites)
        self.direction = direction
        if self.direction == 'right':
            self.image = pygame.transform.scale(load_image(sprite), (load_image(sprite).get_width() * 2, load_image(sprite).get_height() * 2))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(load_image(sprite), (load_image(sprite).get_width() * 2, load_image(sprite).get_height() * 2)), True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.damage = damage

    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    def check(self):
        if self.direction == 'right':
            if self.rect.x > WIDTH:
                return True
            return False
        else:
            if self.rect.x < 0:
                return True
            return False