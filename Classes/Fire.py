import os
import pygame
from .Functions import load_image
from .Constants import WIDTH, HEIGHT


class Fire(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, speed, direction):
        super().__init__(all_sprites)
        self.direction = direction
        self.frames = []
        self.change_frames("Enemies/Snake/Move", 5)
        self.current_frame = 0
        if self.direction == 'right':
            self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2.5, self.frames[self.current_frame].get_height() * 2.5))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2.5, self.frames[self.current_frame].get_height() * 2.5)), True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.isActive = True

    def update(self):
        if self.isActive:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2.5, self.frames[self.current_frame].get_height() * 2.5))
                self.rect.x += self.speed
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2.5, self.frames[self.current_frame].get_height() * 2.5)), True, False)
                self.rect.x -= self.speed

    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))