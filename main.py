import pygame
from game_config import *
from game import Game
from component import *


pygame.init()
DIGDUG = Game()
GAME = True
DONE = False

##
#resize
count = 0
while GAME is not DONE:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        DIGDUG.handle_event(event)
    DIGDUG.update()
    DIGDUG.screen.fill(BLACK)
    render(DIGDUG.screen)
    do_physics()
    pygame.display.flip()
