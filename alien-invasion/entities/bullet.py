from typing import Tuple

import pygame
from pygame import Surface
from pygame.sprite import Sprite

from entities.game_state import GameState
from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game_state: GameState, settings: Settings, starting_location: Tuple[int, int]):
        super().__init__()

        self._game_state = game_state
        self._settings = settings
        self._color = self._settings.bullet_color

        # Create a bullet and set its correct position
        self.rect = pygame.Rect(0, 0, self._settings.bullet_width, self._settings.bullet_height)
        self.rect.midtop = starting_location

        # Store the bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""

        # Update the stored position of the bullet
        self.y -= self._game_state.bullet_speed

        # Update the display position
        self.rect.y = self.y

    def draw_bullet(self, screen: Surface):
        """Draw the bullet to the screen"""
        pygame.draw.rect(screen, self._color, self.rect)
