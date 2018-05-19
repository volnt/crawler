import enum
import random

from . import Tag, spritesheet, Point
from .game_object import LivingObject, LivingState


class EnemyKind(enum.Enum):
    UNDEAD1 = 0
    UNDEAD2 = 1


class Enemy(LivingObject):
    sprites_kind = {
        EnemyKind.UNDEAD1: {
            LivingState.IDLE: spritesheet.get_sprite((6, 7, 8, 9, 10, 11)),
            LivingState.ATTACK: spritesheet.get_sprite((42, 43)),
        },
        EnemyKind.UNDEAD2: {
            LivingState.IDLE: spritesheet.get_sprite((12, 13, 14, 15, 16, 17)),
            LivingState.ATTACK: spritesheet.get_sprite((44, 45)),
        },
    }

    def __init__(self, position, kind=EnemyKind.UNDEAD1):
        self.food = 15
        self.sprites = self.sprites_kind[kind]

        super(Enemy, self).__init__(position, tag=Tag.ENEMY)

    @staticmethod
    def random_kind():
        return random.choice(list(EnemyKind))

    def on_collide(self, collider):
        if collider.tag != Tag.PLAYER:
            return

        collider.damage(random.randint(5, 15))

    def update(self):
        self.move(random.choice((Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1))))
