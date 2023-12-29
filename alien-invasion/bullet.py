from typing import Tuple

import pygame
from pygame import Surface
from pygame.sprite import Sprite

from settings import Settings


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, settings: Settings, screen: Surface, starting_location: Tuple[int, int]):
        super().__init__()

        self.__screen = screen
        self.__settings = settings
        self.__color = self.__settings.bullet_color

        # Create a bullet and set its correct position
        self.rect = pygame.Rect(0, 0, self.__settings.bullet_width, self.__settings.bullet_height)
        self.rect.midtop = starting_location

        # Store the bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""

        # Update the stored position of the bullet
        self.y -= self.__settings.bullet_speed

        # Update the display position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.__screen, self.__color, self.rect)
