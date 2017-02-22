# -*- coding: utf-8 -*-

class MazeObject(object):
    def move(self, game):
        return True

    def to_map_str(self):
        return '　'

class Start(MazeObject):
    pass

class Block(MazeObject):
    def to_map_str(self):
        return '壁'

    def move(self, game):
        return False

class Goal(MazeObject):
    def to_map_str(self):
        return '🚩 '

    def move(self, game):
        game.is_goal = True
        return True

class Floor(MazeObject):
    pass

class Maze(object):
    def __init__(self, game):
        self.size = 5
        self.__map = [
            [Floor(), Block(), Goal(),  Floor(), Floor()],
            [Floor(), Block(), Block(), Block(), Floor()],
            [Floor(), Floor(), Floor(), Block(), Floor()],
            [Block(), Block(), Floor(), Block(), Floor()],
            [Floor(), Floor(), Floor(), Floor(), Floor()],
        ]
        self.__player_position = (0, 0)
        self.__game = game

    def move_player(self, direction):
        x, y = direction
        px, py = self.__player_position
        mx, my = px + x, py + y

        if mx < 0 or mx >= self.size:
            return
        if my < 0 or my >= self.size:
            return

        maze_obj = self.__map[mx][my]

        if maze_obj.move(self.__game):
            self.__player_position = (mx, my)

    def show(self):
        print('　ーーーーー')
        for i in range(len(self.__map)):
            row = self.__map[i]
            row_str = '｜'
            for j in range(len(row)):
                point = row[j]
                if self.__player_position == (i, j):
                    row_str += '🐼 '
                else:
                    row_str += point.to_map_str()
            row_str += '｜'
            print(row_str)
        print('　ーーーーー')