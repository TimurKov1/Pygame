import os
import pygame
from .Functions import load_image
from .Bullet import Bullet
from .Ray import Ray


class Leaf(pygame.sprite.Sprite):
    def __init__(self, all_sprites, enemies, ground, fly, fly2):
        super().__init__(all_sprites)
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.frames = []
        self.ground = ground
        self.fly = fly
        self.fly2 = fly2
        self.change_frames("Characters/Leaf/Idle", 5)
        self.current_frame = 0
        self.type = 'idle'
        self.direction = 'right'
        self.image = pygame.transform.scale(self.frames[self.current_frame], (int(int(self.frames[self.current_frame].get_width() * 1.8)), int(int(self.frames[self.current_frame].get_height() * 1.8))))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 448 - self.image.get_height()
        self.speed = 7
        self.isJump = False
        self.isAttack = False
        self.isAttack2 = False
        self.isAttack3 = False
        self.attackEnergy = 7
        self.attack2Energy = 15
        self.attack3Energy = 50
        self.isBlock = False
        self.bullet = 0
        self.jumpCount = 13
        self.attackCount = 0
        self.attackX = 0
        self.power = 100
        self.countPower = 0
        self.loop = False
        self.changeLoop = False
        self.hp = 100
        self.isDead = False
        self.imageWidth = 0
        self.groundY = 0
        self.isGround = False

    def update(self):
        result = []
        for i in self.ground:
            if not pygame.sprite.collide_mask(self, i):
                result.append(True)
            else:
                self.groundY = i.rect.y
                result.append(False)
        for i in self.fly:
            if not pygame.sprite.collide_mask(self, i):
                result.append(True)
            else:
                if i.rect.x - 10 <= self.rect.x + self.image.get_width() // 2 <= i.rect.x + i.image.get_width():
                    self.groundY = i.rect.y
                    result.append(False)
        for i in self.fly2:
            if not pygame.sprite.collide_mask(self, i):
                result.append(True)
            else:
                if i.rect.x - 10 <= self.rect.x + self.image.get_width() // 2 <= i.rect.x + i.image.get_width():
                    self.groundY = i.rect.y
                    result.append(False)
        if all(result) and (not self.isGround) and (not self.isJump):
            self.isJump = True
            self.jumpCount = -1
            self.isGround = True
        if self.attackCount == len(self.frames):
            for enemy in self.enemies:
                if self.isAttack:
                    if self.rect.x <= enemy.rect.x <= self.rect.x + 10 + self.image.get_width():
                        enemy.hp -= 15
                        enemy.isDamaged = True
                        enemy.damageLoop = True
                    elif self.rect.x >= enemy.rect.x and self.rect.x <= enemy.rect.x + enemy.image.get_width() + 10:
                        enemy.hp -= 15
                        enemy.isDamaged = True
                        enemy.damageLoop = True
        if not self.isDead:
            if self.countPower == 20:
                if self.power < 100:
                    self.power += 1
                self.countPower = 0
            if self.bullet:
                for enemy in self.enemies:
                    if enemy != '':
                        if self.bullet.rect.x <= enemy.rect.x <= self.bullet.rect.x + self.bullet.image.get_width() and (not enemy.bulletDamaged):
                            enemy.hp -= 20
                            enemy.bulletDamaged = True
                            enemy.isDamaged = True
                            enemy.damageLoop = True
                            self.bullet = 0
                            self.loop = False
                            break
            else:
                for enemy in self.enemies:
                    if enemy != '':
                        enemy.bulletDamaged = False
            if self.isJump:
                if self.jumpCount == 13:
                    self.current_frame = 0

                if self.jumpCount >= 0:
                    self.change_frames("Characters/Leaf/Jump", 5)
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    if self.direction == 'right':
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                    else:
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                    self.rect.y -= int(self.jumpCount ** 2) // 6
                    self.jumpCount -= 1
                else:
                    if self.jumpCount > -6:
                        self.change_frames("Characters/Leaf/Fall", 5)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        if self.direction == 'right':
                            self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                        else:
                            self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                        self.rect.y += int(self.jumpCount ** 2) // 6
                        self.jumpCount -= 1
                    else:
                        result = []
                        for i in self.ground:
                            if not pygame.sprite.collide_mask(self, i):
                                result.append(True)
                            else:
                                self.groundY = i.rect.y
                                self.rect.y = self.groundY - self.image.get_height() + 32
                                result.append(False)
                        for i in self.fly:
                            if not pygame.sprite.collide_mask(self, i):
                                result.append(True)
                            else:
                                if i.rect.x - 10 <= self.rect.x + self.image.get_width() // 2 <= i.rect.x + i.image.get_width() + 10:
                                    self.groundY = i.rect.y
                                    result.append(False)
                                    self.rect.y = self.groundY - self.image.get_height() + 32
                        for i in self.fly2:
                            if not pygame.sprite.collide_mask(self, i):
                                result.append(True)
                            else:
                                if i.rect.x - 10 <= self.rect.x + self.image.get_width() // 2 <= i.rect.x + i.image.get_width() + 10:
                                    self.groundY = i.rect.y
                                    self.rect.y = self.groundY - self.image.get_height() + 32
                                    result.append(False)
                        if all(result):
                            self.change_frames("Characters/Leaf/Fall", 5)
                            self.current_frame = (self.current_frame + 1) % len(self.frames)
                            if self.direction == 'right':
                                self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                            else:
                                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                            self.rect.y += int(self.jumpCount ** 2) // 6
                            self.jumpCount -= 1
                        else:
                            self.isJump = False
                            self.jumpCount = 13
                            self.type = 'idle'
                            self.isGround = False
                            self.change_frames("Characters/Leaf/Idle", 5)
                            self.current_frame = (self.current_frame + 1) % len(self.frames)
                            if self.direction == 'right':
                                self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                            else:
                                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                            self.rect.y = self.groundY - self.image.get_height() + 32
            if self.isAttack and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                    self.imageWidth = self.image.get_width()
                if self.attackCount == len(self.frames):
                    self.isAttack = False
                    self.attackCount = 0
                    self.power -= 15
                    if self.type == 'idle':
                        self.change_frames("Characters/Leaf/Idle", 5)
                    else:
                        self.change_frames("Characters/Leaf/Run", 4)
                    return
                if self.changeLoop:
                    self.change_frames("Characters/Leaf/Attack1", 4)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8)))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8))), True, False)
                    self.rect.x = self.attackX + (self.imageWidth - self.image.get_width())
                self.attackCount += 1
            elif self.isAttack2 and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                    
                if self.attackCount == 30:
                    if self.direction == 'right':
                        self.bullet = Bullet(self.all_sprites, self.rect.x - self.image.get_width(), self.rect.y - 50, 50, 10, self.direction, "Characters/Leaf/Things/arrow.png")
                    else:
                        self.bullet = Bullet(self.all_sprites, self.rect.x - self.image.get_width() * 1.8, self.rect.y - 50, 50, 10, self.direction, "Characters/Leaf/Things/arrow.png")
                if self.attackCount == len(self.frames):
                    self.loop = True
                    self.attackCount = 0
                    self.isAttack2 = False
                    self.power -= 15
                    if self.type == 'idle':
                        self.change_frames("Characters/Leaf/Idle", 5)
                    else:
                        self.change_frames("Characters/Leaf/Run", 4)
                    return
                if self.changeLoop:
                    self.change_frames("Characters/Leaf/Attack2", 4)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8)))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8))), True, False)
                    self.rect.x = self.attackX + (self.imageWidth - self.image.get_width()) + 75
                self.attackCount += 1
            elif self.isAttack3 and (not self.isJump):
                if self.attackCount == 0:
                    self.attackX = self.rect.x
                if self.attackCount == len(self.frames):
                    self.isAttack3 = False
                    self.attackCount = 0
                    self.power -= 50
                    if self.type == 'idle':
                        self.change_frames("Characters/Leaf/Idle", 5)
                    else:
                        self.change_frames("Characters/Leaf/Run", 4)
                    return
                if self.attackCount == 45:
                    if self.direction == 'right':
                        self.ray = Ray(self.all_sprites, self.rect.x - self.image.get_width() + 230, self.rect.y - 40, 50)
                    else:
                        self.ray = Ray(self.all_sprites, self.rect.x - self.image.get_width() - 820, self.rect.y - 40, 50)
                    for enemy in self.enemies:
                        if self.direction == 'right' and self.rect.x <= enemy.rect.x <= self.rect.x + 600:
                            enemy.hp -= 50
                            enemy.isDamaged = True
                            enemy.damageLoop = True
                        elif self.direction == 'left' and self.rect.x >= enemy.rect.x >= self.rect.x - 600:
                            enemy.hp -= 50
                            enemy.isDamaged = True
                            enemy.damageLoop = True
                if self.changeLoop:
                    self.change_frames("Characters/Leaf/Attack3", 5)
                if self.direction == 'right':
                    self.image = pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8)))
                else:
                    self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.attackCount], (int(self.frames[self.attackCount].get_width() * 1.8), int(self.frames[self.attackCount].get_height() * 1.8))), True, False)
                    self.rect.x = self.attackX - self.image.get_width() + 92
                self.attackCount += 1
            else:
                if self.type == 'idle':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Leaf/Idle", 5)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        if self.direction == 'right':
                            self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                        else:
                            self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                if self.type == 'run_right':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Leaf/Run", 4)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
                    self.rect.x += self.speed
                if self.type == 'run_left':
                    if not self.isJump:
                        if self.changeLoop:
                            self.change_frames("Characters/Leaf/Run", 4)
                        self.current_frame = (self.current_frame + 1) % len(self.frames)
                        self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
                    if self.rect.x > 0:
                        self.rect.x -= self.speed
            self.countPower += 1
        else:
            if self.changeLoop:
                self.change_frames("Characters/Leaf/Death", 5)
                self.changeLoop = False
            if self.current_frame == len(self.frames):
                return
            if self.direction == 'right':
                self.image = pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8)))
            else:
                self.image = pygame.transform.flip(pygame.transform.scale(self.frames[self.current_frame], (int(self.frames[self.current_frame].get_width() * 1.8), int(self.frames[self.current_frame].get_height() * 1.8))), True, False)
            self.current_frame += 1
    
    def change_frames(self, path, speed):
        self.frames = []
        for i in range(len(os.listdir(f"Sprites/{path}"))):
            for j in range(speed):
                self.frames.append(load_image(f"{path}/{i + 1}.png"))