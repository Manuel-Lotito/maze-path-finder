import tkinter as tk
from tkinter import ttk
from maze.grid import Grid
from utils.functions import (change_cell, clear_matrix)



class UI(tk.Frame): 

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid_object = Grid.from_file("src\\texto.txt")
        self.init_ui()


    def init_ui(self):
        self.parent.title("Maze Path Finder")
        
        #Control interface   
        
        #Sueprior Frame
        self.control_frame = tk.Frame(self.parent)
        self.control_frame.pack(pady=10)

        #Clear Button
        def clear_grid(array, matrix, start, end):
            clear_matrix(matrix, start, end)
            for cell in array:
                cell.config(text="\u2B1C")
        
        clear_button = tk.Button(
            self.control_frame, 
            text="Clear",
            command= lambda m=self.grid_object.matrix, s=self.grid_object.start, e=self.grid_object.end: clear_grid(grid_cell_array, m, s, e)
            ).pack(side=tk.LEFT, padx=5)
    
        #Save button
        save_button = tk.Button(
            self.control_frame, 
            text="Save"
            ).pack(side=tk.LEFT, padx=5)
        
        #Load button
        load_button = tk.Button(
            self.control_frame, 
            text="Load",
            ).pack(side=tk.LEFT, padx=5)
        
        #Algorythms combox
        Algorythms_list = ttk.Combobox(
            self.control_frame,
            state="readonly",
            values=["djkastra", "algorythm2", "algorythm3"]
        )
        Algorythms_list.pack(side=tk.LEFT, padx=25)
        Algorythms_list.set("Algorythms")

        #Grid Frame
        self.Grid_Frame = tk.Frame(self.parent)
        self.Grid_Frame.pack(pady=10)

        def click_on_cell(cell, matrix, i, j):
            change_cell(matrix, i, j)
            if cell.cget("text") == "\u2B1B":
                cell.config(text="\u2B1C")
            else:
                cell.config(text="\u2B1B")
            print(matrix)

        #Grid
        grid_cell_array = []
        for i in range(len(self.grid_object.matrix)):
            for j in range(len(self.grid_object.matrix[0])):
                cell = tk.Button(
                    self.Grid_Frame,
                    text=self.grid_object.get_symbol(i, j),
                    width=2,
                    height=1,
                )
                cell.grid(row=i, column=j)
                if (j, i) not in [self.grid_object.start, self.grid_object.end]:
                    cell.config(command= lambda b=cell, i=i, j=j: click_on_cell(b, self.grid_object.matrix, i, j))
                    grid_cell_array.append(cell)
