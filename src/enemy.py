import random

from . import Point, Tag, spritesheet
from .living_object import LivingObject, LivingStateKind, LivingStateMachine
from .state import State


class Enemy1StateMachine(LivingStateMachine):
    states = {state.kind: state for state in (
        State(LivingStateKind.IDLE, spritesheet.get_sprite((6, 7, 8, 9, 10, 11))),
        State(LivingStateKind.CHOP, spritesheet.get_sprite((42, 43))),
    )}


class Enemy2StateMachine(LivingStateMachine):
    states = {state.kind: state for state in (
        State(LivingStateKind.IDLE, spritesheet.get_sprite((12, 13, 14, 15, 16, 17))),
        State(LivingStateKind.CHOP, spritesheet.get_sprite((44, 45))),
    )}


class Enemy(LivingObject):
    def __init__(self, position):
        self.food = 15
        from .scene import scene
        self.player = scene.player

        super(Enemy, self).__init__(position, tag=Tag.ENEMY)

    @staticmethod
    def create_random(position):
        return random.choice((Enemy1, Enemy2))(position)

    def on_collide(self, collider):
        if collider.tag != Tag.PLAYER:
            return

        collider.damage(random.randint(5, 15))

    def update(self):
        self.move(random.choice((Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1))))


class Enemy1(Enemy):
    state_machine = Enemy1StateMachine


class Enemy2(Enemy):
    state_machine = Enemy2StateMachine
