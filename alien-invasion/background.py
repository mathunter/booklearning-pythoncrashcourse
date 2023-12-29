import pygame

from pygame import Surface


class Background:

    def __init__(self, screen: Surface):
        self.__screen = screen

        # Load the background image
        self.__image = pygame.image.load("images/bg.png")
        self.__rect = self.__image.get_rect()

    def render(self):
        """Draw the background"""
        self.__screen.blit(self.__image, self.__rect)
