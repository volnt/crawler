import random
from . import Tag, spritesheet, Layer
from .game_object import GameObject, Collider, Transform


class Wall(GameObject):
    sprites = spritesheet.get_sprite((21, 22, 23, 24, 27, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54))

    def __init__(self, position):
        index = random.randint(0, len(self.sprites.images) - 1)
        sprite = self.sprites.subsprite((index,))
        super(Wall, self).__init__(
            layer=Layer.BLOCKING, tag=Tag.WALL, transform=Transform(position), sprite=sprite, collider=Collider())


class OuterWall(Wall):
    sprites = spritesheet.get_sprite((25, 26, 28))
