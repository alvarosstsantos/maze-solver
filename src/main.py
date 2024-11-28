from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(0, 0), Point(800, 600)), "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
