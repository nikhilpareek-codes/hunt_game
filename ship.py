# A Module for ship class containing all t=of the settings and files
import pygame
class Ship():
    def __init__(self,screen):
        self.image = pygame.image.load('ship.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # aligning the position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # flag movement
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        # floating thr position seamless navigation
        self.rect.centerx = float(self.rect.centerx)
        self.rect.top = float(self.rect.top)
        self.rect.bottom = float(self.rect.bottom)
    #     update position of the ship
    def update(self,gs):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += gs.speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= gs.speed
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.rect.top -= gs.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += gs.speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)

