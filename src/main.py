from cell import Cell
from point import Point
from window import Window


def main():
    win = Window(800, 600)

    cell1 = Cell(Point(50, 50), win)
    cell1.draw()
    cell2 = Cell(Point(250, 250), win)
    cell2.draw()

    cell1.draw_move(cell2)

    win.wait_for_close()


if __name__ == "__main__":
    main()
