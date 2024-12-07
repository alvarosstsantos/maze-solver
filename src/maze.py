from time import sleep
from typing import List
from cell import Cell
from point import Point
from window import Window


class Maze():
    def __init__(
        self,
        top_left_corner: Point,
        num_rows: int,
        num_cols: int,
        cell_size: int,
        win: Window = None,
    ):
        self.top_left_corner = top_left_corner
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self.cells: List[List[Cell]] = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell = Cell(Point(self.top_left_corner.x + i * self.cell_size,
                                  self.top_left_corner.y + j * self.cell_size),
                            self.cell_size,
                            self.win)

                row.append(cell)

            self.cells.append(row)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
                self._animate()

    def _draw_cell(self, i: int, j: int):
        self.cells[i][j].draw()

    def _animate(self):
        if not self.win:
            return

        self.win.redraw()
        sleep(0.05)
