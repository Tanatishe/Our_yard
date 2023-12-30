import pygame
from screen import Screen
from sounds import sounds
from images import images


class Fighter:

    def __init__(self, x, y, reverse=False):
        self.x = x
        self.y = y
        self.coords = [self.x, self.y]
        self.reverse = reverse
        self.rect = pygame.Rect([(self.x, self.y, 100, 360), (self.x + 100, self.y, 100, 360)][self.reverse])
        self.hitbox = pygame.Surface((100, 360))
        self.hp = self.max_hp
        self.choose_flag = False
        self.counter = 1
        self.back_counter = 0
        self.jump_counter = 0
        self.punch_counter = 0
        self.kick_counter = 0
        self.image = (images['fighters'][self.name]['main'],
                      pygame.transform.flip(images['fighters'][self.name]['main'],1,0))
        self.image_right = ((images['fighters'][self.name]['r1'], images['fighters'][self.name]['r2']),
                            (pygame.transform.flip(images['fighters'][self.name]['r1'], 1, 0),
                             pygame.transform.flip(images['fighters'][self.name]['r2'], 1, 0)))
        self.image_punch = ((images['fighters'][self.name]['r1'], images['fighters'][self.name]['p']),
                            (pygame.transform.flip(images['fighters'][self.name]['r1'], 1, 0),
                             pygame.transform.flip(images['fighters'][self.name]['p'], 1, 0)))
        self.image_kick = ((images['fighters'][self.name]['k1'], images['fighters'][self.name]['k2']),
                            (pygame.transform.flip(images['fighters'][self.name]['k1'], 1, 0),
                             pygame.transform.flip(images['fighters'][self.name]['k2'], 1, 0)))
        self.image_now = self.image[self.reverse]

    def move_right(self):

        if self.x < 1080:
            self.x += self.speed
            self.rect.x += self.speed
        self.image_now = self.image_right[self.reverse][int(self.counter) % 2]
        self.counter += 0.1
        self.back_counter = 10

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
            self.rect.x -= self.speed
        self.image_now = self.image_right[self.reverse][int(self.counter) % 2]
        self.counter += 0.1
        self.back_counter = 10

    def jump(self):
        if self.jump_counter == 55:
            sounds['fighter']['jump'].play()
        if self.jump_counter > 0:
            self.y -= 6
        else:
            self.y += 6
        self.jump_counter -= 2
        if self.jump_counter < -71:
            self.jump_counter = 0

    def punch(self, enemy):
        if self.punch_counter == 30:
            sounds['fighter']['punch'].play()
            enemy.rect = pygame.Rect([(enemy.x, enemy.y, 100, 360), (enemy.x + 100, enemy.y, 100, 360)][enemy.reverse])
            if enemy.rect.collidepoint((self.x + 100) + [100, -100][self.reverse], self.y + 100):
                enemy.hp -= 10
                sounds['effects']['ai'].play()
        if self.punch_counter > 30:
            self.image_now = self.image_punch[self.reverse][0]
        else:
            self.image_now = self.image_punch[self.reverse][1]
        self.punch_counter -= 1
        self.back_counter = 10

    def kick(self, enemy):
        if self.kick_counter == 30:
            sounds['fighter']['kick'].play()
            enemy.rect = pygame.Rect([(enemy.x, enemy.y, 100, 360), (enemy.x + 100, enemy.y, 100, 360)][enemy.reverse])
            if enemy.rect.collidepoint((self.x + 100) + [100, -100][self.reverse], self.y + 100):
                enemy.hp -= 20
                sounds['effects']['balls'].play()
        if self.kick_counter > 30:
            self.image_now = self.image_kick[self.reverse][0]
        else:
            self.image_now = self.image_kick[self.reverse][1]
        self.kick_counter -= 1
        self.back_counter = 10


class Vovka(Fighter):
    def __init__(self, x, y, reverse):
        self.max_hp = 80
        self.name = 'VOVKA'
        self.speed = 5
        super().__init__(x, y, reverse)


class Denya(Fighter):
    def __init__(self, x, y, reverse):
        self.max_hp = 120
        self.name = 'DENYA'
        self.speed = 3
        super().__init__(x, y, reverse)


class Alex(Fighter):
    def __init__(self, x, y, reverse):
        self.max_hp = 90
        self.name = 'ALEX'
        self.speed = 4
        super().__init__(x, y, reverse)
