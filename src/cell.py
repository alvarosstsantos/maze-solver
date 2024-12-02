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

        self._win = win

        self._set_coordinates(top_left_corner)

    def _set_coordinates(self, top_left_corner: Point):
        if top_left_corner:
            self._x1 = top_left_corner.x
            self._x2 = top_left_corner.x + WIDTH
            self._y1 = top_left_corner.y
            self._y2 = top_left_corner.y + WIDTH

    def draw(self, top_left_corner: Point = None):
        self._set_coordinates(top_left_corner)

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

    def get_center_point(self):
        return Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, target_cell: "Cell", undo=False):
        fill_color = "gray" if undo else "red"

        self._win.draw_line(Line(self.get_center_point(),
                            target_cell.get_center_point()), fill_color)
