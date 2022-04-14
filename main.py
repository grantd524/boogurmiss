#grant davis
#import library for pygame
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

#define main game function
def alien_invasion():
    #initialize library pygame
    pygame.init()
    #
    settings = Settings()
    #creates our display by inputting width and height of display
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    #
    pygame.display.set_caption('Alien Invasion')
    #add ship
    ship = Ship(screen)


    #make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #loop to start animation
    while True:

        #access event handler
        gf.check_events(ship)
        #updates screen
        gf.update_screen(settings, screen, ship, bullets)
        # make an alien
        a&walien = Alien(settings, screen)
        a&walien.blitme()

        bullets.updtate()
alien_invasion()
