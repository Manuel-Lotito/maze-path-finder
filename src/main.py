import tkinter as tk
from ui.visualizer import UI


if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("550x650")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
