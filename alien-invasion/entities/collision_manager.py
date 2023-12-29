from time import sleep

import pygame

from entities.alien_fleet import AlienFleet
from entities.bullet_volley import BulletVolley
from entities.game_state import GameState
from entities.scoreboard import Scoreboard
from entities.ship import Ship


class CollisionManager:

    def __init__(self, ship: Ship, bullet_volley: BulletVolley, alien_fleet: AlienFleet, game_state: GameState,
                 scoreboard: Scoreboard):

        self._ship = ship
        self._bullet_volley = bullet_volley
        self._alien_fleet = alien_fleet
        self._game_state = game_state
        self._scoreboard = scoreboard

    def resolve_collisions(self):
        """Checks for and resolves collisions between entities"""
        self._check_bullet_alien_collisions()
        self._check_ship_alien_collisions()
        self._check_aliens_landed()

    def _check_aliens_landed(self):
        """Checks whether any aliens have reached the bottom of the screen"""
        if self._alien_fleet.has_landed():
            self._handle_ship_hit()

    def _check_bullet_alien_collisions(self):
        """Checks for any collisions between bullets and aliens"""

        # Check and resolve the collisions
        collisions = pygame.sprite.groupcollide(self._bullet_volley.bullets, self._alien_fleet.aliens, True, True)

        # If an alien was hit, increment the score by the number of aliens hit
        if collisions:
            for aliens in collisions.values():
                self._game_state.game_score += self._game_state.alien_points * len(aliens)
            self._scoreboard.prep_game_score()
            self._scoreboard.check_high_score()

        # If, after resolving collisions, there are no more aliens, create a new fleet
        if self._alien_fleet.is_empty():
            self._bullet_volley.reset()
            self._alien_fleet.reset()
            self._game_state.increase_speed()
            self._game_state.level += 1
            self._scoreboard.prep_level()

    def _check_ship_alien_collisions(self):
        """Checks for any collisions between the ship and aliens"""

        # Check for a collision and handle a ship hit
        if pygame.sprite.spritecollideany(self._ship, self._alien_fleet.aliens):
            self._handle_ship_hit()

    def _handle_ship_hit(self):
        """Handles the case where the ship is hit"""

        # Decrement the number of ships left
        self._game_state.ships_left -= 1
        self._scoreboard.prep_lives()

        # If there are ships remaining, reset the game
        if self._game_state.ships_left > 0:
            # Reset all entities
            self._bullet_volley.reset()
            self._ship.reset()
            self._alien_fleet.reset()

            # Pause
            sleep(0.5)

        # If there are no ships remaining, end the game
        if self._game_state.ships_left <= 0:
            # Deactivate the game
            self._game_state.is_game_active = False

            # Show the mouse cursor
            pygame.mouse.set_visible(True)
