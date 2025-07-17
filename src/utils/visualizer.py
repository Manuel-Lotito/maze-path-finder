import tkinter as tk
from tkinter import ttk
from maze.grid import Grid


class UI(tk.Frame):

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid_object = Grid.from_file()
        self.grid_cell_array = []
        self.init_ui()

    def init_ui(self):
        self.parent.title("Maze Path Finder")

        # Control interface

        # Sueprior Frame
        self.control_frame = tk.Frame(self.parent)
        self.control_frame.pack(pady=10)

        # Random Maze Button
        tk.Button(
            self.control_frame,
            text="Random Maze",
            ).pack(side=tk.LEFT, padx=(0, 20))

        # Clear Button
        tk.Button(
            self.control_frame,
            text="Clear",
            command=self.clear_grid
            ).pack(side=tk.LEFT, padx=5)

        # Save button
        tk.Button(
            self.control_frame,
            text="Save",
            command=lambda: self.grid_object.save_matrix()
            ).pack(side=tk.LEFT, padx=5)

        # Load button
        tk.Button(
            self.control_frame,
            text="Load",
            command=self.load_maze
            ).pack(side=tk.LEFT, padx=5)

        # Algorythms combox
        algorythms_list = ttk.Combobox(
            self.control_frame,
            state="readonly",
            values=["djkastra", "algorythm2", "algorythm3"]
        )
        algorythms_list.pack(side=tk.LEFT, padx=(20, 0))
        algorythms_list.set("Algorythms")

        # Run Algorythm Button
        tk.Button(
            self.control_frame,
            text="Run",
            ).pack(side=tk.LEFT, padx=5)

        # Grid Frame
        self.grid_frame = tk.Frame(self.parent)
        self.grid_frame.pack(pady=10)

        self.create_visual_grid()

    def click_on_cell(self, cell, i, j):
        symbol = self.grid_object.change_cell(i, j)
        cell.config(text=symbol)

    def create_visual_grid(self):
        self.grid_cell_array.clear()
        for i in range(len(self.grid_object.matrix)):

            row = []

            for j in range(len(self.grid_object.matrix[0])):
                cell = tk.Button(
                    self.grid_frame,
                    text=self.grid_object.get_symbol(i, j),
                    width=2,
                    height=1,
                )
                cell.grid(row=i, column=j)
                if (i, j) not in [self.grid_object.start, self.grid_object.end]:
                    cell.config(command=lambda c=cell, i=i, j=j: self.click_on_cell(c, i, j))
                    row.append(cell)

            self.grid_cell_array.append(row)

    def load_maze(self):
        self.grid_object = Grid.from_file(self.grid_object.PATHS["user_matrix"])
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.create_visual_grid()

    def clear_grid(self):
        self.grid_object.clear_matrix()

        for i, array in enumerate(self.grid_cell_array):
            for j, cell in enumerate(array):
                cell.config(text=self.grid_object.get_symbol(i, j))
