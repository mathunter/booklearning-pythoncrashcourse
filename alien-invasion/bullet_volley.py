import pygame
from pygame import Surface

from bullet import Bullet
from settings import Settings
from ship import Ship


class BulletVolley:

    def __init__(self, settings: Settings, screen: Surface, ship: Ship):
        """Initializes this instance"""

        self.settings = settings
        self.screen = screen
        self.ship = ship

        # Create a group for the bullets in the volley
        self.bullets = pygame.sprite.Group()

    def add_bullet(self):
        """Creates a new bullet and adds it to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.ship.rect.midtop)
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
