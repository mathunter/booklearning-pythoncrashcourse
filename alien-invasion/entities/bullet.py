from typing import Tuple

import pygame
from pygame import Rect
from pygame.sprite import Sprite

from entities.game_state import GameState


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game_state: GameState, bounds: Rect, starting_location: Tuple[int, int]):
        super().__init__()

        self._game_state = game_state

        # Create a bullet and set its correct position
        self.rect = pygame.Rect(0, 0, bounds.width, bounds.height)
        self.rect.midtop = starting_location

        # Store the bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""

        # Update the stored position of the bullet
        self.y -= self._game_state.bullet_speed

        # Update the display position
        self.rect.y = self.y
