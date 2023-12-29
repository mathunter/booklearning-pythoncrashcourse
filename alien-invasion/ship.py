import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position"""

        self.settings = settings
        self.screen = screen

        # Movement directions
        self.moving_right = False
        self.moving_left = False

        # Get the screen rect
        self.screen_rect = screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, .5)
        self.rect = self.image.get_rect()

        # Start the ship in the center
        self._center_ship()

    def move_left(self):
        """Starts the ship moving to the left"""
        self.moving_left = True

    def move_right(self):
        """Starts the ship moving to the right"""
        self.moving_right = True

    def render(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def reset(self):
        """Resets the ship"""
        self._center_ship()

    def stop_movement(self):
        """Stops ship movement"""
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flags"""

        # Move left or right depending on the flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect from the ship location
        self.rect.x = self.x

    def _center_ship(self):
        """Recenters the ship in the middle of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
