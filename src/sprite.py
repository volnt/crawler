import time

import pygame

SPRITE_TIME_STEP = 200


def time_picker(time_step=SPRITE_TIME_STEP):
    start_time = time.time() * 1000

    def picker(images):
        return images[int(((time.time() * 1000) - start_time) / time_step) % len(images)]

    return picker


class Sprite(object):
    def __init__(self, images, picker=None):
        self.images = images
        self.picker = picker or time_picker()

    def draw(self, surface, point):
        surface.blit(self.picker(self.images), point.to_tuple())


class SpriteSheet(object):
    def __init__(self, filename, sprite_size, cell_size):
        self.sprite_size = sprite_size
        self.cell_size = cell_size
        self.spritesheet = pygame.image.load(filename).convert()

    def get_sprite(self, indexes, time_step=SPRITE_TIME_STEP):
        images = []
        width, height = self.sprite_size

        for index in indexes:
            image = pygame.Surface([width, height]).convert()
            x = index % (self.spritesheet.get_width() / width)
            y = index / (self.spritesheet.get_width() / width)
            image.blit(
                self.spritesheet,
                (0, 0),
                (x * width, y * height, width, height)
            )
            image = pygame.transform.scale(image, self.cell_size)
            image.set_colorkey((255, 255, 255))
            images.append(image)

        return Sprite(images, picker=time_picker(time_step=time_step))
