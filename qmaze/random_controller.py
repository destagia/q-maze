import random

class RandomController(object):
    def select_move(self):
        return (random.randint(-1, 1), random.randint(-1, 1))