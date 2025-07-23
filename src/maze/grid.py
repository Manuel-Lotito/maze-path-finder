

class Grid:
    SYMBOLS = {
        "wall": "\u2B1B",
        "path": "\u2B1C",
        "start": "\u25B6",
        "end": "\u23F9",
        "visited": "\U0001F7E9"
    }

    PATHS = {
        "main_matrix": "src\\maze.txt",
        "user_matrix": "src\\my_maze.txt"
    }

    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end

    # Function to get matrix from the file
    @classmethod
    def from_file(cls, matrix_path="src\\maze.txt"):
        open_path = open(matrix_path, "r")
        lines = open_path.readlines()
        open_path.close()

        matrix = []
        start = None
        end = None

        for y, line in enumerate(lines):
            row = []

            for x, char in enumerate(line):
                if char == "S":
                    start = (y, x)
                    row.append("S")
                elif char == "E":
                    end = (y, x)
                    row.append("E")
                elif char != "\n":
                    row.append(char)

            matrix.append(row)

        return cls(matrix, start, end)

    # Function to draw matrix
    def get_symbol(self, y, x):
        if (y, x) == self.start:
            return self.SYMBOLS["start"]
        elif (y, x) == self.end:
            return self.SYMBOLS["end"]
        elif self.matrix[y][x] == "#":
            return self.SYMBOLS["wall"]
        elif self.matrix[y][x] == " ":
            return self.SYMBOLS["path"]

    # Function for cell changing
    def change_cell(self, y, x):

        if self.matrix[y][x] not in ["S", "E"]:

            if self.matrix[y][x] == "#":
                self.matrix[y][x] = " "
            else:
                self.matrix[y][x] = "#"

        return self.get_symbol(y, x)

    # Function to clear the matrix
    def clear_matrix(self):
        for y in range(len(self.matrix)):

            for x in range(len(self.matrix[0])):

                if (y, x) not in [self.start, self.end]:
                    self.matrix[y][x] = " "

    # Function to save the matrix
    def save_matrix(self):

        path = self.PATHS["user_matrix"]

        with open(path, "w") as my_maze:

            for i in range(len(self.matrix)):

                line = self.matrix[i]
                my_maze.write("".join(line))

                if i < len(self.matrix) - 1:
                    my_maze.write("\n")
