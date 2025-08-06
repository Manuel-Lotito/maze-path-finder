from abc import ABC, abstractmethod


class MazeSolver(ABC):

    @abstractmethod
    def solve(self, start, end, matrix):
        pass

    def manhattan(self, start, end):
        (y1, x1) = start
        (y2, x2) = end
        return abs(y1 - y2) + abs(x1 - x2)

    def get_neighbours(self, posicion, matrix):
        neighbours = []
        (y, x) = posicion

        for y_mov, x_mov in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            actual_y = y + y_mov
            actual_x = x + x_mov

            if 0 <= actual_y < len(matrix) and 0 <= actual_x < len(matrix[0]):

                if matrix[actual_y][actual_x] != "#":

                    pos = (actual_y, actual_x)
                    neighbours.append(pos)

        return neighbours
