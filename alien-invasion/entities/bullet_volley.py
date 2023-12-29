import pygame
from pygame import Surface

from entities.bullet import Bullet
from entities.game_state import GameState
from entities.ship import Ship
from settings import Settings


class BulletVolley:

    def __init__(self, game_state: GameState, settings: Settings, screen: Surface, ship: Ship):

        self.__game_state = game_state
        self.__settings = settings
        self.__screen = screen
        self.__ship = ship

        # Create a group for the bullets in the volley
        self.bullets = pygame.sprite.Group()

    def add_bullet(self):
        """Creates a new bullet and adds it to the group"""
        if self.__game_state.is_game_active and len(self.bullets) < self.__settings.bullets_allowed:
            new_bullet = Bullet(self.__game_state, self.__settings, self.__screen, self.__ship.rect.midtop)
            self.bullets.add(new_bullet)

    def render(self):
        """Draws the bullets to the screen"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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
