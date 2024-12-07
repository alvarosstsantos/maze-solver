from maze import Maze
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(Point(9, 9), 39, 29, 20, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
