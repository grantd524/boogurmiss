import pygame
from pygame.sprite import Sprite

#class to manage the bullets fired from the ship
class Bullets(Sprite):
    #initiliazes a bullet object and tracks the position on the screen
    def __init__(self,settings,screen,ship):
        super(Bullet. self).__init__()
        self.screen = screen

        #create bullet rectangle
        #create a rectangular bullet at 0,0
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        #move the bullet to the center/top of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = settings.bullet_colour

        #assign speed to bullets
        self.speed = settings.bullet_speed

        def update(self):
            #move the bullet up the screen
            self.y -= self.speed
            self.rect.y = self.y

        def draw_bullet(self):
            #draw bullet to screen
            pygame.draw.rect(self.screen, self.color, self.rect)
