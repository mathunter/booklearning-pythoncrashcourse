import pygame

from pygame import Surface, Rect


class Background:
    """A class that renders the background of the game"""

    def __init__(self, bounds: Rect):
        # Load the background image
        self._stars_image = pygame.image.load("assets/images/bg.png")
        self._stars_rect = self._stars_image.get_rect()

        # Load the earth image
        self._earth_image = pygame.image.load("assets/images/earth.png")
        self._earth_rect = self._earth_image.get_rect()
        self._earth_rect.bottom = bounds.bottom + (self._earth_rect.height / 2)

    def render(self, screen: Surface):
        """Draw the background"""
        screen.blit(self._stars_image, self._stars_rect)
        screen.blit(self._earth_image, self._earth_rect)
