import enum

import pygame

from .sprite import SpriteSheet

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
GRID_SIZE = GRID_WIDTH, GRID_HEIGHT = 10, 10
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = SCREEN_WIDTH / GRID_WIDTH, SCREEN_HEIGHT / GRID_HEIGHT
SPRITE_SIZE = SPRITE_WIDTH, SPRITE_HEIGHT = 32, 32
BACKGROUND = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
spritesheet = SpriteSheet("assets/Scavengers_SpriteSheet.png", SPRITE_SIZE, CELL_SIZE)
font = pygame.font.Font(None, 24)


class Layer(enum.Enum):
    FLOOR = 0
    BLOCKING = 1
    DEFAULT = 2
    GUI = 3


class Tag(enum.Enum):
    PLAYER = 0
    ENEMY = 1
    WALL = 2
    FLOOR = 3
    FOOD = 4
    SODA = 5
    EXIT = 6


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_absolute(self):
        return Point(int(self.x * CELL_WIDTH), int(self.y * CELL_HEIGHT))

    def to_grid(self):
        return Point(float(self.x) / CELL_WIDTH, float(self.y) / CELL_HEIGHT)

    def to_tuple(self):
        return (self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def __bool__(self):
        return self.x or self.y
