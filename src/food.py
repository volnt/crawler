from . import Tag, spritesheet
from .game_object import GameObject, Transform


class Food(GameObject):
    sprite = spritesheet.get_sprite((19,))

    def __init__(self, position):
        super(Food, self).__init__(
            tag=Tag.FOOD, transform=Transform(position), sprite=self.sprite)
