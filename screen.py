from pygame.locals import *
import pygame
from sounds import sounds
from images import images, screen, WIDTH, HEIGHT
from random import randint as rand

FPS = 60
PUNCH_LONG = 60
JUMP_LONG = 71

clock1 = pygame.time.Clock()

font_test = pygame.font.Font('fonts/Tana_Uncial_SP/TanaUncialSP.otf', 200)
font_test1 = pygame.font.Font('fonts/Tana_Uncial_SP/TanaUncialSP.otf', 100)
font = pygame.font.Font(size=60)
font2 = pygame.font.Font(size=50)
flags = RESIZABLE | SCALED


class Screen:
    screen = screen

    FPS = FPS

    def __init__(self):
        self.timer = 120
        pygame.display.set_caption('Our yard Alpha 0.4')
        pygame.display.set_icon(pygame.image.load("images/loh.ico"))
        self.flag = 0


class Fight_Screen(Screen):

    def __init__(self, player1, player2):
        self.back = images['arenas'][rand(0, len(images['arenas']) - 1)]
        super().__init__()
        sounds['effects']['fight'].play()
        pygame.mixer.music.load('sounds/show_falls_Lisa.mp3')
        pygame.mixer.music.play(-1)
        clock1.tick(0.5)
        self.text1 = font.render(player1.name, True, 'White', 'Black')
        self.text2 = font.render(player2.name, True, 'White', 'Black')
        self.text_tip1 = font2.render('wasd fg', True, 'White', 'Black')
        self.text_tip2 = font2.render('arrows num1 num3', True, 'White', 'Black')
        self.hp_bar1 = pygame.Surface((player1.max_hp * 4, 50))
        self.hp_bar1.fill('Red')
        self.hp_bar2 = pygame.Surface((player2.max_hp * 4, 50))
        self.hp_bar2.fill('Red')

    def process_screen(self, player1, player2, news):

        if self.timer > 0:
            text_timer = font.render(str(int(self.timer)), True, 'Gold')
        else:
            text_timer = font.render('0', True, 'Gold')

        hp_bar1_current = pygame.Surface((player1.hp * 4, 50))
        hp_bar1_current.fill('Green')
        hp_bar2_current = pygame.Surface((player2.hp * 4, 50))
        hp_bar2_current.fill('Green')
        self.screen.blit(self.back, (0, 0))
        self.screen.blit(self.text1, (50, 10))
        self.screen.blit(self.text2, (1050, 10))
        self.screen.blit(self.text_tip1, (100, HEIGHT - 50))
        self.screen.blit(self.text_tip2, (900, HEIGHT - 50))
        self.screen.blit(player1.image_now, (player1.x, player1.y))
        self.screen.blit(player2.image_now, (player2.x, player2.y))
        self.screen.blit(self.hp_bar1, (50, 50))
        self.screen.blit(hp_bar1_current, (50, 50))
        self.screen.blit(self.hp_bar2, (WIDTH - player2.max_hp * 4 - 50, 50))
        self.screen.blit(hp_bar2_current, (WIDTH - player2.hp * 4 - 50, 50))
        self.screen.blit(text_timer, (600, 10))

        key = pygame.key.get_pressed()

        # move
        if player1.punch_counter == 0 and player1.kick_counter == 0 and key[pygame.K_d]:
            player1.move_right()
        elif player1.punch_counter == 0 and player1.kick_counter == 0 and key[pygame.K_a]:
            player1.move_left()
        player1.back_counter -= 1
        if player2.punch_counter == 0 and player2.kick_counter == 0 and key[pygame.K_LEFT]:
            player2.move_left()
        elif player2.punch_counter == 0 and player2.kick_counter == 0 and key[pygame.K_RIGHT]:
            player2.move_right()
        player1.back_counter -= 1
        if player1.back_counter < 1:
            player1.image_now = player1.image[player1.reverse]
        player2.back_counter -= 1
        if player2.back_counter < 1:
            player2.image_now = player2.image[player2.reverse]

        # jump
        if player1.jump_counter == 0 and (key[pygame.K_SPACE] or key[pygame.K_w]):
            player1.jump_counter = JUMP_LONG
        if player1.jump_counter != 0:
            player1.jump()
        if player2.jump_counter == 0 and key[pygame.K_UP]:
            player2.jump_counter = JUMP_LONG
        if player2.jump_counter != 0:
            player2.jump()

        # punch
        if player1.jump_counter == 0 and player1.punch_counter == 0 and player1.kick_counter == 0 and key[pygame.K_f]:
            player1.punch_counter = PUNCH_LONG
        if player1.punch_counter != 0:
            player1.punch(player2)
        if player2.jump_counter == 0 and player2.punch_counter == 0 and player2.kick_counter == 0 and key[pygame.K_KP1]:
            player2.punch_counter = PUNCH_LONG
        if player2.punch_counter != 0:
            player2.punch(player1)

        # kick
        if player1.jump_counter == 0 and player1.punch_counter == 0 and player1.kick_counter == 0 and key[pygame.K_g]:
            player1.kick_counter = PUNCH_LONG
        if player1.kick_counter != 0:
            player1.kick(player2)
        if player2.jump_counter == 0 and player2.punch_counter == 0 and player2.kick_counter == 0 and key[pygame.K_KP3]:
            player2.kick_counter = PUNCH_LONG
        if player2.kick_counter != 0:
            player2.kick(player1)

        # reverse
        if player1.x > player2.x:
            player1.reverse = True
            player2.reverse = False
        else:
            player2.reverse = True
            player1.reverse = False


class Choose_Screen(Screen):
    back = pygame.image.load('images/choose.jpg').convert()

    def __init__(self):
        super().__init__()
        pygame.mixer.music.load('sounds/zaglavnaja-tema-mortal-kombat-8-bit.mp3')
        pygame.mixer.music.play(-1)
        sounds['effects']['choose'].play()
        self.back = pygame.transform.scale(self.back, (self.back.get_width() * 2, self.back.get_height() * 2))
        self.text1 = font.render('CHOOSE UR HERO', True, 'White', 'Black')
        self.rect_text1 = self.text1.get_rect(center=(WIDTH // 2, 30))
        self.text_tip1 = font2.render('ENTER and NUM_ENTER for choise', True, 'White', 'Black')
        self.rect_text_tip1 = self.text_tip1.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.hero1 = pygame.Surface((100, 100))
        self.hero2 = pygame.Surface((100, 100))
        self.hero3 = pygame.Surface((100, 100))
        self.hero1.blit(pygame.image.load('images/vovka/ava.jpeg').convert(), (0, 0))
        self.hero2.blit(pygame.image.load('images/denya/ava.jpg').convert(), (0, 0))
        self.hero3.blit(pygame.image.load('images/alex/ava.JPG').convert(), (0, 0))
        self.pl1 = pygame.Surface((100, 100), )
        pygame.draw.rect(self.pl1, 'Gold', (0, 0, 100, 100))
        self.pl1.set_alpha(128)
        self.pl1_rect_count = 0
        self.pl1_rect_coord = [(330, 400), (560, 420), (830, 440)][self.pl1_rect_count]
        self.pl1_rect = self.pl1.get_rect(topleft=self.pl1_rect_coord)
        self.pl1_text = font2.render('P1', True, 'White', 'Black')
        self.pl1.blit(self.pl1_text, (0, 0))
        self.pl2 = pygame.Surface((100, 100), )
        pygame.draw.rect(self.pl2, 'Gold', (0, 0, 100, 100))
        self.pl2.set_alpha(128)
        self.pl2_rect_count = 2
        self.pl2_rect_coord = [(330, 400), (560, 420), (830, 440)][self.pl2_rect_count]
        self.pl2_rect = self.pl2.get_rect(topleft=self.pl2_rect_coord)
        self.pl2_text = font2.render('P2', True, 'White', 'Black')
        self.pl2.blit(self.pl2_text, (0, 0))

    def process_count_pl1(self, n):
        self.pl1_rect_count += n
        if self.pl1_rect_count < 0:
            self.pl1_rect_count = 2
        elif self.pl1_rect_count > 2:
            self.pl1_rect_count = 0

    def process_count_pl2(self, n):
        self.pl2_rect_count += n
        if self.pl2_rect_count < 0:
            self.pl2_rect_count = 2
        elif self.pl2_rect_count > 2:
            self.pl2_rect_count = 0

    def process_screen(self, player1, player2, news):

        self.pl1_rect_coord = [(330, 400), (560, 420), (830, 440)][self.pl1_rect_count]
        self.pl1_rect = self.pl1.get_rect(topleft=self.pl1_rect_coord)
        self.pl2_rect_coord = [(330, 400), (560, 420), (830, 440)][self.pl2_rect_count]
        self.pl2_rect = self.pl2.get_rect(topleft=self.pl2_rect_coord)

        self.screen.blit(self.back, (0, 0))
        self.screen.blit(self.text1, self.rect_text1)
        self.screen.blit(self.text_tip1, self.rect_text_tip1)
        self.screen.blit(self.hero1, (330, 400))
        self.screen.blit(self.hero2, (560, 420))
        self.screen.blit(self.hero3, (830, 440))
        self.screen.blit(self.pl1, self.pl1_rect)
        self.screen.blit(self.pl2, self.pl2_rect)

        for i in news:
            if i.type == pygame.KEYDOWN:
                if not player1.choose_flag:
                    if i.key == pygame.K_d:
                        self.process_count_pl1(n=1)
                    elif i.key == pygame.K_a:
                        self.process_count_pl1(n=-1)
                    elif i.key == pygame.K_RETURN:
                        player1.choose_flag = True
                        sounds['effects']['choise'].play()
                if not player2.choose_flag:
                    if i.key == pygame.K_RIGHT:
                        self.process_count_pl2(n=1)
                    elif i.key == pygame.K_LEFT:
                        self.process_count_pl2(n=-1)
                    elif i.key == pygame.K_KP_ENTER:
                        player2.choose_flag = True
                        sounds['effects']['choise'].play()

        if self.timer < 3:
            player1.choose_flag = True
            player2.choose_flag = True
            sounds['effects']['choise'].play()

        if player1.choose_flag and player2.choose_flag:
            self.flag = 1


class Start_screen(Screen):

    def process_start_screen(self):
        sounds['effects']['ha'].play()
        self.screen.blit(self.text1, self.rect_text1)

        pygame.display.update()
        clock1.tick(0.2)

    def __init__(self):
        super().__init__()
        self.text1 = font_test.render('Our Yard', True, 'Red', 'Black')
        self.rect_text1 = self.text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.process_start_screen()


class Loose_Screen(Screen):

    def process_screen(self):
        sounds['effects']['ha'].play()
        self.screen.blit(self.text1, self.rect_text1)
        self.screen.blit(self.text2, self.rect_text2)
        self.screen.blit(self.text3, self.rect_text3)

        pygame.display.update()
        flag = False
        while True:
            if flag:
                break
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    break
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_RETURN or i.key == pygame.K_KP_ENTER:
                        flag = True
                        break

    def __init__(self, looser):
        super().__init__()
        self.text1 = font_test.render('LOOSE', True, 'Red', 'Black')
        self.rect_text1 = self.text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.text2 = font_test1.render(looser.name, True, 'Red', 'Black')
        self.rect_text2 = self.text2.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        self.text3 = font2.render('Press ENTER to continue', True, 'White', 'Black')
        self.rect_text3 = self.text2.get_rect(center=(WIDTH // 2, 3 * (HEIGHT // 4)))

        self.process_screen()


class Menu_Screen(Screen):

    def process_count_frame(self, n):
        self.frame_rect_count += n
        if self.frame_rect_count < 0:
            self.frame_rect_count = 2
        elif self.frame_rect_count > 2:
            self.frame_rect_count = 0

    def process_screen(self):
        sounds['effects']['che'].play()

        flag = False
        while True:
            self.t_option1 = font2.render('option1', True, self.colors[self.frame_rect_count == 0])
            self.t_option2 = font2.render('option2', True, self.colors[self.frame_rect_count == 1])
            self.t_option3 = font2.render('option3', True, self.colors[self.frame_rect_count == 2])
            self.surf.blit(self.t_option1, self.t_option1_rect)
            self.surf.blit(self.t_option2, self.t_option2_rect)
            self.surf.blit(self.t_option3, self.t_option3_rect)

            self.screen.blit(self.surf, self.surf_rect)

            pygame.display.update(self.surf)

            if flag:
                break
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    break
                if i.type == pygame.KEYDOWN:
                    if i.key == K_ESCAPE:
                        flag = True
                        break
                    elif i.key in [K_RIGHT, K_DOWN, K_s, K_d]:
                        self.process_count_frame(1)

                    elif i.key in [K_LEFT, K_UP, K_w, K_a]:
                        self.process_count_frame(-1)

    def __init__(self, screen):
        self.screen = screen
        self.w = 300
        self.h = 400
        self.surf = pygame.Surface((self.w, self.h))
        self.surf_rect = self.surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.t_menu = font2.render('MENU', True, 'White')
        self.t_menu_rect = self.t_menu.get_rect(centerx=self.w // 2)
        self.colors = ('White', 'Gold')
        self.t_option1 = font2.render('option1', True, 'White')
        self.t_option1_rect = self.t_option1.get_rect(center=(self.w // 2, 100))
        self.t_option2 = font2.render('option2', True, 'White')
        self.t_option2_rect = self.t_option2.get_rect(center=(self.w // 2, 200))
        self.t_option3 = font2.render('option3', True, 'White')
        self.t_option3_rect = self.t_option3.get_rect(center=(self.w // 2, 300))
        self.frame_rect_count = 0
        self.surf.blit(self.t_menu, self.t_menu_rect)
        self.surf.blit(self.t_option1, self.t_option1_rect)
        self.surf.blit(self.t_option2, self.t_option2_rect)
        self.surf.blit(self.t_option3, self.t_option3_rect)
        self.process_screen()
