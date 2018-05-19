import enum

from . import Layer, Point


class Transform(object):
    def __init__(self, position, rotation=None):
        self.position = position
        self.rotation = rotation or Point(0, 0)


class Collider(object):
    def __init__(self, trigger=False, size=None):
        self.trigger = trigger
        self.size = size or Point(1, 1)


class GameObject(object):
    def __init__(self, layer=Layer.DEFAULT, tag=None, transform=None, sprite=None, collider=None):
        self.layer = layer
        self.tag = tag
        self.transform = transform
        self.sprite = sprite
        self.collider = collider

    def update(self):
        pass

    def draw(self, surface):
        self.sprite.draw(surface, self.transform.position.to_absolute())

    def on_collide(self, collider):
        pass


class LivingState(enum.Enum):
    IDLE = 0
    ATTACK = 1


class LivingObject(GameObject):
    def __init__(self, position, tag=None):
        super(LivingObject, self).__init__(
            layer=Layer.BLOCKING, tag=tag, transform=Transform(position),
            sprite=self.sprites[LivingState.IDLE], collider=Collider())

    def on_move(self):
        pass

    def damage(self, n):
        self.food -= n
        if self.food <= 0:
            from .scene import scene
            scene.remove(self)

    def collide_with(self, target):
        from .scene import scene
        for blocking in scene.tiles[Layer.BLOCKING]:
            if blocking != self and blocking.transform.position == target:
                return blocking

        for blocking in scene.tiles[Layer.DEFAULT]:
            if blocking != self and blocking.transform.position == target:
                return blocking

    def move(self, direction):
        target = self.transform.position + direction
        collision = self.collide_with(target)

        if collision:
            self.on_collide(collision)

        if not collision or collision.layer != Layer.BLOCKING:
            self.on_move()
            self.transform.position = target
            return True

        return False
