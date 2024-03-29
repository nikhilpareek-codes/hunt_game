# A way to create alien on the screen
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,gs):
        super(Alien,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('alien.png')
        self.gs = gs
        self.rect = self.image.get_rect()
        # aligning the position of the ship(starting pos.)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    #     draw our alien
    def blitme(self):
        self.screen.blit(self.image,self.rect)




    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True

    def update(self):
        self.x += (self.gs.alien_speed*self.gs.fleet_direction)
        self.rect.x = self.x


