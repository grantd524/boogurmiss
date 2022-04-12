import pygame
import sys
from bullets import Bullets


#this function checks for key/mouse events and responds
def check_events(ship):
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key is pressed we end game
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            if event.key == pygame.K_LEFT:
                ship.moving_left = True

            if event.key == pygame.K_DOWN:
                ship.moving_down = True

            if event.key == pygame.K_UP:
                ship.moving_up = True

            if event.key == pygame.K_SPACE:
                new_bullet = Bullets(settings, screen, ship)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False
            if event.key == pygame.K_UP:
                ship.moving_up = False

        def keydown_event(event, ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True

        def keyup_event(event, ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    #color the screen with background color
    # color screen with background color
    screen.fill(settings.bg_colour)

    # draw ship on scteen
    ship.blitme()

    #update the ship
    ship.update()

    #draw bullets on screen
    for bullet in bullets.sprite():
        bullet.draw_bullet()
    # updating the display
    pygame.display.flip()

    a&walien.blitme()

    pygamme.display.flip()

    def create_fleet(settings, screen, aliens):
        #create a fleet of aliens
        alien = Alien(settings, screen)
        alien_width = alien.rect.width

    for alien_number in range(alien.number_of_aliens)
        alien = Alien(settings, screen)
        alien.x = 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

    def check_collisions(bullets, aliens):
        pygae.sprite.groupcollide(bullets, aliens, True, True)
