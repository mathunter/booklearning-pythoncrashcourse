import pygame.font
from pygame import Surface

from game_state import GameState
from settings import Settings


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game_state: GameState, settings: Settings, screen: Surface):
        self.__game_state = game_state
        self.__settings = settings
        self.__screen = screen
        self.__screen_rect = screen.get_rect()

        # Set up the font settings for the score
        self.__text_color = (220, 220, 220)
        self.__font = pygame.font.SysFont(None, 48)

        # Prepare the initial font image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""

        # Get the score value
        rounded_score = round(self.__game_state.score, -1)
        score_str = f"{rounded_score:,}"

        # Convert the score string into an image
        self.__score_image = self.__font.render(score_str, True, self.__text_color, self.__settings.bg_color)
        self.__score_rect = self.__score_image.get_rect()

        # Set the score location
        self.__score_rect.right = self.__screen_rect.right - 20
        self.__score_rect.top = 20

    def render(self):
        """Renders the score to the screen"""
        self.__screen.blit(self.__score_image, self.__score_rect)
