import math
import random

import pygame

from . import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, Layer, Point, font
from .enemy import Enemy
from .exit import Exit
from .floor import Floor
from .food import Food
from .game_object import GameObject, Transform
from .player import Player
from .wall import OuterWall, Wall
from .sprite import Sprite


class Gui(GameObject):
    height = 50
    width = 200

    def __init__(self, position):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert()
        self.image.fill((255, 255, 255))
        self.image.set_alpha(64)
        pygame.Surface.convert_alpha(self.image)
        sprite = Sprite([self.image])

        super(Gui, self).__init__(
            layer=Layer.GUI, transform=Transform(position), sprite=sprite)

    def update(self):
        text = font.render("Food : {}".format(scene.player.food), True, (0, 0, 0))
        self.image.fill((255, 255, 255))
        self.image.set_alpha(64)
        pygame.Surface.convert_alpha(self.image)
        self.image.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2))


class Scene(object):
    wall_count = (5, 9)
    food_count = (1, 5)

    def __init__(self, level):
        self.level = level
        self.player = None
        self.reset(level)

    def add(self, game_object):
        self.tiles[game_object.layer].append(game_object)

    def remove(self, game_object):
        self.tiles[game_object.layer].remove(game_object)

    def reset(self, level):
        self.level = level
        width, height = GRID_SIZE
        self.tiles = {layer: [] for layer in Layer}

        if self.player:
            self.player.transform.position = Point(1, height - 2)
        else:
            self.player = Player(Point(1, height - 2))
        self.add(self.player)

        # Place outer walls and floor
        for x in xrange(width):
            for y in xrange(height):
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    self.add(OuterWall(Point(x, y)))
                else:
                    self.add(Floor(Point(x, y)))

        grid_positions = [Point(x, y) for x in xrange(2, width - 2) for y in xrange(2, height - 2)]
        random.shuffle(grid_positions)

        # Place inside walls
        wall_count = random.randint(*self.wall_count)

        for _ in xrange(wall_count):
            self.add(Wall(grid_positions.pop()))

        # Place enemies
        enemy_count = int(math.log(self.level, 2))

        for _ in xrange(enemy_count):
            self.add(Enemy(grid_positions.pop(), kind=Enemy.random_kind()))

        # Place food
        food_count = random.randint(*self.food_count)

        for _ in xrange(food_count):
            self.add(Food(grid_positions.pop()))

        # Place exit
        self.add(Exit(Point(width - 2, 1)))

        # Display GUI
        self.gui = Gui(Point(SCREEN_WIDTH / 2 - Gui.width / 2, SCREEN_HEIGHT - Gui.height).to_grid())
        self.add(self.gui)

    def draw(self, surface):
        for layer in Layer:
            for tile in self.tiles[layer]:
                tile.draw(surface)

    def update(self):
        for layer in Layer:
            for tile in self.tiles[layer]:
                tile.update()

scene = Scene(3)
