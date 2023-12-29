import pygame
from pygame import Surface

from entities.bullet import Bullet
from entities.game_state import GameState
from entities.ship import Ship
from settings import Settings


class BulletVolley:

    def __init__(self, game_state: GameState, settings: Settings, ship: Ship):

        self._game_state = game_state
        self._settings = settings
        self._ship = ship

        # Create a group for the bullets in the volley
        self.bullets = pygame.sprite.Group()

    def add_bullet(self):
        """Creates a new bullet and adds it to the group"""
        if self._game_state.is_game_active and len(self.bullets) < self._settings.bullets_allowed:
            new_bullet = Bullet(self._game_state, self._settings, self._ship.rect.midtop)
            self.bullets.add(new_bullet)

    def render(self, screen: Surface):
        """Draws the bullets to the screen"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet(screen)

    def reset(self):
        """Resets this instance"""
        self.bullets.empty()

    def update(self):
        """Update the position of bullets and get rid of old bullets"""

        # Update the bullet positions
        self.bullets.update()

        # Check and remove bullets that have gone off-screen
        self._check_offscreen_bullets()

    def _check_offscreen_bullets(self):
        """Checks for and removes bullets that have gone beyond the top of the screen"""
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
