class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullets_allowed = 10
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (252, 35, 45)

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Difficulty speed up
        self.speedup_scale = 1.2
