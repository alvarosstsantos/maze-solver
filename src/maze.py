import random
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
        seed: int = None
    ):
        self.top_left_corner = top_left_corner
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self.cells: List[List[Cell]] = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        sleep(0.0005)

    def _break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        exit = self.cells[self.num_rows - 1][self.num_cols - 1]

        entrance.has_top_wall = False
        entrance.draw()

        exit.has_bottom_wall = False
        exit.draw()

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False

    def _break_walls_r(self, i: int, j: int):
        self.cells[i][j].visited = True

        while True:
            next_index_list = []

            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))

            if i < self.num_rows - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))

            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))

            if j < self.num_cols - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False

            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False

            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False

            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int):
        self._animate()

        self.cells[i][j].visited = True

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        if (
            i < self.num_rows - 1
            and not self.cells[i][j].has_right_wall
            and not self.cells[i + 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)

        if (
            j > 0
            and not self.cells[i][j].has_top_wall
            and not self.cells[i][j - 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        if (
            j < self.num_cols - 1
            and not self.cells[i][j].has_bottom_wall
            and not self.cells[i][j + 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        return False
