# Start the game , the main file to define our game
import pygame
import sys
from GameSettings import Settings
from ship import Ship
import GameFunctions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    pygame.init()
    gs = Settings()
    screen = pygame.display.set_mode((gs.width,gs.height))
    pygame.display.set_caption(gs.caption)
    ship = Ship(screen)
    bullets = Group()
    alien = Alien(screen,gs)
    aliens = Group()
    gf.create_fleet(gs,screen,aliens,ship)
    # Main loop
    while True:
        gf.chk_events(ship,screen,gs,bullets)
        gf.update_aliens(aliens, gs)
        gf.update(gs,ship,screen,bullets,aliens)

run_game()




