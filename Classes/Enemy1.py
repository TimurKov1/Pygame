import os
import pygame
from .Functions import load_image


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x1, x2):
        super().__init__(all_sprites)
        self.frames = []
        self.change_frames("Enemies/Enemy1/Idle", 5)
        self.current_frame = 0
        self.type = 'idle'
        self.direction = 'right'
        self.image = pygame.transform.scale(self.frames[self.current_frame], (
        self.frames[self.current_frame].get_width() * 2, self.frames[self.current_frame].get_height() * 2))
        self.rect = self.image.get_rect()
        self.x1 = x1
        self.dx = 0
        self.rect.x = x2
        self.rect.y = 448 - self.image.get_height()
        self.auch = 0
        self.seeya = False
        self.hp = 70
        self.see = False
        self.dmg = False
        self.speed = 2
        self.power = 1
        self.isDamaged = False
        self.isAttack = False
        self.isAttack2 = False
        self.isAttack3 = False
        self.attackEnergy = 10
        self.isBlock = False
        self.jumpCount = 15
        self.attackX = 0
        self.count = 0
        self.attackCount = 0
        self.damageLoop = False
        self.isDead = False
        self.bulletDamaged = False

    def update(self):
        if self.hp <= 0:
            if not self.isDead:
                self.change_frames("Enemies/Enemy1/Hit", 5)
                self.current_frame = 0
                self.isDead = True
            if self.current_frame == len(self.frames):
                self.frames = []
                self.current_frame = 0
                self.image = pygame.transform.scale(self.image, (0, 0))
                return
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2)), True, False)
            self.current_frame += 1
        if self.count == 50:
            self.power = 1
            self.count = 0
        if self.isDamaged:
            if self.damageLoop:
                self.current_frame = 0
                self.change_frames("Enemies/Enemy1/Hit", 5)
                self.damageLoop = False
            if self.current_frame == len(self.frames):
                self.isDamaged = False
                self.type = 'idle'
                self.change_frames("Enemies/Enemy1/idle", 5)
                self.current_frame = 0
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2)), True, False)
            self.current_frame += 1
        elif self.isAttack:
            if self.attackCount == 0:
                self.attackX = self.rect.x
                self.change_frames("Enemies/Enemy1/Attack", 4)
            if self.attackCount == len(self.frames) - 1:
                self.isAttack = False
                self.attackCount = 0
                self.power = 0
                self.dmg = True
                self.change_frames("Enemies/Enemy1/Idle", 5)
                return
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2, self.frames[self.attackCount].get_height() * 2)), True, False)
            self.attackCount += 1
        else:
            if self.type == 'idle':
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2,
                        self.frames[self.current_frame].get_height() * 2))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2,
                        self.frames[self.current_frame].get_height() * 2)), True, False)
            if self.type == 'run_right':
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2))
                self.rect.x += self.speed
                self.direction = 'right'
                self.dx += self.speed
            if self.type == 'run_left':
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2,
                    self.frames[self.current_frame].get_height() * 2)),
                                                    True, False)
                self.direction = 'left'
                self.rect.x -= self.speed
                self.dx -= self.speed
        self.count += 1


    def check(self, player):
        if self.dmg == True:
            if player.rect.x >= self.rect.x - 30 and not player.rect.x > self.rect.x:
                player.hp -= 10
            elif player.rect.x <= self.rect.x + 150 and not player.rect.x < self.rect.x:
                player.hp -= 10
            self.dmg = False

        if player.rect.x <= self.rect.x <= player.rect.x + 200 and (not self.see):
            self.see = True
        elif player.rect.x - 200 <= self.rect.x <= player.rect.x and (not self.see):
            self.see = True
        if self.see:
            if player.rect.x <= self.rect.x - 10 and self.dx > self.x1:
                if self.type != 'run_left':
                    self.current_frame = 0
                    self.change_frames("Enemies/Enemy1/Run", 7)
                self.type = 'run_left'
            elif player.rect.x >= self.rect.x - 40 + self.image.get_width() and self.dx < 0:
                if self.type != 'run_right':
                    self.current_frame = 0
                    self.change_frames("Enemies/Enemy1/Run", 7)
                self.type = 'run_right'
            else:
                if self.power:
                    self.isAttack = True
                if self.type != 'idle':
                    self.current_frame = 0
                    self.change_frames("Enemies/Enemy1/Idle", 5)
                self.type = 'idle' 

    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))