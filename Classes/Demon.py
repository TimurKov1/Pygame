import os
import pygame
import random
from .Functions import load_image


class Demon(pygame.sprite.Sprite):
    def __init__(self, all_sprites, screen, x):
        super().__init__(all_sprites)
        self.frames = []
        self.screen = screen
        self.change_frames("Bosses/Demon/Idle", 10)
        self.current_frame = 0
        self.type = 'idle'
        self.direction = 'left'
        self.image = pygame.transform.scale(self.frames[self.current_frame], (
        self.frames[self.current_frame].get_width() * 2.5, self.frames[self.current_frame].get_height() * 2.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 480 - self.image.get_height()
        self.auch = 0
        self.seeya = False
        self.hp = 1000
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
        self.hpX = 0
        self.count = 0
        self.attackCount = 0
        self.damageLoop = False
        self.isDead = False
        self.bulletDamaged = False
        self.player = 0

    def update(self):
        if self.hp <= 0:
            if not self.isDead:
                self.change_frames("Bosses/Demon/Death", 7)
                self.current_frame = 0
                self.isDead = True
            if self.current_frame == len(self.frames):
                self.frames = []
                self.current_frame = 0
                self.image = pygame.transform.scale(self.image, (0, 0))
                return
            if self.direction == 'left':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2.5,
                    self.frames[self.current_frame].get_height() * 2.5))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                    self.frames[self.current_frame].get_width() * 2.5,
                    self.frames[self.current_frame].get_height() * 2.5)), True, False)
            self.current_frame += 1
        else:
            if self.isAttack or self.isAttack2 or self.isAttack3:
                pygame.draw.rect(self.screen, 'white', (self.hpX, self.rect.y + 100, 200, 15), 1)
                pygame.draw.rect(self.screen, '#E32636', (self.hpX + 1, self.rect.y + 101, self.hp // 5 - 2, 13))
            else:
                pygame.draw.rect(self.screen, 'white', (self.rect.x, self.rect.y + 100, 200, 15), 1)
                pygame.draw.rect(self.screen, '#E32636', (self.rect.x + 1, self.rect.y + 101, self.hp // 5 - 2, 13))
            if self.count == 200:
                self.power = 1
                self.count = 0
            if self.isDamaged and (not self.isAttack) and (not self.isAttack2) and (not self.isAttack3):
                if self.damageLoop:
                    self.current_frame = 0
                    self.change_frames("Bosses/Demon/Hit", 5)
                    self.damageLoop = False
                if self.current_frame == len(self.frames):
                    self.isDamaged = False
                    self.type = 'idle'
                    self.change_frames("Bosses/Demon/Idle", 10)
                    self.current_frame = 0
                if self.direction == 'left':
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2.5,
                        self.frames[self.current_frame].get_height() * 2.5))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2.5,
                        self.frames[self.current_frame].get_height() * 2.5)), True, False)
                self.current_frame += 1
            elif self.isAttack:
                if self.attackCount == 0:
                    self.hpX = self.rect.x
                    self.attackX = self.rect.x + self.image.get_width()
                    self.change_frames("Bosses/Demon/Attack1", 4)
                if self.attackCount == len(self.frames) - 1:
                    if -100 < (self.rect.x - (self.player.rect.x + self.player.image.get_width())) < 130 and self.direction == 'left':
                        self.player.hp -= 30
                    elif -150 < (self.player.rect.x - (self.rect.x + self.image.get_width())) < 100 and self.direction == 'right':
                        self.player.hp -= 30
                    self.isAttack = False
                    self.attackCount = 0
                    self.power = 0
                    self.change_frames("Bosses/Demon/Idle", 10)
                    if self.player.rect.x <= self.rect.x:
                        self.direction = 'left'
                    else:
                        self.direction = 'right'
                    return
                if self.direction == 'left':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2.5, self.frames[self.attackCount].get_height() * 2.5))
                    self.rect.x = self.attackX - self.image.get_width()
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 2.5, self.frames[self.attackCount].get_height() * 2.5)), True, False)
                self.attackCount += 1
            elif self.isAttack2:
                if self.attackCount == 0:
                    self.hpX = self.rect.x
                    self.attackX = self.rect.x + self.image.get_width()
                    self.change_frames("Bosses/Demon/Attack2", 4)
                if self.attackCount == len(self.frames) - 1:
                    if -150 < (self.rect.x - (self.player.rect.x + self.player.image.get_width())) < 150 and self.direction == 'left':
                        self.player.hp -= 50
                    elif -150 < (self.player.rect.x - (self.rect.x + self.image.get_width())) < 120 and self.direction == 'right':
                        self.player.hp -= 50
                    self.isAttack2 = False
                    self.attackCount = 0
                    self.power = 0
                    self.change_frames("Bosses/Demon/Idle", 10)
                    if self.player.rect.x <= self.rect.x:
                        self.direction = 'left'
                    else:
                        self.direction = 'right'
                    return
                if self.direction == 'left':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 0.83), int(self.frames[self.attackCount].get_height() * 0.83)))
                    self.rect.x = self.attackX - self.image.get_width()
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 0.83), int(self.frames[self.attackCount].get_height() * 0.83))), True, False)
                self.attackCount += 1
            elif self.isAttack3:
                if self.attackCount == 0:
                    self.hpX = self.rect.x
                    self.attackX = self.rect.x + self.image.get_width() // 2
                    self.change_frames("Bosses/Demon/Attack3", 4)
                if self.attackCount == len(self.frames) - 1:
                    if -400 < (self.rect.x - (self.player.rect.x + self.player.image.get_width())) < 110:
                        self.player.hp -= 70
                    self.isAttack3 = False
                    self.attackCount = 0
                    self.power = 0
                    self.change_frames("Bosses/Demon/Idle", 10)
                    if self.player.rect.x <= self.rect.x:
                        self.direction = 'left'
                    else:
                        self.direction = 'right'
                    return
                if self.direction == 'left':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 0.83), int(self.frames[self.attackCount].get_height() * 0.83)))
                    self.rect.x = self.attackX - self.image.get_width() // 2
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 0.83), int(self.frames[self.attackCount].get_height() * 0.83))), True, False)
                    self.rect.x = self.attackX - self.image.get_width() // 2
                self.attackCount += 1
            else:
                if self.type == 'idle':
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    if self.direction == 'left':
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (
                            self.frames[self.current_frame].get_width() * 2.5,
                            self.frames[self.current_frame].get_height() * 2.5))
                    else:
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                            self.frames[self.current_frame].get_width() * 2.5,
                            self.frames[self.current_frame].get_height() * 2.5)), True, False)
                if self.type == 'run_left':
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    self.image = pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2.5,
                        self.frames[self.current_frame].get_height() * 2.5))
                    self.rect.x -= self.speed
                    self.direction = 'left'
                if self.type == 'run_right':
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (
                        self.frames[self.current_frame].get_width() * 2.5,
                        self.frames[self.current_frame].get_height() * 2.5)),
                                                        True, False)
                    self.direction = 'right'
                    self.rect.x += self.speed
            self.count += 1

    def check(self, player):
        if not self.isDamaged:
            if self.rect.x - (player.rect.x + player.image.get_width()) > 100 and (not self.isAttack) and (not self.isAttack2) and (not self.isAttack3):
                if self.type != 'run_left':
                    self.current_frame = 0
                    self.change_frames("Bosses/Demon/Run", 7)
                self.type = 'run_left'
            elif player.rect.x - (self.rect.x + self.image.get_width()) > 100 and (not self.isAttack) and (not self.isAttack2) and (not self.isAttack3):
                if self.type != 'run_right':
                    self.current_frame = 0
                    self.change_frames("Bosses/Demon/Run", 7)
                self.type = 'run_right'
            else:
                if self.power and (not self.attackCount):
                    attack = [1, 1, 1, 1, 2, 2, 2, 3, 3]
                    random.shuffle(attack)
                    if attack[0] == 1:
                        self.isAttack = True
                    elif attack[0] == 2:
                        self.isAttack2 = True
                    elif attack[0] == 3:
                        self.isAttack3 = True
                if self.type != 'idle':
                    self.current_frame = 0
                    self.change_frames("Bosses/Demon/Idle", 10)
                self.type = 'idle' 

    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))