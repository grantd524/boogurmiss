
class Settings():
    # a class to store all settings for alien invasion

    def __init__(self):

        # screen settings
        self.bg_colour = (75,120,203)
        self.screen_width = (800)
        self.screen_height = (600)


        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255,0,0)

        #player settings
        self.lives = 3
        self.score = 0

        #play game
        self.game_active = False
