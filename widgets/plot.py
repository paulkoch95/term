__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import random

from core import Renderable
from utils.drawing import Drawing
from widgets.text import AutoScrollText
import curses
from typing import Iterable


class BarSlot:

    def __init__(self, index_pos: int, desc: str, val: float):
        self.index = index_pos
        self.description = desc
        self.data = val


class BarPlot(Renderable):
    """
    Bar Plot Widget:
    Renders a horizontal Bar Plot

    Vertical Axis (y - Axis) (fills entire height available to widget)
    |
    v

    |   # <- Single Column Data Point (every Data Point is BarSlot object)
    |   #
    |   #
    |-----------    <- x-Axis (Horizontal Axis) (fills entire width available to widget)

    Data can be added, removed or update on runtime. Axis are fully dynamic based on the current that is
    to be plotted.
    """
    def __init__(self, render: curses.window, x: int, y: int, w: int, h: int):
        super().__init__(render, x, y, w, h)
        self.bars: list[BarSlot] = []
        self.max_height: int = 0
        self.horizontal_offset = 3

    def add_bar(self, val):
        """
        Adds a BarSlot object to the BarPlot Widget. Essentially plotting a new column of data.
        """
        s = BarSlot(len(self.bars), f'Test Bar {len(self.bars)}', val)
        self.bars.append(s)

    def remove_bar(self, idx):
        """
        Remove a data point that is being plotted. Deletes the whole BarSlot Object from the list which also updates the drawing
        """
        del self.bars[idx]

    def update_bar(self, idx, val):
        """
        Update a specific column BarSlot data point.
        """
        self.bars[idx].data = val

    def update(self):
        for bar in self.bars:
            bar.data = random.randint(0,25)

    def render(self) -> None:
        # intermediate constants to allow the rendering
        self.max_height = max(self.max_height, max(bar.data for bar in self.bars))
        # horizontal x-axis object which also returns the indices where a BarSlot shoudl be rendered. will be
        # replaced by its own AXIS Class in the future to allow interchangable axis between different types of graphs
        # and to also accept pyplot axis objects.
        data_points = Drawing.h_line_staggered(self._ctx, self._y + self.height+1, self._x+self.horizontal_offset, self.width, len(self.bars))
        Drawing.v_line_staggered(self._ctx, self._y + self.height, self._x, self.max_height, 2)
        bar: BarSlot
        for idx, bar in enumerate(self.bars):
            Drawing.block_v_line(self._ctx, self._y + self._h, self._x + data_points[idx]+self.horizontal_offset, bar.data)
        # Drawing.draw_text_label(self._ctx, 0,0,str(data_points))
        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 1, self.bar_height)
        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 2, self.bar_height)
        # Drawing.block_v_line(self._ctx, self._y + 24, self._x + 4, self.bar_height)


class ScatterGrid(Renderable):
    def __init__(self, render: curses.window, x: int, y: int, w: int, h: int):
        super().__init__(render, x, y, w, h)
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
        self.title = AutoScrollText(render, self._x, self._y, "Hallo Welt", 4)
        self.data = {}

    def update(self):
        self.title.update()
        # TODO: This sould be natively done by the Parent Widget Upon x, y, w or h change.
        self.title.position = (self._x, self._y)

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
