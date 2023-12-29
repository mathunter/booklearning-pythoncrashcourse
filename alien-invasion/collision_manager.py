from time import sleep

import pygame

from alien_fleet import AlienFleet
from bullet_volley import BulletVolley
from game_stats import GameStats
from ship import Ship


class CollisionManager:

    def __init__(self, ship: Ship, volley: BulletVolley, alien_fleet: AlienFleet, stats: GameStats):
        """Initializes this instance"""

        self.ship = ship
        self.volley = volley
        self.alien_fleet = alien_fleet
        self.stats = stats

    def resolve_collisions(self):
        """Checks for and resolves collisions between entities"""
        self._check_bullet_alien_collisions()
        self._check_ship_alien_collisions()
        self._check_aliens_landed()

    def _check_aliens_landed(self):
        """Checks whether any aliens have reached the bottom of the screen"""
        if self.alien_fleet.has_landed():
            self._handle_ship_hit()

    def _check_bullet_alien_collisions(self):
        """Checks for any collisions between bullets and aliens"""

        # Check and resolve the collisions
        pygame.sprite.groupcollide(self.volley.bullets, self.alien_fleet.aliens, True, True)

        # If, after resolving collisions, there are no more aliens, create a new fleet
        if self.alien_fleet.is_empty():
            self.volley.reset()
            self.alien_fleet.reset()

    def _check_ship_alien_collisions(self):
        """Checks for any collisions between the ship and aliens"""

        # Check for a collision and handle a ship hit
        if pygame.sprite.spritecollideany(self.ship, self.alien_fleet.aliens):
            self._handle_ship_hit()

    def _handle_ship_hit(self):
        """Handles the case where the ship is hit"""

        # Decrement the number of ships left
        self.stats.ships_left -= 1

        # If there are any ships remaining, reset the game
        if self.stats.ships_left >= 0:
            # Reset the bullet volley
            self.volley.reset()

            # Reset the alien fleet
            self.alien_fleet.reset()

            # Reset the ship
            self.ship.reset()

            # Pause
            sleep(0.5)
