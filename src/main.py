from .game_manager import GameManager
import time


def main():
    game_manager = GameManager()

    while 42:
        game_manager.update()
        game_manager.draw()
