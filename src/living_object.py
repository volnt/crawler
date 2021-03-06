import enum
import time

from . import Layer
from .game_object import GameObject
from .sprite import SPRITE_TIME_STEP
from .state import StateMachine


class LivingStateKind(enum.Enum):
    IDLE = 0
    CHOP = 1
    CRY = 2


class LivingStateMachine(StateMachine):
    def __init__(self):
        self.state = self.states[LivingStateKind.IDLE]
        self.start_chop = None

    def update(self):
        if self.state.kind == LivingStateKind.CHOP:
            if self.start_chop is None:
                self.start_chop = time.time() * 1000
            elif time.time() * 1000 - self.start_chop > SPRITE_TIME_STEP * 2:
                self.state = self.states[LivingStateKind.IDLE]
                self.start_chop = None


class LivingObject(GameObject):
    def __init__(self, position, tag=None):
        super(LivingObject, self).__init__(layer=Layer.LIVING, tag=tag, position=position)

    def on_move(self):
        pass

    def collide_with(self, target):
        from .scene import scene
        for layer in (Layer.BLOCKING, Layer.LIVING, Layer.DEFAULT):
            for blocking in scene.objects[layer]:
                if blocking != self and blocking.position == target:
                    return blocking

    def move(self, direction):
        target = self.position + direction
        collision = self.collide_with(target)

        if collision:
            self.on_collide(collision)

        if not collision or collision.layer not in (Layer.BLOCKING, Layer.LIVING):
            self.on_move()
            self.position = target
            return True

        return False
