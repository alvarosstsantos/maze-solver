from cell import Cell
from point import Point
from window import Window


def main():
    win = Window(800, 600)

    cell = Cell(Point(50, 50), win)
    cell.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
