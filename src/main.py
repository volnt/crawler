import sys

import pygame

from . import BACKGROUND, clock, screen, Point
from .scene import scene


def main():
    while 42:
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    scene.player.move(Point(-1, 0))
                    scene.update()
                if event.key == pygame.K_RIGHT:
                    scene.player.move(Point(1, 0))
                    scene.update()
                if event.key == pygame.K_UP:
                    scene.player.move(Point(0, -1))
                    scene.update()
                if event.key == pygame.K_DOWN:
                    scene.player.move(Point(0, 1))
                    scene.update()

        screen.fill(BACKGROUND)
        scene.draw(screen)
        pygame.display.flip()
