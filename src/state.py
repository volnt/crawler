class State(object):
    def __init__(self, kind, sprite):
        self.kind = kind
        self.sprite = sprite

    def draw(self, surface, position):
        self.sprite.draw(surface, position)


class StateMachine(object):
    def update(self):
        pass

    def draw(self, surface, point):
        self.state.draw(surface, point)

    def change_state(self, state):
        self.state = self.states[state]
