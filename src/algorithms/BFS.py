from queue import Queue
import time


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


def BFS(start, end, matrix):
    start_time = time.time()
    output = {}
    queue = Queue()
    queue.put(start)
    visited = set([start])
    came_from = {}

    while not queue.empty():

        current = queue.get()

        # Find the solution
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

        neighbours = get_neighbours(current, matrix)

        for neighbour in neighbours:

            if neighbour not in visited:

                queue.put(neighbour)
                visited.add(neighbour)
                came_from[neighbour] = current
