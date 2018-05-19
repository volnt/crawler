import random
from . import Tag, spritesheet, Layer
from .game_object import GameObject, Collider, Transform


class Floor(GameObject):
    sprites = spritesheet.get_sprite((32, 33, 34, 35, 36, 37, 38, 39))

    def __init__(self, position):
        index = random.randint(0, len(self.sprites.images) - 1)
        sprite = self.sprites.subsprite((index,))
        super(Floor, self).__init__(
            layer=Layer.FLOOR, tag=Tag.FLOOR, transform=Transform(position), sprite=sprite, collider=Collider())
