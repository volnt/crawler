import random

from . import Layer, Tag, spritesheet
from .game_object import GameObject, basic_state_machine


class Wall(GameObject):
    def __init__(self, position):
        super(Wall, self).__init__(
            layer=Layer.BLOCKING, tag=Tag.WALL, position=position)

    @staticmethod
    def create_random(position):
        return random.choice((
            Wall1, Wall2, Wall3, Wall4, Wall5, Wall6, Wall7, Wall8, Wall9,
            Wall10, Wall12, Wall13, Wall14, Wall15, Wall16))(position)


class Wall1(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((21,)))


class Wall2(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((22,)))


class Wall3(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((23,)))


class Wall4(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((24,)))


class Wall5(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((27,)))


class Wall6(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((29,)))


class Wall7(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((30,)))


class Wall8(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((31,)))


class Wall9(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((48,)))


class Wall10(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((49,)))


class Wall12(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((50,)))


class Wall13(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((51,)))


class Wall14(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((52,)))


class Wall15(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((53,)))


class Wall16(Wall):
    state_machine = basic_state_machine(spritesheet.get_sprite((54,)))


class OuterWall(Wall):
    @staticmethod
    def create_random(position):
        return random.choice((
            OuterWall1, OuterWall2, OuterWall3))(position)


class OuterWall1(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((25,)))


class OuterWall2(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((26,)))


class OuterWall3(OuterWall):
    state_machine = basic_state_machine(spritesheet.get_sprite((28,)))
