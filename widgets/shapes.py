__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from drawing import Drawing, Chars
import curses


class FilledBlock(Renderable):

    def __init__(self, render: curses.window, x, y, w = 10, h = 10):
        super().__init__(render, x, y)
        self.block_width = w
        self.block_height = h

    def render(self):

        for height in range(self.block_height):
            for width in range(self.block_width):
                self._ctx.addch(self._y+height, self._x+width, Chars.UPPER_HALF.value)
