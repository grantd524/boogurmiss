import pygame

class Ship():

    def __init__(self, screen):

        #load image of ship and access image data
        self.image = pygame.image.load("images/mug2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set starting location of each ship
        #makes centerx value of ship same centerx value of screen
        self.rect.centerx = self.screen_rect.centerx
        #makes bottom of ship same as bottom of screen
        self.rect.bottom = self.screen_rect.bottom

        # stores centerx of ship as decimal value
        self.center = float(self.rect.centerx)

        #create movememnt flag to determine if ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        #draw the ship on screen
        #image.blit image being added and self.rect is the location
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1
        elif self.moving_left and self.rect.left > 0:
            self.center -= 1
        if self.moving_down and self.rect.down < self.screen_rect.down:
            self.center += 1
        elif self.moving_up and self.rect.up > 0:
            self.center -= 1


        self.rect.centerx = self.center
