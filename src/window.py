from tkinter import BOTH, Tk, Canvas

from line import Line


class Window():
    def __init__(self, width, heigh):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, width=width, height=heigh)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while (self.running):
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)
