import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 0xFFFFFF, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x - self.radius > SCREEN_WIDTH:
            self.position.x = -self.radius
        elif self.position.x + self.radius < 0:
            self.position.x = SCREEN_WIDTH + self.radius
        if self.position.y - self.radius > SCREEN_HEIGHT:
            self.position.y = -self.radius
        elif self.position.y + self.radius < 0:
            self.position.y = SCREEN_HEIGHT + self.radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
        x, y = self.position[0], self.position[1]
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(x, y, radius)
        asteroid_2 = Asteroid(x, y, radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2
