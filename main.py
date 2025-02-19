import pygame

from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clk = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black", rect=None, special_flags=0)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()