import heapq
import time
from servicies.base_solver import MazeSolver


class A_STAR(MazeSolver):

    def solve(self, start, end, matrix):
        start_time = time.time()
        output = {}

        open_set = []
        heapq.heappush(open_set, (self.manhattan(start, end), start))

        g_score = {start: 0}
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

            visited.add(current)

            for neighbour in self.get_neighbours(current, matrix):

                tentative_g = g_score[current] + 1

                if neighbour not in g_score or tentative_g < g_score[neighbour]:
                    came_from[neighbour] = current
                    visited.add(neighbour)
                    g_score[neighbour] = tentative_g
                    f_score = tentative_g + self.manhattan(neighbour, end)
                    heapq.heappush(open_set, (f_score, neighbour))

        return False
