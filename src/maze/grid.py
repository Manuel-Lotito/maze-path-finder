import os

class Grid:
    SYMBOLS = {
    "wall": "\u2B1B",
    "path": "\u2B1C",
    "start": "\u25B6",
    "end": "\u23F9",
    "visited": "\U0001F7E9"
    }

    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end 

    #Function to get matrix from the file 
    @classmethod
    def from_file(cls, matrix_path):
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
                    start = (x, y)
                    row.append(" ")
                elif char == "E":
                    end = (x, y)
                    row.append(" ")
                elif char != "\n":
                    row.append(char)

            matrix.append(row)

        return cls(matrix, start, end)
    
    #Function to draw matrix
    def get_symbol(self, y, x):
        if (x, y) == self.start:
            return self.SYMBOLS["start"]
        elif (x, y) == self.end:
            return self.SYMBOLS["end"] 
        elif self.matrix[y][x] == "#":
            return self.SYMBOLS["wall"]
        elif self.matrix[y][x] == " ":
            return self.SYMBOLS["path"]


    #Function for cell changing
    def change_cell(self, pos):
        y, x = pos

        if self.matrix[y][x] not in ["S", "E"]:
            if self.matrix[y][x] == "#":
                self.matrix[y][x] = " "
            else:
                self.matrix[y][x] = "#"



