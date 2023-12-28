import sys

import pygame

from alien_fleet import AlienFleet
from bullet_volley import BulletVolley
from collision_manager import CollisionManager
from game_stats import GameStats
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""

        self.game_active = True

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

        # Create the game stats
        self.stats = GameStats(self.settings)

        # Create the ship
        self.ship = Ship(self.settings, self.screen)

        # Create the alien fleet
        self.alien_fleet = AlienFleet(self.settings, self.screen)

        # Create the bullet volley
        self.bullet_volley = BulletVolley(self.settings, self.screen, self.ship)

        # Create a new manager to resolve collisions between entities
        self.collision_manager = CollisionManager(self.ship, self.bullet_volley, self.alien_fleet, self.stats)

    def game_over(self):
        """Handles a game over condition"""
        self.game_active = False

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Check game events
            self._check_events()

            # If the game is active, handle all the updates
            if self.stats.ships_left > 0:

                # Update the ship
                self.ship.update()

                # Update the bullet volley
                self.bullet_volley.update()

                # Update the fleet
                self.alien_fleet.update()

                # Check and resolve collisions
                self.collision_manager.resolve_collisions()

            # Update the screen
            self._update_screen()

            # Run the game clock
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left()
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bullet_volley.add_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_LEFT:
            self.ship.stop_movement()
        elif event.key == pygame.K_RIGHT:
            self.ship.stop_movement()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Add the ship
        self.ship.render()

        # Add the bullets
        self.bullet_volley.render()

        # Add the aliens
        self.alien_fleet.render()

        # Make the most recently-drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
