import pygame

from . import BACKGROUND, screen
from .scene import scene


class GameManager(object):

    def update(self):
        scene.update()

    def draw(self):
        screen.fill(BACKGROUND)
        scene.draw(screen)
        pygame.display.flip()
