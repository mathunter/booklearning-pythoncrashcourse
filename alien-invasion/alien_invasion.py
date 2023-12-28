import sys
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""

        # Initialize the game framework
        pygame.init()

        # Create a game clock
        self.clock = pygame.time.Clock()

        # Create a new settings instance
        self.settings = Settings()

        # Create the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the screen title
        pygame.display.set_caption("Alien Invasion")

        # Create the ship
        self.ship = Ship(self)

        # Create a group for the bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            # Check game events
            self._check_events()

            # Update the ship
            self.ship.update()

            # Update the bullets
            self.bullets.update()

            # Update the screen
            self._update_screen()

            # Run the game clock
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""

        # Watch for keyboard and mouse events
        for event in pygame.event.get():

            # Handle input events
            if event.type == pygame.QUIT:

                # Exit the application
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Respond to key releases"""

        # If the key is the left or right arrow, stop the ship moving in that direction
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _check_keydown_events(self, event):
        """Respond to keypresses"""

        # If the key is the left or right arrow, start the ship moving in that direction
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the group"""

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Add the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Add the ship
        self.ship.blitme()

        # Make the most recently-drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":

    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
