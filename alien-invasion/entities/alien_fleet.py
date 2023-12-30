from typing import Tuple

import pygame
from pygame import Surface, Rect

from entities.alien import Alien
from entities.game_state import GameState
from settings import Settings


class AlienFleet:
    """A class tha represents a fleet of aliens that descend on the player"""

    # The margins, expressed in alien widths, to leave when filling the fleet
    MARGIN_BOTTOM: int = 4
    MARGIN_SIDES: int = 2

    # The spacing, expressed in multiples of alien widths/heights, to leave between aliens
    SPACE_HORIZONTAL: float = 1
    SPACE_VERTICAL: float = 1.5

    def __init__(self, game_state: GameState, settings: Settings, game_bounds: Rect):

        self._game_state = game_state
        self._settings = settings
        self._game_bounds = game_bounds

        # Load the alien image and get the rect
        self._alien_image = pygame.image.load("assets/images/alien.png").convert_alpha()
        self._alien_image = pygame.transform.scale_by(self._alien_image, .5)
        self._alien_rect = self._alien_image.get_rect()

        # Create a group for the aliens and set up the fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def has_landed(self):
        """Checks to see if any alien in the fleet has reached the bottom of the scree"""
        return any(alien.has_landed() for alien in self.aliens.sprites())

    def is_empty(self):
        """Determines if the fleet is empty"""
        return not self.aliens

    def render(self, screen: Surface):
        """Draws the fleet on the screen"""
        for alien in self.aliens.sprites():
            screen.blit(self._alien_image, alien.rect)

    def reset(self):
        """Recreates the alien fleet"""
        self._create_fleet()

    def update(self):
        """Updates the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Checks whether any alien in the fleet has hit the edge of the screen"""
        if any(alien.has_hit_edge() for alien in self.aliens.sprites()):
            self._descend_and_turn()

    def _create_fleet(self):
        """Creates the fleet of aliens"""

        # Ensure that the fleet is empty to start
        self.aliens.empty()

        # Fill the game bounds with aliens, iterating row by row
        alien_width, alien_height = self._alien_rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self._game_bounds.height - self.MARGIN_BOTTOM * alien_height):

            # Fill a row with aliens
            while current_x < (self._game_bounds.width - self.MARGIN_SIDES * alien_width):
                self._create_fleet_alien((current_x, current_y))
                current_x += self.SPACE_HORIZONTAL * alien_width

            # Finished a row; reset X and increment Y
            current_x = alien_width
            current_y += self.SPACE_VERTICAL * alien_height

    def _create_fleet_alien(self, location: Tuple[int, int]):
        """Creates an alien and places it at the specified location"""
        starting_rect = self._alien_rect.move(location)
        new_alien = Alien(self._game_state, self._game_bounds, starting_rect)
        self.aliens.add(new_alien)

    def _descend_and_turn(self):
        """Drops the entire fleet, and changes their direction"""
        for alien in self.aliens.sprites():
            alien.descend(self._settings.fleet_drop_speed)
        self._game_state.change_fleet_direction()
