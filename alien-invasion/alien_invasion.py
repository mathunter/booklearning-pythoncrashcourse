import sys

import pygame

from alien_fleet import AlienFleet
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

        # Create the alien fleet
        self.alien_fleet = AlienFleet(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Check game events
            self._check_events()

            # Update the ship
            self.ship.update()

            # Update the bullets
            self._update_bullets()

            # Update the fleet
            self.alien_fleet.update()

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
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        # Add the ship
        self.ship.blitme()

        # Add the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Add the aliens
        self.alien_fleet.draw(self.screen)

        # Make the most recently-drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""

        # Update the bullet positions
        self.bullets.update()

        # Check for any bullets that have hit aliens
        pygame.sprite.groupcollide(self.bullets, self.alien_fleet.aliens, True, True)

        # If, after resolving collisions, there are no more aliens, create a new fleet
        if not self.alien_fleet.aliens:
            self.bullets.empty()
            self.alien_fleet.regenerate()

        # Remove bullets that have gone off the top of the screen
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
