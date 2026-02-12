import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        # Iterate through a list of new velocities, each based of the angle determined above, and create a baby based off of these values:
        for v in (self.velocity.rotate(angle)), (self.velocity.rotate(-angle)):
            baby = Asteroid(x, y, new_radius)
            baby.velocity = v * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
