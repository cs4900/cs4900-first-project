from tkinter import *
import tkinter as tk
import mpmath
import sympy
import pytest


class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyCompGeo")
        self.geometry('800x500+0+0')
        self.resizable(True, True)
        #self.iconphoto(False, tk.PhotoImage(file="assets/title_icon.png"))
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    app = MainUI()
    app.mainloop()