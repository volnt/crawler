import random

from . import Tag, spritesheet
from .living_object import LivingObject, LivingStateKind, LivingStateMachine
from .state import State


class PlayerStateMachine(LivingStateMachine):
    states = {state.kind: state for state in (
        State(LivingStateKind.IDLE, spritesheet.get_sprite((0, 1, 2, 3, 4, 5))),
        State(LivingStateKind.CHOP, spritesheet.get_sprite((40, 41)))
    )}


class Player(LivingObject):
    state_machine = PlayerStateMachine

    def __init__(self, position):
        self.food = 100
        super(Player, self).__init__(position, tag=Tag.PLAYER)

    def on_move(self):
        self.food -= 1

    def on_collide(self, collider):
        if collider.tag == Tag.ENEMY:
            self.change_state(LivingStateKind.CHOP)
            collider.damage(random.randint(5, 15))

        elif collider.tag == Tag.FOOD:
            self.food += 20
            collider.die()

        elif collider.tag == Tag.EXIT:
            from .scene import scene
            scene.reset(scene.level + 1)

    def change_state(self, state):
        self.state_machine.state = self.state_machine.states[state]
