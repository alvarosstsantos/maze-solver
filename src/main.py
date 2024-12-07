from maze import Maze
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(Point(49, 49), 7, 5, 100, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
