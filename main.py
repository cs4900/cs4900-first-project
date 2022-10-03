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
        Comp = CompDropDown(container)
        Comp.test_dropdown()
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

class CompDropDown(tk.Tk):
    def __init__(self, container):
        self.container = container
        self.currentFrame = None

    def test_dropdown(self):
        # options for dropdown box
        options = [
            "frame1",
            "frame2"
        ]

        selected = StringVar()
        # set default value to none
        selected.set(None)
        # trace selected variable and setup callback to call change_ui when value changed
        selected.trace_add("write", lambda var, index, operation:self.change_frame(selected))

        # create dropdown box
        drop = OptionMenu(self.container, selected, *options)
        drop.config(width=10)
        # render
        drop.pack(anchor="nw", padx=(3,3), pady=(3,3))

    # event handler for when value is changed in dropdown
    def change_frame(self, selected):
        option = selected.get()
        if option == "frame1":
            # unpack current frame
            self.unpack_frame(self.currentFrame)
            # pack next frame and set currentFrame as packed frame
            self.currentFrame = self.frame1()
        elif option == "frame2":
            self.unpack_frame(self.currentFrame)
            self.currentFrame = self.frame2()

    # unpack frame when switched off
    def unpack_frame(self, frame):
        if frame is not None:
            frame.destroy()

    # test frame 1
    def frame1(self):
        frame = Frame()
        label = Label(frame, text="you are in frame1", justify=CENTER)
        label.pack()
        frame.pack()
        return frame

    # test frame 2
    def frame2(self):
        frame = Frame()
        label = Label(frame, text="you are in frame2", justify=CENTER)
        label.pack()
        frame.pack()
        return frame



class CompFrame(tk.Tk):
    pass


if __name__ == "__main__":
    app = MainUI()
    app.mainloop()