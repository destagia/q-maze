from qmaze.maze import Maze

class Game(object):
    def __init__(self, controller):
        self.__controller = controller
        self.__maze = Maze(self)
        self.is_goal = False

    def next(self):
        if self.is_goal:
            return None

        move = self.__controller.select_move()
        self.__maze.move_player(move)

        if self.is_goal:
            return 1.0

        return 0.0

    def show(self):
        self.__maze.show()
