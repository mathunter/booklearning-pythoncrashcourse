import pygame.font
from pygame import Surface, Rect

from entities.game_state import GameState
from settings import Settings


class Scoreboard:
    """A class to report scoring information"""

    FONT_COLOR = (200, 200, 200)
    FONT_SIZE = 24

    MARGIN = 20

    def __init__(self, game_state: GameState, settings: Settings, bounds: Rect):
        self._game_state = game_state
        self._settings = settings
        self._bounds = bounds

        # Set up the font settings for the score
        self._font = pygame.font.Font("assets/fonts/retro_space_inv.ttf", self.FONT_SIZE)

        # Prepare the displays
        self.prep_game_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def check_high_score(self):
        """Checks to see if there's a new high score, and assigns the game score to the high score, if so"""
        if self._game_state.game_score > self._game_state.high_score:
            self._game_state.high_score = self._game_state.game_score
            self.prep_high_score()

    def prep_game_score(self):
        """Prepares the game score for display by turning it into a rendered image"""

        # Get the value
        rounded_score = round(self._game_state.game_score, -1)

        # Convert the string into an image
        self._game_score_image = self._render_score_image(f"game: {rounded_score:,}")
        self._game_score_rect = self._game_score_image.get_rect()

        # Set the location
        self._game_score_rect.topleft = (self.MARGIN, self.MARGIN)

    def prep_high_score(self):
        """Prepares the high score for display by turning it into a rendered image"""

        # Get the value
        rounded_score = round(self._game_state.high_score, -1)

        # Convert the string into an image
        self._high_score_image = self._render_score_image(f"high: {rounded_score:,}")
        self._high_score_rect = self._high_score_image.get_rect()

        # Set the location
        self._high_score_rect.topright = (self._bounds.right - self.MARGIN, self.MARGIN)

    def prep_level(self):
        """Prepares the level for display by turning it into a rendered image"""

        # Get the value
        level = self._game_state.level

        # Convert the string into an image
        self._level_image = self._render_score_image(f"level: {level:,}")
        self._level_rect = self._level_image.get_rect()

        # Set the location
        self._level_rect.midtop = (int(self._bounds.width / 3), self.MARGIN)

    def prep_lives(self):
        """Prepares the number of lives for display by turning it into a rendered image"""

        # Get the value
        lives = self._game_state.ships_left

        # Convert the string into an image
        self._lives_image = self._render_score_image(f"lives: {lives:,}")
        self._lives_rect = self._lives_image.get_rect()

        # Set the location
        self._lives_rect.midtop = (int(self._bounds.width / 3) * 2, self.MARGIN)

    def render(self, screen: Surface):
        """Renders the score to the screen"""
        screen.blit(self._game_score_image, self._game_score_rect)
        screen.blit(self._high_score_image, self._high_score_rect)
        screen.blit(self._level_image, self._level_rect)
        screen.blit(self._lives_image, self._lives_rect)

    def reset(self):
        """Resets the scoreboard, by re-preparing the score and level displays"""
        self.prep_game_score()
        self.prep_level()
        self.prep_lives()

    def _render_score_image(self, score_str):
        """Renders the specified score string to an image"""
        return self._font.render(score_str, True, self.FONT_COLOR, self._settings.bg_color)

