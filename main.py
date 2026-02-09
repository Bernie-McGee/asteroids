import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
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
    # Add Player classes to groups.
    Player.containers = (updatable, drawable)
    # Instantiate a player object:
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
        # Loop over everything in the drawables group and draw them:
        for drawing in drawable:
            drawing.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # Pause to limit to 60 fps and capture delta time for other purposes.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
