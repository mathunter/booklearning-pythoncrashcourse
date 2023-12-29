import pygame
from pygame import Surface, Rect

from entities.game_state import GameState


class Ship:
    """A class to manage the ship"""

    MARGIN_BOTTOM = 10

    def __init__(self, game_state: GameState, bounds: Rect):

        self._game_state = game_state
        self._bounds = bounds

        # Movement directions
        self._moving_right = False
        self._moving_left = False

        # Load the ship image and get its rect
        self.image = pygame.image.load('assets/images/ship.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()

        # Start the ship in the center
        self._center_ship()

    def move_left(self):
        """Starts the ship moving to the left"""
        self._moving_left = True

    def move_right(self):
        """Starts the ship moving to the right"""
        self._moving_right = True

    def render(self, screen: Surface):
        """Draw the ship at its current location"""
        screen.blit(self.image, self.rect)

    def reset(self):
        """Resets the ship"""
        self._center_ship()

    def stop_movement(self):
        """Stops ship movement"""
        self._moving_left = False
        self._moving_right = False

    def update(self):
        """Update the ship's position based on the movement flags"""

        # Move left or right depending on the flags
        if self._moving_right and self.rect.right < self._bounds.right:
            self.x += self._game_state.ship_speed
        elif self._moving_left and self.rect.left > self._bounds.left:
            self.x -= self._game_state.ship_speed

        # Update the rect from the ship location
        self.rect.x = self.x

    def _center_ship(self):
        """Re-centers the ship in the middle of the screen"""
        self.rect.midbottom = (self._bounds.centerx, self._bounds.bottom - self.MARGIN_BOTTOM)
        self.x = float(self.rect.x)
