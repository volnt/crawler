import random

from . import Layer, Tag, spritesheet
from .game_object import GameObject, basic_state_machine


class Floor(GameObject):
    def __init__(self, position):
        super(Floor, self).__init__(
            layer=Layer.FLOOR, tag=Tag.FLOOR, position=position)

    @staticmethod
    def create_random(position):
        return random.choice((Floor1, Floor2, Floor3, Floor4, Floor5, Floor6, Floor7, Floor8))(position)


class Floor1(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((32,)))


class Floor2(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((33,)))


class Floor3(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((34,)))


class Floor4(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((35,)))


class Floor5(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((36,)))


class Floor6(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((37,)))


class Floor7(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((38,)))


class Floor8(Floor):
    state_machine = basic_state_machine(spritesheet.get_sprite((39,)))
