from settings import Settings


class GameState:
    """A class that holds the game state for Alien Invasion"""

    def __init__(self, settings: Settings):
        self.settings = settings

        self.ships_left = None
        self.is_game_active = None
        self.ship_speed = None
        self.bullet_speed = None
        self.alien_speed = None
        self.fleet_direction = None
        self.game_score = None
        self.high_score = 0
        self.alien_points = None
        self.level = None

        self.reset()

    def change_fleet_direction(self):
        """Changes the fleet direction"""
        self.fleet_direction *= -1

    def increase_speed(self):
        """Increases the speed of the game by the configured scale"""
        speedup_scale = self.settings.speedup_scale
        score_scale = self.settings.score_scale
        self.ship_speed *= speedup_scale
        self.bullet_speed *= speedup_scale
        self.alien_speed *= speedup_scale
        self.alien_points = int(self.alien_points * score_scale)

    def reset(self):
        """Resets the state for the game"""
        self.ships_left = self.settings.ship_limit
        self.is_game_active = False
        self.ship_speed = self.settings.ship_speed
        self.bullet_speed = self.settings.bullet_speed
        self.alien_speed = self.settings.alien_speed
        self.fleet_direction = self.settings.fleet_direction
        self.game_score = 0
        self.alien_points = self.settings.alien_points
        self.level = 1
