from gc import callbacks
from optparse import Option
from tkinter import *
import mpmath
import sympy
import pytest

class MainUI:
    def __init__(self):
        self.root = Tk()
        self.currentFrame = None
        # render test window
        self.test_window()

    # function to render test_window
    def test_window(self):
        self.root.title('Hello World')
        self.root.geometry("500x300+10+20")
        # render dropdown box
        self.test_dropdown()
        self.root.mainloop()

    # render dropdown box
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
        drop = OptionMenu(self.root, selected, *options)
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
        frame = Frame(self.root)
        label = Label(frame, text="you are in frame1", justify=CENTER)
        label.pack()
        frame.pack()
        return frame

    # test frame 2
    def frame2(self):
        frame = Frame(self.root)
        label = Label(frame, text="you are in frame2", justify=CENTER)
        label.pack()
        frame.pack()
        return frame


if __name__ == "__main__":
    mainUI = MainUI()
    mainUI.test_window()
