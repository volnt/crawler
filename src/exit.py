from . import Tag, spritesheet, Layer
from .game_object import GameObject, Collider, Transform


class Exit(GameObject):
    sprite = spritesheet.get_sprite((20,))

    def __init__(self, position):
        super(Exit, self).__init__(
            layer=Layer.BLOCKING, tag=Tag.EXIT, transform=Transform(position),
            sprite=self.sprite, collider=Collider(trigger=True))

    def on_collide(self, collider):
        if collider.tag != Tag.PLAYER:
            return

        from .scene import scene
        scene.reset(scene.level + 1)
