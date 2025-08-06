import random
from models.cell import cell


class Grid:

    PATHS = {
        "main_matrix": "src\\static\\maze.txt",
        "user_matrix": "src\\static\\my_maze.txt"
    }

    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end

    # Function to get matrix from the file
    @classmethod
    def from_file(cls, matrix_path="src\\static\\maze.txt"):
        open_path = open(matrix_path, "r")
        lines = open_path.readlines()
        open_path.close()

        matrix = []
        start = None
        end = None

        for y, line in enumerate(lines):
            row = []

            for x, char in enumerate(line):

                if char == "\n":

                    continue

                if char == "S":

                    start = (y, x)

                    cell_obj = cell(char, True, False)

                elif char == "E":

                    end = (y, x)

                    cell_obj = cell(char, False, True)

                else:

                    cell_obj = cell(char, False, False)

                row.append(cell_obj)

            matrix.append(row)

        return cls(matrix, start, end)

    # Function to clear the maze
    def clear_matrix(self):
        for y, array in enumerate(self.matrix):

            for x, cell_obj in enumerate(array):

                if not cell_obj.start and not cell_obj.end:

                    cell_obj.character = " "

    # Function to save the maze
    def save_matrix(self):

        path = self.PATHS["user_matrix"]

        with open(path, "w") as my_maze:

            for y, array in enumerate(self.matrix):

                line = []

                for x, cell_obj in enumerate(array):

                    line.append(cell_obj.character)

                my_maze.write("".join(line))

                if y < len(self.matrix) - 1:

                    my_maze.write("\n")

    # Function to generate maze
    def generate_maze(self):

        new_maze = [["#" for _ in range(21)] for _ in range(21)]

        self.random_maze(new_maze, 1, 1)

        for y in range(len(new_maze)):

            for x in range(len(new_maze[0])):
                character = new_maze[y][x]
                new_maze[y][x] = cell(character, False, False)

        new_maze[1][1] = cell("S", True, False)
        new_maze[19][19] = cell("E", False, True)
        self.start = (1, 1)
        self.end = (19, 19)

        self.matrix = new_maze

    # Function to randomize a maze
    def random_maze(self, maze, y, x):
        maze[y][x] = " "
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 < ny < len(maze) and 0 < nx < len(maze[0]) and maze[ny][nx] == "#":
                maze[y + dy // 2][x + dx // 2] = " "
                self.random_maze(maze, ny, nx)

    #
    def to_char_matrix(self):
        return [[cell.character for cell in row] for row in self.matrix]
