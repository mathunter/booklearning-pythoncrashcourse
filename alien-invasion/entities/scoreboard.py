import pygame.font
from pygame import Surface

from entities.game_state import GameState
from settings import Settings


class Scoreboard:
    """A class to report scoring information"""

    FONT_COLOR = (200, 200, 200)
    FONT_SIZE = 24

    def __init__(self, game_state: GameState, settings: Settings, screen: Surface):
        self.__game_state = game_state
        self.__settings = settings
        self.__screen = screen
        self.__screen_rect = screen.get_rect()

        # Set up the font settings for the score
        self.__font = pygame.font.Font("assets/fonts/retro_space_inv.ttf", self.FONT_SIZE)

        # Prepare the initial font image
        self.prep_game_score()
        self.prep_high_score()

    def check_high_score(self):
        """Checks to see if there's a new high score"""
        if self.__game_state.game_score > self.__game_state.high_score:
            self.__game_state.high_score = self.__game_state.game_score
            self.prep_high_score()

    def prep_game_score(self):
        """Turn the score into a rendered image"""

        # Get the score value
        rounded_score = round(self.__game_state.game_score, -1)

        # Convert the score string into an image
        self.__game_score_image = self._render_score_image(f"game: {rounded_score:,}")
        self.__game_score_rect = self.__game_score_image.get_rect()

        # Set the score location
        self.__game_score_rect.left = 20
        self.__game_score_rect.top = 20

    def prep_high_score(self):
        """Turn the score into a rendered image"""

        # Get the score value
        rounded_score = round(self.__game_state.high_score, -1)

        # Convert the score string into an image
        self.__high_score_image = self._render_score_image(f"high: {rounded_score:,}")
        self.__high_score_rect = self.__high_score_image.get_rect()

        # Set the score location
        self.__high_score_rect.right = self.__screen_rect.right - 20
        self.__high_score_rect.top = 20

    def render(self):
        """Renders the score to the screen"""
        self.__screen.blit(self.__game_score_image, self.__game_score_rect)
        self.__screen.blit(self.__high_score_image, self.__high_score_rect)

    def _render_score_image(self, score_str):
        """Renders the specified score string to an image"""
        return self.__font.render(score_str, True, self.FONT_COLOR, self.__settings.bg_color)
