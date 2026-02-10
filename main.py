import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initialize pygame
    pygame.init()
    # Create clock object so our game doesn't run as fast as CPU allows.
    clock = pygame.time.Clock()
    dt = 0
    # Get a GUI window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create some goups for classes to keep things tidy.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Put things in groups:
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    # Instantiate a player object:
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Instantiate a asteroid field!
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            # Close the window if close button is pressed:
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        # Update everything in the updatables group:
        updatable.update(dt)
        # Check for collisions:
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        # Loop over everything in the drawables group and draw them:
        for drawing in drawable:
            drawing.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # Pause to limit to 60 fps and capture delta time for other purposes.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
