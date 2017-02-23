import random

class QController(object):
    def __init__(self, maze):
        self.__maze = maze

    def invoke(self):
        #
        # Select action from state
        #
        dx = random.randint(-1, 1)
        if dx == 0:
            dy = random.randint(-1, 1)
        else:
            dy = 0
        direction = (dy, dx)
        print('player move: (x, y) = {}'.format((dx, dy)))
        self.__maze.move_player(direction)

        #
        # Train Q-function
        #
