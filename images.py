import pygame


images ={
    'fighters':{
        'VOVKA':{
            'main':pygame.image.load('images/vovka/vovan.png').convert_alpha(),
            'r1' : pygame.image.load('images/vovka/vovan_r1.png').convert_alpha(),
            'r2' : pygame.image.load('images/vovka/vovan_r2.png').convert_alpha(),
            'p' : pygame.image.load('images/vovka/vovan_r_punch.png').convert_alpha(),
            'k1' : pygame.image.load('images/vovka/vovan_k1.png').convert_alpha(),
            'k2' : pygame.image.load('images/vovka/vovan_k2.png').convert_alpha()
        },
        'DENYA':{
            'main':pygame.image.load('images/denya/denya.png').convert_alpha(),
            'r1' : pygame.image.load('images/denya/denya_r1.png').convert_alpha(),
            'r2' : pygame.image.load('images/denya/denya_r2.png').convert_alpha(),
            'p' : pygame.image.load('images/denya/denya_r_punch.png').convert_alpha(),
            'k1' : pygame.image.load('images/denya/denya_k1.png').convert_alpha(),
            'k2' : pygame.image.load('images/denya/denya_k2.png').convert_alpha()
        },
        'ALEX':{
            'main':pygame.image.load('images/alex/alex.png').convert_alpha(),
            'r1' : pygame.image.load('images/alex/alex_r1.png').convert_alpha(),
            'r2' : pygame.image.load('images/alex/alex_r2.png').convert_alpha(),
            'p' : pygame.image.load('images/alex/alex_p.png').convert_alpha(),
            'k1' : pygame.image.load('images/alex/alex_k1.png').convert_alpha(),
            'k2' : pygame.image.load('images/alex/alex_k2.png').convert_alpha()
        }

    }
}