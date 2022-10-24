from tkinter import Widget
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window


class PyCompGeoMainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(PyCompGeoMainWindow, self).__init__(**kwargs)
        Window.size = (800, 500)
        self.cols = 1


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
   PyCompGeo().run()