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
        self.hp = 4
        self.player = None
        self.wait_turn = True

        super(Enemy, self).__init__(position, tag=Tag.ENEMY)

    @staticmethod
    def create_random(position):
        return random.choice((Enemy1, Enemy2))(position)

    def on_collide(self, collider):
        if collider.tag != Tag.PLAYER:
            return

        from .scene import scene

        damage = random.randint(*self.damage)
        scene.gui.action = "-{}".format(damage)
        collider.take_damage(damage)
        self.change_state(LivingStateKind.CHOP)

    def get_player(self):
        if self.player:
            return self.player
        from .scene import scene
        self.player = scene.player
        return self.player

    def update(self):
        if self.wait_turn:
            self.wait_turn = False
            return
        self.wait_turn = True

        difference = self.get_player().position - self.position

        if abs(difference.x) > abs(difference.y):
            self.move(Point(difference.x / abs(difference.x), 0))
        else:
            self.move(Point(0, difference.y / abs(difference.y)))


class Enemy1(Enemy):
    state_machine = Enemy1StateMachine
    damage = (5, 15)


class Enemy2(Enemy):
    state_machine = Enemy2StateMachine
    damage = (15, 25)
