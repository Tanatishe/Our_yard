import pygame
from screen import Screen
from sounds import sounds


class Fighter:

    def __init__(self, x, y, reverse=False):
        self.x = x
        self.y = y
        self.coords = [self.x, self.y]
        self.image_now = self.image
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
        self.image_right = [[self.r1, self.r2], [pygame.transform.flip(self.r1, 1, 0),
                                                 pygame.transform.flip(self.r2, 1, 0)]]
        self.image_punch = [[self.r1, self.p], [pygame.transform.flip(self.r1, 1, 0),
                                                pygame.transform.flip(self.p, 1, 0)]]
        self.image_kick = [[self.k1, self.k2], [pygame.transform.flip(self.k1, 1, 0),
                                                pygame.transform.flip(self.k2, 1, 0)]]

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
        self.name = 'ВОВАН'
        self.image = pygame.image.load('images/vovka/vovan.png').convert_alpha()
        self.r1 = pygame.image.load('images/vovka/vovan_r1.png').convert_alpha()
        self.r2 = pygame.image.load('images/vovka/vovan_r2.png').convert_alpha()
        self.p = pygame.image.load('images/vovka/vovan_r_punch.png').convert_alpha()
        self.k1 = pygame.image.load('images/vovka/vovan_k1.png').convert_alpha()
        self.k2 = pygame.image.load('images/vovka/vovan_k2.png').convert_alpha()
        self.speed = 5
        super().__init__(x, y, reverse)


class Denya(Fighter):
    def __init__(self, x, y, reverse):
        self.max_hp = 120
        self.name = 'ДЕНЯ'
        self.image = pygame.image.load('images/denya/denya.png').convert_alpha()
        self.r1 = pygame.image.load('images/denya/denya_r1.png').convert_alpha()
        self.r2 = pygame.image.load('images/denya/denya_r2.png').convert_alpha()
        self.p = pygame.image.load('images/denya/denya_r_punch.png').convert_alpha()
        self.k1 = pygame.image.load('images/denya/denya_k1.png').convert_alpha()
        self.k2 = pygame.image.load('images/denya/denya_k2.png').convert_alpha()
        self.speed = 3
        super().__init__(x, y, reverse)


class Alex(Fighter):
    def __init__(self, x, y, reverse):
        self.max_hp = 90
        self.name = 'ЛЁХА'
        self.image = pygame.image.load('images/alex/alex.png').convert_alpha()
        self.r1 = pygame.image.load('images/alex/alex_r1.png').convert_alpha()
        self.r2 = pygame.image.load('images/alex/alex_r2.png').convert_alpha()
        self.p = pygame.image.load('images/alex/alex_p.png').convert_alpha()
        self.k1 = pygame.image.load('images/alex/alex_k1.png').convert_alpha()
        self.k2 = pygame.image.load('images/alex/alex_k2.png').convert_alpha()
        self.speed = 4
        super().__init__(x, y, reverse)
