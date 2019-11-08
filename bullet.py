# A way of defining and shooting the bullet
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,screen,gs,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        # rectangele Drawn
        self.rect = pygame.Rect(0,0,gs.bullet_width,gs.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = gs.bullet_color
        self.speed = gs.bullet_speed

    # updating the position of bullets
    # it gets only one arg.
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.rect)




