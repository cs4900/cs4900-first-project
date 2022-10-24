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


class PyCompGeo(App):
    def build(self):
        return PyCompGeoMainWindow()

if __name__ == "__main__":
   PyCompGeo().run()