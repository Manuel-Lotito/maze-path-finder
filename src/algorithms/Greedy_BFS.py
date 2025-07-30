import heapq
import time


def manhattan(start, end):
    (y1, x1) = start
    (y2, x2) = end
    return abs(y1 - y2) + abs(x1 - x2)


def get_neighbours(posicion, matrix):
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


def Greedy_BFS(start, end, matrix):
    start_time = time.time()
    output = {}

    open_set = []
    heapq.heappush(open_set, (manhattan(start, end), start))

    visited = set([start])
    came_from = {}

    while open_set:

        _, current = heapq.heappop(open_set)

        # Find solution
        if current == end:
            path = []

            while came_from[current] != start:

                current = came_from[current]
                path.append(current)

            path.reverse()
            end_time = time.time()

            output["maze_solution"] = path
            output["visited_nodes"] = len(visited)
            output["solution_length"] = len(path)
            output["real_time_solve"] = end_time - start_time

            return output

        for neighbour in get_neighbours(current, matrix):
            if neighbour not in visited:
                heapq.heappush(open_set, (manhattan(neighbour, end), neighbour))
                came_from[neighbour] = current
                visited.add(neighbour)

    return False
