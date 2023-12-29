import pygame.font

from pygame import Surface


class Button:
    """A class to build buttons for the game"""

    def __init__(self, screen: Surface, message: str):
        self.__screen = screen
        self.__screen_rect = self.__screen.get_rect()

        # Set the dimensions and properties
        self.__width, self.height = 200, 50
        self.__button_color = (0, 135, 0)
        self.__text_color = (255, 255, 255)
        self.__font = pygame.font.Font("assets/fonts/retro_space_inv.ttf", 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.__width, self.height)
        self.rect.center = self.__screen_rect.center

        # Prep the button message
        self._prep_message(message)

    def render(self):
        """Renders the button on-screen"""
        self.__screen.fill(self.__button_color, self.rect)
        self.__screen.blit(self.message_image, self.message_image_rect)

    def _prep_message(self, message):
        """Converts the specified message into a rendered image"""
        self.message_image = self.__font.render(message, True, self.__text_color, self.__button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center
