from settings import Settings


class GameState:
    """A class that holds the game state for Alien Invasion"""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.ships_left = self.settings.ship_limit
        self.is_game_active = False

    def reset_state(self):
        """Resets the state for the game"""
        self.ships_left = self.settings.ship_limit
        self.is_game_active = False
