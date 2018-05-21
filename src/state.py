class State(object):
    def __init__(self, kind, sprite):
        self.kind = kind
        self.sprite = sprite

    def draw(self, surface, position):
        self.sprite.draw(surface, position)
