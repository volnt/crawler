import pygame
import time
import random

from . import Tag, spritesheet
from .living_object import LivingObject, LivingStateKind, LivingStateMachine
from .state import State
from .sprite import SPRITE_TIME_STEP


class PlayerStateMachine(LivingStateMachine):
    states = {state.kind: state for state in (
        State(LivingStateKind.IDLE, spritesheet.get_sprite((0, 1, 2, 3, 4, 5))),
        State(LivingStateKind.CHOP, spritesheet.get_sprite((40, 41))),
        State(LivingStateKind.CRY, spritesheet.get_sprite((46, 47)))
    )}

    def __init__(self):
        super(PlayerStateMachine, self).__init__()
        self.start_cry = None

    def update(self):
        super(PlayerStateMachine, self).update()

        if self.state.kind == LivingStateKind.CRY:
            if self.start_cry is None:
                self.start_cry = time.time() * 1000
            elif time.time() * 1000 - self.start_cry > SPRITE_TIME_STEP * 2:
                self.change_state(LivingStateKind.IDLE)
                self.start_cry = None


class Player(LivingObject):
    state_machine = PlayerStateMachine
    move_sounds = [
        pygame.mixer.Sound(file="assets/scavengers_footstep1.ogg"),
        pygame.mixer.Sound(file="assets/scavengers_footstep2.ogg"),
    ]
    fruit_sounds = [
        pygame.mixer.Sound(file="assets/scavengers_fruit1.ogg"),
        pygame.mixer.Sound(file="assets/scavengers_fruit2.ogg"),
    ]
    soda_sounds = [
        pygame.mixer.Sound(file="assets/scavengers_fruit1.ogg"),
        pygame.mixer.Sound(file="assets/scavengers_fruit2.ogg"),
    ]
    chop_sounds = [
        pygame.mixer.Sound(file="assets/scavengers_chop1.ogg"),
        pygame.mixer.Sound(file="assets/scavengers_chop2.ogg"),
    ]

    def __init__(self, position):
        self.food = 100
        super(Player, self).__init__(position, tag=Tag.PLAYER)

    def on_move(self):
        self.food -= 1
        random.choice(self.move_sounds).play()

    def take_damage(self, damage):
        self.change_state(LivingStateKind.CRY)
        self.food -= damage

    def attack(self, target):
        self.change_state(LivingStateKind.CHOP)
        target.take_damage(random.randint(2, 4))
        random.choice(self.chop_sounds).play()

    def eat(self, target):
        from .scene import scene
        scene.gui.action = "+{}".format(target.value)
        self.food += target.value
        target.die()

        if target.tag == Tag.FOOD:
            random.choice(self.fruit_sounds).play()
        elif target.tag == Tag.SODA:
            random.choice(self.soda_sounds).play()

    def exit(self):
        from .scene import scene
        scene.gui.action = "Day {}".format(scene.level + 1)
        scene.reset(scene.level + 1)

    def on_collide(self, collider):
        if collider.tag in (Tag.ENEMY, Tag.WALL):
            self.attack(collider)

        elif collider.tag in (Tag.FOOD, Tag.SODA):
            self.eat(collider)

        elif collider.tag == Tag.EXIT:
            self.exit()
