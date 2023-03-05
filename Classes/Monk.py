import os
import pygame
from .Functions import load_image


class Monk(pygame.sprite.Sprite):
    def __init__(self, all_sprites, enemies, ground, fly, fly2):
        super().__init__(all_sprites)
        self.frames = []
        self.enemies = enemies
        self.change_frames("Characters/Monk/Idle", 5)
        self.current_frame = 0
        self.type = 'idle'
        self.direction = 'right'
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500 - self.image.get_height()
        self.power = 100
        self.speed = 8
        self.isJump = False
        self.isAttack = False
        self.isAttack2 = False
        self.isAttack3 = False
        self.attackEnergy = 7
        self.attack2Energy = 25
        self.attack3Energy = 50
        self.isBlock = False
        self.jumpCount = 15
        self.attackCount = 0
        self.attackX = 0
        self.count = 0
        self.changeLoop = False
        self.hp = 100
        self.isDead = False
        self.imageWidth = 0

    def update(self):
        if self.attackCount == len(self.frames):
            for enemy in self.enemies:
                if self.isAttack:
                    if self.rect.x <= enemy.rect.x <= self.rect.x + 40 + self.image.get_width() and self.direction == 'right':
                        enemy.hp -= 20
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                    elif self.rect.x >= enemy.rect.x and self.rect.x <= enemy.rect.x + enemy.image.get_width() + 40 and self.direction == 'left':
                        enemy.hp -= 20
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                if self.isAttack2:
                    if self.rect.x <= enemy.rect.x <= self.rect.x + 250 + self.image.get_width() and self.direction == 'right':
                        enemy.hp -= 40
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                    elif self.rect.x >= enemy.rect.x and self.rect.x <= enemy.rect.x + enemy.image.get_width() + 250 and self.direction == 'left':
                        enemy.hp -= 40
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                if self.isAttack3:
                    if self.rect.x <= enemy.rect.x <= self.rect.x + 100 + self.image.get_width() and self.direction == 'right':
                        enemy.hp -= 70
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                    elif self.rect.x >= enemy.rect.x and self.rect.x <= enemy.rect.x + enemy.image.get_width() + 100 and self.direction == 'left':
                        enemy.hp -= 70
                        enemy.isDamaged = True
                        enemy.damageLoop = True
        if not self.isDead:
            if self.count == 15:
                if self.power < 100:
                    self.power += 1
                self.count = 0
            if self.isJump:
                if self.jumpCount == 15:
                    self.current_frame = 0
                if self.jumpCount >= 0:
                    self.change_frames("Characters/Monk/Jump", 5)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    if self.direction == 'right':
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
                    else:
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3)), True, False)
                else:
                    self.change_frames("Characters/Monk/Fall", 5)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    if self.direction == 'right':
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
                    else:
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3)), True, False)
                if self.jumpCount >= -15:
                    if self.jumpCount < 0:
                        self.rect.y += (self.jumpCount ** 2) // 6
                    else:
                        self.rect.y -= (self.jumpCount ** 2) // 6
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 15
                    self.type = 'idle'
                    self.change_frames("Characters/Monk/Idle", 5)
            if self.isAttack and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                    self.imageWidth = self.image.get_width()
                if self.attackCount == len(self.frames):
                    self.isAttack = False
                    self.attackCount = 0
                    self.power -= 7
                    self.change_frames("Characters/Monk/Idle", 5)
                    return
                if self.changeLoop:
                    self.change_frames("Characters/Monk/Attack1", 4)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3)), True, False)
                    self.rect.x = self.attackX + (self.imageWidth - self.image.get_width())
                self.attackCount += 1
            elif self.isAttack2 and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                    self.imageWidth = self.image.get_width()
                if self.attackCount == len(self.frames):
                    self.isAttack2 = False
                    self.attackCount = 0
                    self.power -= 25
                    self.change_frames("Characters/Monk/Idle", 5)
                    return
                if self.changeLoop:
                    self.change_frames("Characters/Monk/Attack2", 4)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3)), True, False)
                    self.rect.x = self.attackX + (self.imageWidth - self.image.get_width())
                self.attackCount += 1
            elif self.isAttack3 and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                    self.imageWidth = self.image.get_width()
                if self.attackCount == len(self.frames):
                    self.isAttack3 = False
                    self.attackCount = 0
                    self.power -= 50
                    self.change_frames("Characters/Monk/Idle", 5)
                    return
                if self.changeLoop:
                    self.change_frames("Characters/Monk/Attack3", 4)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (self.frames[self.attackCount].get_width() * 3, self.frames[self.attackCount].get_height() * 3)), True, False)
                    self.rect.x = self.attackX + (self.imageWidth - self.image.get_width())
                self.attackCount += 1
            else:
                if self.type == 'idle':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Monk/Idle", 5)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        if self.direction == 'right':
                            self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
                        else:
                            self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3)), True, False)
                if self.type == 'run_right':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Monk/Run", 4)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
                    self.rect.x += self.speed
                if self.type == 'run_left':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Monk/Run", 4)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3)), True, False)
                    if self.rect.x > 0:
                        self.rect.x -= self.speed
            self.count += 1
        else:
            if self.changeLoop:
                self.change_frames("Characters/Monk/Death", 5)
                self.changeLoop = False
            if self.current_frame == len(self.frames):
                return
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (self.frames[self.current_frame].get_width() * 3, self.frames[self.current_frame].get_height() * 3)), True, False)
            self.current_frame += 1
    
    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))