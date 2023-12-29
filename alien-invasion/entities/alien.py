import pygame
from pygame import Rect
from pygame.sprite import Sprite

from entities.game_state import GameState
from settings import Settings


class Alien(Sprite):
    """A class that represents a single alien in the fleet"""

    def __init__(self, game_state: GameState, settings: Settings, bounds: Rect):
        super().__init__()

        self._bounds = bounds
        self._game_state = game_state
        self._settings = settings

        # Load the alien image and get the rect
        self.image = pygame.image.load("assets/images/alien.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.center = (self.rect.width, self.rect.height)

        # Store the alien's x position
        self.x = float(self.rect.x)

    def descend(self):
        """Moves this alien down according to the drop speed of the fleet"""
        self.rect.y += self._settings.fleet_drop_speed

    def has_hit_edge(self):
        """Checks whether the alien has hit the edge of the screen"""
        return (self.rect.right >= self._bounds.right) or (self.rect.left <= 0)

    def has_landed(self):
        """Determines if this alien has hit the bottom of the screen"""
        return self.rect.bottom >= self._settings.screen_height

    def update(self):
        """Move the alien"""
        self.x += self._game_state.alien_speed * self._game_state.fleet_direction
        self.rect.x = self.x
