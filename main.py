import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock, dt = pygame.time.Clock(), 0
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()