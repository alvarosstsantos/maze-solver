from line import Line
from point import Point
from window import Window


class Cell():
    def __init__(self, top_left_corner: Point, size: int, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.size = size
        self.win = win

        self.visited = False

        self._set_coordinates(top_left_corner)

    def _set_coordinates(self, top_left_corner: Point):
        if top_left_corner:
            self._x1 = top_left_corner.x
            self._x2 = top_left_corner.x + self.size
            self._y1 = top_left_corner.y
            self._y2 = top_left_corner.y + self.size

    def draw(self, top_left_corner: Point = None):
        self._set_coordinates(top_left_corner)

        if not self.win:
            return

        left_wall_color = "black" if self.has_left_wall else "#d9d9d9"
        self.win.draw_line(
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), left_wall_color)
        right_wall_color = "black" if self.has_right_wall else "#d9d9d9"
        self.win.draw_line(
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), right_wall_color)
        top_wall_color = "black" if self.has_top_wall else "#d9d9d9"
        self.win.draw_line(
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), top_wall_color)
        bottom_wall_color = "black" if self.has_bottom_wall else "#d9d9d9"
        self.win.draw_line(
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), bottom_wall_color)

    def _get_center_point(self):
        return Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, target_cell: "Cell", undo=False):
        fill_color = "gray" if undo else "red"

        if not self.win:
            return

        self.win.draw_line(Line(self._get_center_point(),
                                target_cell._get_center_point()), fill_color)
