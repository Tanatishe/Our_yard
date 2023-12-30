import pygame

pygame.init()

from fighters import Fighter, Vovka, Denya, Alex
from screen import Screen, Fight_Screen, FPS, Choose_Screen, Start_screen, Loose_Screen

clock = pygame.time.Clock()

player1 = Vovka(100, 300, reverse=False)
player2 = Denya(980, 300, reverse=True)

now_screen = Start_screen()
now_screen = Choose_Screen()

while True:

    timer = now_screen.timer

    if timer < 0:
        player1.hp -= 0.1
        player2.hp -= 0.1

    if player1.hp <= 0:
        now_screen.flag = 2
    elif player2.hp <= 0:
        now_screen.flag = 3

    if now_screen.flag == 1:
        if now_screen.pl1_rect_count == 0:
            player1 = Vovka(100, 300, reverse=False)
        elif now_screen.pl1_rect_count == 1:
            player1 = Denya(100, 300, reverse=False)
        elif now_screen.pl1_rect_count == 2:
            player1 = Alex(100, 300, reverse=False)
        if now_screen.pl2_rect_count == 0:
            player2 = Vovka(980, 300, reverse=True)
        elif now_screen.pl2_rect_count == 1:
            player2 = Denya(980, 300, reverse=True)
        elif now_screen.pl2_rect_count == 2:
            player2 = Alex(980, 300, reverse=True)
        now_screen = Fight_Screen(player1, player2)
    elif now_screen.flag == 2:
        now_screen = Loose_Screen(player1)
        now_screen = Choose_Screen()
        player1.__init__(100, 300, reverse=False)
        player2.__init__(1000, 300, reverse=True)
        now_screen.flag = 0
        continue
    elif now_screen.flag == 3:
        now_screen = Loose_Screen(player2)
        now_screen = Choose_Screen()
        player1.__init__(100, 300, reverse=False)
        player2.__init__(1000, 300, reverse=True)
        now_screen.flag = 0
        continue

    news = pygame.event.get()
    for i in news:
        if i.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    now_screen.process_screen(player1, player2, news)

    now_screen.timer -= 1 / FPS

    pygame.display.update()

    clock.tick(FPS)
