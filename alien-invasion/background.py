import pygame
from pygame import Surface

from settings import Settings


class Background:

    def __init__(self, screen: Surface):
        """Initializes this instance"""

        self.screen = screen

        # Load the background image
        self.image = pygame.image.load("images/bg.png")
        self.rect = self.image.get_rect()

    def render(self):
        """Draw the background"""
        self.screen.blit(self.image, self.rect)


