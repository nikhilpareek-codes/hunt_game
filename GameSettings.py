# A module containing all game settings

class Settings():
    def __init__(self):
        # Screen settings
        self.width = 1000
        self.height = 600
        self.caption = "Hunt The Alien"
        self.color = (230,230,230)
        self.speed = 2.5
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_speed = 1.5
        self.bullet_color = 0,0,255
#     Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 6
#         1-> Right -1 -> Left
        self.fleet_direction = 1



