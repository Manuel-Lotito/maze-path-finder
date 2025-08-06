from queue import Queue
import time
from servicies.base_solver import MazeSolver


class BFS(MazeSolver):

    def solve(self, start, end, matrix):
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

            neighbours = self.get_neighbours(current, matrix)

            for neighbour in neighbours:

                if neighbour not in visited:

                    queue.put(neighbour)
                    visited.add(neighbour)
                    came_from[neighbour] = current

        return False
