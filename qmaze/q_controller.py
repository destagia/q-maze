import random

class QController(object):
    def __init__(self, maze):
        self.__maze = maze

    def invoke(self):
        direction = (random.randint(-1, 1), random.randint(-1, 1))
        self.__maze.move_player(direction)
