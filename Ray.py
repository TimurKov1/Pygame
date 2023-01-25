import os
import pygame
from Functions import load_image
from Constants import WIDTH, HEIGHT


class Ray(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, damage):
        super().__init__(all_sprites)
        self.change_frames("Characters/Leaf/Things/Ray", 4)
        self.current_frame = 0
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 4, self.frames[self.current_frame].get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = damage
        self.loop = False

    def update(self):
        if self.current_frame < len(self.frames):
            self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 4, self.frames[self.current_frame].get_height() * 2))
            self.current_frame = (self.current_frame + 1)

    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))