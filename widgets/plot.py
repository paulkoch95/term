__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from utils.drawing import Drawing
from widgets.text import AutoScrollText
import curses


class BarPlot(Renderable):

    def __init__(self, render: curses.window, x: int, y: int, w: int, h: int):
        super().__init__(render, x, y)
        self.bar_height = 1

    def update(self):
        if self.bar_height > 5:
            self.bar_height = 0
        else:
            self.bar_height += 1

    def render(self) -> None:
        Drawing.h_line_staggered(self._ctx, self._y + self.height - 3, self._x, self.width, 5)
        # Drawing.v_line_staggered(self._ctx, self._y + (self.height+3), self._x, self.height, 5)

        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 1, self.bar_height)
        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 2, self.bar_height)
        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 4, self.bar_height)


class ScatterGrid(Renderable):
    def __init__(self, render: curses.window, x: int, y: int, w: int, h: int):
        super().__init__(render, x, y)
        self.data: list[list] = [[]]  # [ - rows [ - cols]]

    def plot(self, data: list[list]) -> None:
        """
        Ingest plotting data, must be two-dimensional, flattening should be done beforehand
        """
        self.data = data
        self._w = len(data)
        self._h = len(data[0])

    def render(self):
        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                Drawing.draw_text_label(self._ctx, self._y + y, self._x + x, col)


class TableView(Renderable):
    def __init__(self, render: curses.window, x: int, y: int, w: int, h: int):
        super().__init__(render, x, y)
        self.title = AutoScrollText(render, 5, 0, "Hallo Welt", 4)
        self.data = {}

    def update(self):
        self.title.update()

    def ingest(self, data):
        self.data = data

    def render(self):
        max_len = 0
        len_longest_column = 0
        for col, (k, v) in enumerate(self.data.items()):
            lst = [k, *v]
            lst = [str(i) for i in lst]
            len_longest_column = max(len_longest_column, len(lst))
            max_len = self.width // len(self.data.keys())
            for y, row in enumerate(lst):
                Drawing.draw_text_label(self._ctx, (self._y + y) * 2 + 1, self._x + 1 + (col * max_len) + 1, row)
        Drawing.draw_grid(self._ctx, self._y, self._x, len_longest_column, len(self.data.items()), max_len, 2)
        self.title.render()
