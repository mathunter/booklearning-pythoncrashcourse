import pygame
from pygame import Surface, Rect

from entities.alien import Alien
from entities.game_state import GameState
from settings import Settings


class AlienFleet:
    """A class tha represents a fleet of aliens that descend on the player"""

    def __init__(self, game_state: GameState, settings: Settings, bounds: Rect):

        self._game_state = game_state
        self._settings = settings
        self._bounds = bounds

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
        self.aliens.draw(screen)

    def reset(self):
        """Recreates the alien fleet"""
        self._create_fleet()

    def update(self):
        """Updates the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _change_fleet_direction(self):
        """Drops the entire fleet, and changes their direction"""
        for alien in self.aliens.sprites():
            alien.descend()
        self._game_state.change_fleet_direction()

    def _check_fleet_edges(self):
        """Checks whether any alien in the fleet has hit the edge of the screen"""
        if any(alien.has_hit_edge() for alien in self.aliens.sprites()):
            self._change_fleet_direction()

    def _create_fleet(self):
        """Creates the fleet of aliens"""

        # Ensure that the fleet is empty to start
        self.aliens.empty()

        # Create an alien to get the size of the alien image, then create the fleet
        #  with a spacing between of one alien
        alien = Alien(self._game_state, self._settings, self._bounds)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self._bounds.height - 4 * alien_height):
            while current_x < (self._bounds.width - 2 * alien_width):
                self._create_fleet_alien(current_x, current_y)
                current_x += alien_width

            # Finished a row; reset X and increment Y
            current_x = alien_width
            current_y += 1.5 * alien_height

    def _create_fleet_alien(self, current_x, current_y):
        """Creates an alien and place it in the row"""

        # Create the alien and set its location based on the current X specified
        new_alien = Alien(self._game_state, self._settings, self._bounds)
        new_alien.x = current_x
        new_alien.rect.topleft = (current_x, current_y)
        self.aliens.add(new_alien)
