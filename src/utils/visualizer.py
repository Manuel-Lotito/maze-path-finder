import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from maze.grid import Grid
from algorithms.BFS import BFS
from algorithms.Greedy_BFS import Greedy_BFS
from algorithms.A_STAR import A_STAR


class UI(tk.Frame):

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid_object = Grid.from_file()
        self.grid_cell_array = []
        self.algorithms = {
            "BFS": BFS,
            "Greedy BFS": Greedy_BFS,
            "A STAR": A_STAR
        }
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
            command=self.random_maze_button
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
        self.algorythms_list = ttk.Combobox(
            self.control_frame,
            state="readonly",
            values=["BFS", "Greedy BFS", "A STAR"]
        )
        self.algorythms_list.pack(side=tk.LEFT, padx=(20, 0))
        self.algorythms_list.set("Algorythms")

        # Run Algorythm Button
        self.run_button = tk.Button(
            self.control_frame,
            text="Run",
            state="normal",
            command=self.run_button_func
            )
        self.run_button.pack(side=tk.LEFT, padx=5)

        # Grid Frame
        self.grid_frame = tk.Frame(self.parent)
        self.grid_frame.pack(pady=10)

        self.create_visual_grid()

    # Visual grid functions
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

    # Load button functions
    def load_maze(self):

        self.grid_object = Grid.from_file(self.grid_object.PATHS["user_matrix"])

        for widget in self.grid_frame.winfo_children():

            widget.destroy()

        self.create_visual_grid()

    # Clear button functions
    def clear_grid(self):

        self.grid_object.clear_matrix()

        for i, array in enumerate(self.grid_cell_array):
            for j, cell in enumerate(array):
                cell.config(text=self.grid_object.get_symbol(i, j))

    # Run button functions
    def run_button_func(self):

        if self.run_button.cget("text") == "Run":
            self.run_algorythm()
        else:

            for i, array in enumerate(self.grid_cell_array):

                for j, cell in enumerate(array):

                    if cell.cget("text") == "\U0001F7E6":
                        cell.config(text=self.grid_object.get_symbol(i, j))
                        cell.config(state="normal")

            self.end_animation()

            self.run_button.config(text="Run")

    def run_algorythm(self):

        selected = self.algorythms_list.get()

        if selected not in self.algorithms:
            messagebox.showinfo("no algorithm selected",
                                "Please select an algorithm")
            return

        algo_func = self.algorithms[selected]
        start = self.grid_object.start
        end = self.grid_object.end
        matrix = self.grid_object.matrix

        maze_data = algo_func(start, end, matrix)

        if not maze_data:
            messagebox.showinfo("Maze is unsolvable",
                                "no valid path from start to end.")
            return

        self.run_button.config(text="Restart")

        self.run_solution_animation(maze_data["maze_solution"])

        messagebox.showinfo(
            "Maze stats",
            f"Real time solution: {maze_data["real_time_solve"]} seconds\n"
            f"Visited cells: {maze_data["visited_nodes"]}\n"
            f"Path length: {maze_data["solution_length"]} cells"
            )

    def run_solution_animation(self, path, index=0):

        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="disabled")

        if index >= len(path):
            self.run_button.config(state="normal")
            return

        i, j = path[index]
        self.grid_cell_array[i][j].config(text="\U0001F7E6", state="disabled")
        self.after(50, lambda: self.run_solution_animation(path, index + 1))

    def end_animation(self):

        for widget in self.control_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal")

    # Random maze functions

    def random_maze_button(self):

        self.grid_object.generate_maze()

        for i, array in enumerate(self.grid_cell_array):

            for j, cell in enumerate(array):

                cell.config(text=self.grid_object.get_symbol(i, j))
