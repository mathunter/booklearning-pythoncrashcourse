import pygame.font
from pygame import Surface

from entities.game_state import GameState
from settings import Settings


class Scoreboard:
    """A class to report scoring information"""

    FONT_COLOR = (200, 200, 200)
    FONT_SIZE = 24

    MARGIN = 20

    def __init__(self, game_state: GameState, settings: Settings, screen: Surface):
        self.__game_state = game_state
        self.__settings = settings
        self.__screen = screen
        self.__screen_rect = screen.get_rect()

        # Set up the font settings for the score
        self.__font = pygame.font.Font("assets/fonts/retro_space_inv.ttf", self.FONT_SIZE)

        # Prepare the displays
        self.prep_game_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def check_high_score(self):
        """Checks to see if there's a new high score, and assigns the game score to the high score, if so"""
        if self.__game_state.game_score > self.__game_state.high_score:
            self.__game_state.high_score = self.__game_state.game_score
            self.prep_high_score()

    def prep_game_score(self):
        """Prepares the game score for display by turning it into a rendered image"""

        # Get the value
        rounded_score = round(self.__game_state.game_score, -1)

        # Convert the string into an image
        self.__game_score_image = self._render_score_image(f"game: {rounded_score:,}")
        self.__game_score_rect = self.__game_score_image.get_rect()

        # Set the location
        self.__game_score_rect.topleft = (self.MARGIN, self.MARGIN)

    def prep_high_score(self):
        """Prepares the high score for display by turning it into a rendered image"""

        # Get the value
        rounded_score = round(self.__game_state.high_score, -1)

        # Convert the string into an image
        self.__high_score_image = self._render_score_image(f"high: {rounded_score:,}")
        self.__high_score_rect = self.__high_score_image.get_rect()

        # Set the location
        self.__high_score_rect.topright = (self.__screen_rect.right - self.MARGIN, self.MARGIN)

    def prep_level(self):
        """Prepares the level for display by turning it into a rendered image"""

        # Get the value
        level = self.__game_state.level

        # Convert the string into an image
        self.__level_image = self._render_score_image(f"level: {level:,}")
        self.__level_rect = self.__level_image.get_rect()

        # Set the location
        self.__level_rect.midtop = (int(self.__screen_rect.width / 3), self.MARGIN)

    def prep_lives(self):
        """Prepares the number of lives for display by turning it into a rendered image"""

        # Get the value
        lives = self.__game_state.ships_left

        # Convert the string into an image
        self.__lives_image = self._render_score_image(f"lives: {lives:,}")
        self.__lives_rect = self.__lives_image.get_rect()

        # Set the location
        self.__lives_rect.midtop = (int(self.__screen_rect.width / 3) * 2, self.MARGIN)

    def render(self):
        """Renders the score to the screen"""
        self.__screen.blit(self.__game_score_image, self.__game_score_rect)
        self.__screen.blit(self.__high_score_image, self.__high_score_rect)
        self.__screen.blit(self.__level_image, self.__level_rect)
        self.__screen.blit(self.__lives_image, self.__lives_rect)

    def reset(self):
        """Resets the scoreboard, by re-preparing the score and level displays"""
        self.prep_game_score()
        self.prep_level()
        self.prep_lives()

    def _render_score_image(self, score_str):
        """Renders the specified score string to an image"""
        return self.__font.render(score_str, True, self.FONT_COLOR, self.__settings.bg_color)

