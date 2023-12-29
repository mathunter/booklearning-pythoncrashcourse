from time import sleep

import pygame

from alien_fleet import AlienFleet
from bullet_volley import BulletVolley
from game_state import GameState
from scoreboard import Scoreboard
from ship import Ship


class CollisionManager:

    def __init__(self, ship: Ship, bullet_volley: BulletVolley, alien_fleet: AlienFleet, game_state: GameState,
                 scoreboard: Scoreboard):

        self.__ship = ship
        self.__bullet_volley = bullet_volley
        self.__alien_fleet = alien_fleet
        self.__game_state = game_state
        self.__scoreboard = scoreboard

    def resolve_collisions(self):
        """Checks for and resolves collisions between entities"""
        self._check_bullet_alien_collisions()
        self._check_ship_alien_collisions()
        self._check_aliens_landed()

    def _check_aliens_landed(self):
        """Checks whether any aliens have reached the bottom of the screen"""
        if self.__alien_fleet.has_landed():
            self._handle_ship_hit()

    def _check_bullet_alien_collisions(self):
        """Checks for any collisions between bullets and aliens"""

        # Check and resolve the collisions
        collisions = pygame.sprite.groupcollide(self.__bullet_volley.bullets, self.__alien_fleet.aliens, True, True)

        # If an alien was hit, increment the score by the number of aliens hit
        if collisions:
            for aliens in collisions.values():
                self.__game_state.score += self.__game_state.alien_points * len(aliens)
            self.__scoreboard.prep_score()

        # If, after resolving collisions, there are no more aliens, create a new fleet
        if self.__alien_fleet.is_empty():
            self.__bullet_volley.reset()
            self.__alien_fleet.reset()
            self.__game_state.increase_speed()

    def _check_ship_alien_collisions(self):
        """Checks for any collisions between the ship and aliens"""

        # Check for a collision and handle a ship hit
        if pygame.sprite.spritecollideany(self.__ship, self.__alien_fleet.aliens):
            self._handle_ship_hit()

    def _handle_ship_hit(self):
        """Handles the case where the ship is hit"""

        # Decrement the number of ships left
        self.__game_state.ships_left -= 1

        # If there are ships remaining, reset the game
        if self.__game_state.ships_left > 0:
            # Reset all entities
            self.__bullet_volley.reset()
            self.__ship.reset()
            self.__alien_fleet.reset()

            # Pause
            sleep(0.5)

        # If there are no ships remaining, end the game
        if self.__game_state.ships_left <= 0:
            # Deactivate the game
            self.__game_state.is_game_active = False

            # Show the mouse cursor
            pygame.mouse.set_visible(True)
