from . import Tag, spritesheet, Layer
from .game_object import GameObject, basic_state_machine


class Exit(GameObject):
    state_machine = basic_state_machine(spritesheet.get_sprite((20,)))

    def __init__(self, position):
        super(Exit, self).__init__(
            layer=Layer.BLOCKING, tag=Tag.EXIT, position=position)
