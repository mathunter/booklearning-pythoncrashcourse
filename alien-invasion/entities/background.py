import pygame

from pygame import Surface


class Background:

    def __init__(self, screen: Surface):
        self.__screen = screen
        self.__screen_rect = screen.get_rect()

        # Load the background image
        self.__stars_image = pygame.image.load("assets/images/bg.png")
        self.__stars_rect = self.__stars_image.get_rect()

        # Load the earth image
        self.__earth_image = pygame.image.load("assets/images/earth.png")
        self.__earth_rect = self.__earth_image.get_rect()
        self.__earth_rect.bottom = self.__screen_rect.bottom + (self.__earth_rect.height / 2)

    def render(self):
        """Draw the background"""
        self.__screen.blit(self.__stars_image, self.__stars_rect)
        self.__screen.blit(self.__earth_image, self.__earth_rect)
