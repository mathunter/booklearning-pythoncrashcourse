import pygame
from pygame import Surface

from alien import Alien
from settings import Settings


class AlienFleet:

    def __init__(self, settings: Settings, screen: Surface):

        self.settings = settings
        self.screen = screen

        # Create a group for the aliens and set up the fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def has_landed(self):
        """Checks to see if any alien in the fleet has reached the bottom of the scree"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                return True

        return False

    def is_empty(self):
        """Determines if the fleet is empty"""
        return not self.aliens

    def render(self):
        """Draws the fleet on the screen"""
        self.aliens.draw(self.screen)

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
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """Checks whether any alien in the fleet has hit the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _create_fleet(self):
        """Creates the fleet of aliens"""

        # Ensure that the fleet is empty to start
        self.aliens.empty()

        # Create an alien and keep adding aliens until there's no room left,
        #  with a spacing between of one alien
        alien = Alien(self.settings, self.screen)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_fleet_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset X and increment Y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_fleet_alien(self, current_x, current_y):
        """Creates an alien and place it in the row"""

        # Create the alien and set its location based on the current X specified
        new_alien = Alien(self.settings, self.screen)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y
        self.aliens.add(new_alien)
