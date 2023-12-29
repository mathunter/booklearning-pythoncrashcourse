from typing import Tuple

import pygame.font

from pygame import Surface


class Button:
    """A class to build buttons for the game"""

    def __init__(self, center: Tuple[int, int], message: str):

        # Set the dimensions and properties
        self._width, self.height = 200, 50
        self._button_color = (0, 135, 0)
        self._text_color = (255, 255, 255)
        self._font = pygame.font.Font("assets/fonts/retro_space_inv.ttf", 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self._width, self.height)
        self.rect.center = center

        # Prep the button message
        self._prep_message(message)

    def render(self, screen: Surface):
        """Renders the button on-screen"""
        screen.fill(self._button_color, self.rect)
        screen.blit(self.message_image, self.message_image_rect)

    def _prep_message(self, message):
        """Converts the specified message into a rendered image"""
        self.message_image = self._font.render(message, True, self._text_color, self._button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center
