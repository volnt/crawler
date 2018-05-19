import random
from . import Tag, spritesheet
from .game_object import LivingObject, LivingState


class Player(LivingObject):
    sprites = {
        LivingState.IDLE: spritesheet.get_sprite((0, 1, 2, 3, 4, 5)),
        LivingState.ATTACK: spritesheet.get_sprite((40, 41)),
    }

    def __init__(self, position):
        self.food = 100
        super(Player, self).__init__(position, tag=Tag.PLAYER)

    def on_move(self):
        self.food -= 1

    def on_collide(self, collider):
        if collider.tag == Tag.ENEMY:
            self.sprite = self.sprites[LivingState.ATTACK]

            collider.damage(random.randint(5, 15))

        elif collider.tag == Tag.FOOD:
            from .scene import scene
            self.food += 20
            scene.remove(collider)
