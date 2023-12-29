import pygame
from pygame import Surface
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):
    """A class that represents a single alien in the fleet"""

    def __init__(self, settings: Settings, screen: Surface):
        super().__init__()

        self.__screen = screen
        self.__settings = settings

        # Load the alien image and get the rect
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's x position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Checks whether the alien is at the edge of the screen"""
        screen_rect = self.__screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien"""
        self.x += self.__settings.alien_speed * self.__settings.fleet_direction
        self.rect.x = self.x
