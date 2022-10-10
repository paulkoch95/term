__author__ = "Paul Koch"
__maintainer__ = "Rob Knight"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from drawing import Drawing
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
        Drawing.h_line_staggered(self._ctx, self._y + 27, self._x, 25, 5)
        Drawing.v_line_staggered(self._ctx, self._y + 25, self._x, 25, 5)
        Drawing.block_v_line(self._ctx, self._y + 24, self._x + 1, self.bar_height)
        Drawing.block_v_line(self._ctx, self._y + 24, self._x + 2, self.bar_height)
        Drawing.block_v_line(self._ctx, self._y + 24, self._x + 4, self.bar_height)
