import tkinter as tk
from tkinter import ttk
from utils.visualizer import UI


if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("500x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()