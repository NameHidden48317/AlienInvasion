import pygame


class Mario:
    """A class to manage Mario"""

    def __init__(self, ai_game):
        """Initilize Mario and set its starting point."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/mario.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw mario at its current location"""
        self.screen.blit(self.image, self.rect)