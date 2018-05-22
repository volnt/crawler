import enum
import random

from . import Layer, Tag, spritesheet
from .game_object import GameObject, basic_state_machine
from .state import State, StateMachine


class WallStateKind(enum.Enum):
    HEALTHY = 0
    DAMAGED = 1


class WallStateMachine(StateMachine):
    def __init__(self):
        self.state = self.states[WallStateKind.HEALTHY]


class Wall(GameObject):
    def __init__(self, position):
        self.hp = 4
        super(Wall, self).__init__(
            layer=Layer.BLOCKING, tag=Tag.WALL, position=position)

    def take_damage(self, damage):
        self.change_state(WallStateKind.DAMAGED)
        super(Wall, self).take_damage(damage)

    @staticmethod
    def create_random(position):
        return random.choice((
            Wall1, Wall2, Wall3, Wall4, Wall5, Wall6, Wall7, Wall8))(position)


class Wall1StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((21,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((48,))),
    )}


class Wall1(Wall):
    state_machine = Wall1StateMachine


class Wall2StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((22,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((49,))),
    )}


class Wall2(Wall):
    state_machine = Wall2StateMachine


class Wall3StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((23,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((50,))),
    )}


class Wall3(Wall):
    state_machine = Wall3StateMachine


class Wall4StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((24,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((51,))),
    )}


class Wall4(Wall):
    state_machine = Wall4StateMachine


class Wall5StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((27,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((52,))),
    )}


class Wall5(Wall):
    state_machine = Wall5StateMachine


class Wall6StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((29,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((51,))),
    )}


class Wall6(Wall):
    state_machine = Wall6StateMachine


class Wall7StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((30,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((53,))),
    )}


class Wall7(Wall):
    state_machine = Wall7StateMachine


class Wall8StateMachine(WallStateMachine):
    states = {state.kind: state for state in (
        State(WallStateKind.HEALTHY, spritesheet.get_sprite((31,))),
        State(WallStateKind.DAMAGED, spritesheet.get_sprite((54,))),
    )}


class Wall8(Wall):
    state_machine = Wall8StateMachine


class OuterWall(Wall):
    @staticmethod
    def create_random(position):
        return random.choice((
            OuterWall1, OuterWall2, OuterWall3))(position)

    def take_damage(self, damage):
        pass


class OuterWall1(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((25,)))


class OuterWall2(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((26,)))


class OuterWall3(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((28,)))
