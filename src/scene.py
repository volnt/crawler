import math
import random

import pygame

from . import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, Layer, Point, font
from .enemy import Enemy
from .exit import Exit
from .floor import Floor
from .food import Food
from .player import Player
from .wall import OuterWall, Wall
from .sprite import Sprite


class Gui(object):
    height = 50
    width = 200
    layer = Layer.GUI

    def __init__(self, position):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert()
        self.image.fill((255, 255, 255))
        self.image.set_alpha(64)
        pygame.Surface.convert_alpha(self.image)
        self.sprite = Sprite([self.image])
        self.position = position

    def update(self):
        pass

    def draw(self, surface):
        self.text = font.render("Level {} | Food {}".format(scene.level, scene.player.food), True, (0, 0, 0))
        self.image.fill((255, 255, 255))
        self.image.set_alpha(64)
        pygame.Surface.convert_alpha(self.image)
        self.image.blit(self.text, (self.width / 2 - self.text.get_width() / 2,
                                    self.height / 2 - self.text.get_height() / 2))
        surface.blit(self.image, self.position.to_tuple())


class Scene(object):
    wall_count = (5, 9)
    food_count = (1, 5)

    def __init__(self, level):
        self.level = level
        self.player = None
        self.reset(level)

    def add(self, game_object):
        self.objects[game_object.layer].append(game_object)

    def remove(self, game_object):
        self.objects[game_object.layer].remove(game_object)

    def reset(self, level):
        self.level = level
        width, height = GRID_SIZE
        self.objects = {layer: [] for layer in Layer}

        if self.player:
            self.player.position = Point(1, height - 2)
        else:
            self.player = Player(Point(1, height - 2))
        self.add(self.player)

        # Place outer walls and floor
        for x in xrange(width):
            for y in xrange(height):
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    self.add(OuterWall.create_random(Point(x, y)))
                else:
                    self.add(Floor.create_random(Point(x, y)))

        grid_positions = [Point(x, y) for x in xrange(2, width - 2) for y in xrange(2, height - 2)]
        random.shuffle(grid_positions)

        # Place inside walls
        wall_count = random.randint(*self.wall_count)

        for _ in xrange(wall_count):
            self.add(Wall.create_random(grid_positions.pop()))

        # Place enemies
        enemy_count = int(math.log(self.level + 2, 2))

        for _ in xrange(enemy_count):
            self.add(Enemy.create_random(grid_positions.pop()))

        # Place food
        food_count = random.randint(*self.food_count)

        for _ in xrange(food_count):
            self.add(Food(grid_positions.pop()))

        # Place exit
        self.add(Exit(Point(width - 2, 1)))

        # Display GUI
        self.gui = Gui(Point(SCREEN_WIDTH / 2 - Gui.width / 2, SCREEN_HEIGHT - Gui.height))
        self.add(self.gui)

    def draw(self, surface):
        for layer in Layer:
            for game_object in self.objects[layer]:
                game_object.draw(surface)

    def update(self):
        for layer in Layer:
            for game_object in self.objects[layer]:
                game_object.update()

scene = Scene(1)
