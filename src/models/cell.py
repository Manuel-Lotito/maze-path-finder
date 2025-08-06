
class cell:

    SYMBOLS = {
        "#": "\u2B1B",
        " ": "\u2B1C",
        "start": "\u25B6",
        "end": "\u23F9"
    }

    def __init__(self, character, start=False, end=False):
        self.start = start
        self.end = end
        self.character = character

    # Function to draw maze
    def get_symbol(self):
        if self.start:
            return self.SYMBOLS["start"]

        if self.end:
            return self.SYMBOLS["end"]

        return self.SYMBOLS[self.character]

    # Function for cell changing
    def change_cell(self):

        if self.character in ["S", "E"]:
            return

        if self.character == "#":
            self.character = " "
        else:
            self.character = "#"

        return self.get_symbol()
