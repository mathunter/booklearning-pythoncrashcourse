from pygame import Rect
from pygame.sprite import Sprite

from entities.game_state import GameState


class Alien(Sprite):
    """A class that represents a single alien in the fleet"""

    def __init__(self, game_state: GameState, game_bounds: Rect, starting_rect: Rect):
        super().__init__()

        self._game_state = game_state
        self._game_bounds = game_bounds

        self.rect = starting_rect
        self.x = float(self.rect.x)

    def descend(self, drop_speed: int):
        """Moves this alien down according to the specified drop speed"""
        self.rect.y += drop_speed

    def has_hit_edge(self):
        """Checks whether the alien has hit the edge of the screen"""
        return (self.rect.right >= self._game_bounds.right) or (self.rect.left <= self._game_bounds.left)

    def has_landed(self):
        """Determines if this alien has hit the bottom of the screen"""
        return self.rect.bottom >= self._game_bounds.bottom

    def update(self):
        """Moves the alien"""
        self.x += self._game_state.alien_speed * self._game_state.fleet_direction
        self.rect.x = self.x
