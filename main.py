import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clk = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black", rect=None, special_flags=0)
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()

        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()