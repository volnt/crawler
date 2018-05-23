import math
import random
import sys
import time

import pygame

from . import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, Layer, Point, font
from .enemy import Enemy
from .exit import Exit
from .floor import Floor
from .food import Food
from .player import Player
from .wall import OuterWall, Wall


class DayTransition(object):

    def __init__(self, day, dead=False):
        self.day = day
        self.dead = dead
        self.start = time.time() * 1000

    def draw(self, surface):
        if self.dead:
            text = text = font.render("You starved on day {}".format(self.day), True, (255, 255, 255))
        else:
            text = font.render("Day {}".format(self.day), True, (255, 255, 255))
        surface.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))


class Gui(object):
    layer = Layer.GUI

    def __init__(self, position):
        self.position = position
        self.action = ""
        self.reset_action = False

    def update(self):
        if self.action and self.reset_action:
            self.action = ""
            self.reset_action = False
        elif self.action:
            self.reset_action = True

    def draw(self, surface):
        self.text = font.render("{} Food: {}".format(self.action, scene.player.food), True, (255, 255, 255))
        surface.blit(self.text, (self.position.x - self.text.get_width() / 2,
                                 self.position.y))


class Scene(object):
    wall_count = (5, 9)
    food_count = (1, 5)

    def __init__(self, level):
        self.level = level
        self.player = None
        self.gui = None
        self.transition = None
        self.transition_time = None
        self.reset(level)

    def add(self, game_object):
        self.objects[game_object.layer].append(game_object)

    def remove(self, game_object):
        self.objects[game_object.layer].remove(game_object)

    def reset(self, level, dead=False):
        self.level = level
        self.transition = DayTransition(level, dead)

    def post_transition(self):
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
            self.add(Food.create_random(grid_positions.pop()))

        # Place exit
        self.add(Exit(Point(width - 2, 1)))

        # Display GUI
        self.gui = Gui(Point(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        self.add(self.gui)

    def draw(self, surface):
        if self.transition and (time.time() * 1000 - self.transition.start > 1000 or self.level < 2):
            self.transition.draw(surface)
            return

        for layer in Layer:
            for game_object in self.objects[layer]:
                game_object.draw(surface)

    def update_game_objects(self):
        for layer in Layer:
            for game_object in self.objects[layer]:
                game_object.update()

    def update(self):
        events = pygame.event.get()

        if self.transition and time.time() * 1000 - self.transition.start > 4000:
            self.transition = None
            if self.player and self.player.dead:
                sys.exit()
            self.post_transition()
        if self.transition:
            return

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                move = None
                if event.key == pygame.K_LEFT:
                    move = Point(-1, 0)
                if event.key == pygame.K_RIGHT:
                    move = Point(1, 0)
                if event.key == pygame.K_UP:
                    move = Point(0, -1)
                if event.key == pygame.K_DOWN:
                    move = Point(0, 1)

                if move:
                    scene.player.move(move)
                    scene.update_game_objects()

scene = Scene(1)
