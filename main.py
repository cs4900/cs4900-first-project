from tkinter import *
import tkinter as tk
import mpmath
import sympy
import pytest
import scipy.spatial


# class MainUI(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("PyCompGeo")
#         self.geometry('800x500+0+0')
#         self.resizable(True, True)
#         #self.iconphoto(False, tk.PhotoImage(file="assets/title_icon.png"))
#         container = tk.Frame(self, bg="#8AA7A9")
#         container.pack(side="top", fill="both", expand = True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

# if __name__ == "__main__":
#     app = MainUI()
#     app.mainloop()


def calculate_intersection(points):
    l1 = sympy.Line(points[0], points[1])
    l2 = sympy.Line(points[2], points[3])
    intersection = sympy.intersection(l1, l2)
    print(intersection[0].coordinates)
    return intersection[0].coordinates


# def calculate_largest_cricle(points):
#     for i in points:



#Quick Sympy test
# p1 = sympy.Point(0,0)
# p2 = sympy.Point(2,2)
# p3 = sympy.Point(0,2)
# p4 = sympy.Point(2,0)
# l1 = sympy.Line(p1,p2)
# l2 = sympy.Line(p3,p4)
# intersection= sympy.intersection(l1, l2)
# print(intersection)

#  for largest empty circle, calculate distance from point to all other points
#  and take it's shortest distance.  Then find the largest of all those
#  shortest distances and that point is the circle.