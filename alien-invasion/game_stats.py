from settings import Settings


class GameStats:
    """A class that holds the game stats for Alien Invasion"""

    def __init__(self, settings: Settings):
        """Initializes the game statistics"""
        self.settings = settings
        self.ships_left = self.settings.ship_limit

    def reset_stats(self):
        """Resets the stats for the game"""
        self.ships_left = self.settings.ship_limit
