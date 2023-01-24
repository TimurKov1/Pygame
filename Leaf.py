import os
import pygame
from Functions import load_image
from Bullet import Bullet


class Leaf(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.all_sprites = all_sprites
        self.frames = [load_image(f"Characters/Leaf/Idle/{i + 1}.png") for i in range(len(os.listdir("./Sprites/Characters/Leaf/Idle")))]
        self.current_frame = 0
        self.type = 'idle'
        self.direction = 'right'
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400
        self.speed = 10
        self.isJump = False
        self.isAttack = False
        self.isAttack2 = False
        self.isAttack3 = False
        self.attackEnergy = 7
        self.attack2Energy = 15
        self.attack3Energy = 0
        self.isBlock = False
        self.bullet = 0
        self.jumpCount = 16
        self.attackCount = 0
        self.attackX = 0
        self.power = 100
        self.count = 0
        self.loop = False

    def update(self):
        if self.count == 15:
            if self.power < 100:
                self.power += 1
            self.count = 0
        if self.bullet:
            if self.bullet.check():
                self.bullet = 0
                self.loop = False
        if self.isJump:
            if self.jumpCount == 16:
                self.current_frame = 0

            if self.jumpCount >= 0:
                self.change_frames("Characters/Leaf/Jump", 5)
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2)), True, False)
            else:
                self.change_frames("Characters/Leaf/Fall", 5)
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2)), True, False)
            if self.jumpCount >= -16:
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 6
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 6
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 16
        if self.isAttack and (not self.isJump):
            if self.attackCount == 0:
                self.attackX = self.rect.x
            if self.attackCount == len(self.frames):
                self.isAttack = False
                self.attackCount = 0
                self.power -= 7
                return
            self.change_frames("Characters/Leaf/Attack1", 5)
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2)), True, False)
                self.rect.x = self.attackX - self.image.get_width() + 92
            self.attackCount += 1
        elif self.isAttack2 and (not self.isJump):
            if self.attackCount == 0:
                self.attackX = self.rect.x
            if self.attackCount == 30:
                if self.direction == 'right':
                    self.bullet = Bullet(self.all_sprites, self.rect.x - self.image.get_width(), self.rect.y - 50, 50, 10, self.direction, "Characters/Leaf/Things/arrow.png")
                else:
                    self.bullet = Bullet(self.all_sprites, self.rect.x - self.image.get_width() * 2, self.rect.y - 50, 50, 10, self.direction, "Characters/Leaf/Things/arrow.png")
            if self.attackCount == len(self.frames):
                self.loop = True
                self.attackCount = 0
                self.isAttack2 = False
                self.power -= 15
                return
            self.change_frames("Characters/Leaf/Attack2", 4)
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2)), True, False)
                self.rect.x = self.attackX - self.image.get_width() + 92
            self.attackCount += 1
        else:
            if self.type == 'idle':
                if not self.isJump:
                    self.change_frames("Characters/Leaf/Idle", 5)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    if self.direction == 'right':
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
                    else:
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2)), True, False)
            if self.type == 'run_right':
                if not self.isJump:
                    self.change_frames("Characters/Leaf/Run", 4)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
                self.rect.x += self.speed
            if self.type == 'run_left':
                if not self.isJump:
                    self.change_frames("Characters/Leaf/Run", 4)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2)), True, False)
                if self.rect.x > 0:
                    self.rect.x -= self.speed
        self.count += 1
    
    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))