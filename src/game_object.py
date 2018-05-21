import enum

from . import Layer
from .state import State


class StateMachine(object):
    def update(self):
        pass

    def draw(self, surface, point):
        self.state.draw(surface, point)


class StateKind(enum.Enum):
    DEFAULT = 0


def basic_state_machine(sprite):
    class BasicStateMachine(StateMachine):
        def __init__(self):
            self.state = State(StateKind.DEFAULT, sprite)

    return BasicStateMachine


class GameObject(object):
    def __init__(self, layer=Layer.DEFAULT, tag=None, position=None):
        self.state_machine = self.state_machine()
        self.layer = layer
        self.tag = tag
        self.position = position

    def update(self):
        pass

    def draw(self, surface):
        self.state_machine.update()
        self.state_machine.draw(surface, self.position.to_absolute())

    def on_collide(self, collider):
        pass

    def die(self):
        from .scene import scene
        scene.remove(self)
