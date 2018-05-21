import random

from . import Tag, spritesheet
from .game_object import GameObject, basic_state_machine


class Food(GameObject):
    state_machine = basic_state_machine(spritesheet.get_sprite((19,)))

    def __init__(self, position):
        super(Food, self).__init__(
            tag=Tag.FOOD, position=position)

    @staticmethod
    def create_random(position):
        return random.choice((Food, Soda,))(position)


class Soda(GameObject):
    state_machine = basic_state_machine(spritesheet.get_sprite((18,)))

    def __init__(self, position):
        super(Food, self).__init__(
            tag=Tag.SODA, position=position)
