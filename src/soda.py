from . import Tag, spritesheet
from .game_object import GameObject, Collider, Transform


class Soda(GameObject):
    sprite = spritesheet.get_sprite((18,))

    def __init__(self, position):
        super(Soda, self).__init__(
            tag=Tag.SODA, transform=Transform(position), sprite=self.sprite, collider=Collider(trigger=True))
