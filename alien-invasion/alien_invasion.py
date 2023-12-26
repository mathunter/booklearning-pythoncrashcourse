import sys
import pygame

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

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            # Watch for keyboard and mouse events
            for event in pygame.event.get():

                # If the event type is to quit, exit the application
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Add the ship
            self.ship.blitme()
            
            # Make the most recently-drawn screen visible
            pygame.display.flip()

            # Run the game clock
            self.clock.tick(60)

if __name__ == "__main__":

    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
