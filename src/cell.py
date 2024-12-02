from line import Line
from point import Point
from window import Window

WIDTH = 10


class Cell():
    def __init__(self, top_left_corner: Point, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left_corner.x
        self._x2 = top_left_corner.x + WIDTH
        self._y1 = top_left_corner.y
        self._y2 = top_left_corner.y + WIDTH
        self._win = win

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y1 + WIDTH)))
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x1 + WIDTH, self._y1), Point(self._x1 + WIDTH, self._y1 + WIDTH)))
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1 + WIDTH, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1 + WIDTH), Point(self._x1 + WIDTH, self._y1 + WIDTH)))
