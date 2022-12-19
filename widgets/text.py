__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from utils.drawing import Drawing
import curses
from enum import Enum


class ROTATION(Enum):
    FOURTY_FIVE_DEGREE = 1
    VERTICAL = 2


class Text(Renderable):
    """
    Simple arbitrary Text Widget that displays text at given position.
    """

    def __init__(self, render: curses.window, x, y, text, rotation=None):
        super().__init__(render, x, y)
        self._text = text
        self._rotation = rotation
    @property
    def text(self):
        return self._text

    def render(self):
        if self._rotation:
            if self._rotation == ROTATION.FOURTY_FIVE_DEGREE:
                chars = list(self._text)
                # chars.reverse()

                for idx, pos in enumerate(chars):
                    Drawing.draw_text_label(self._ctx, self._y-idx, self._x+idx, pos)
                Drawing.debug_marker(self._ctx, self._y, self._x)
                Drawing.debug_marker(self._ctx, self._y-len(chars), self._x+len(chars))
        else:
            Drawing.draw_text_label(self._ctx, self._y, self._x, self._text)


class AutoScrollText(Renderable):

    def __init__(self, render: curses.window, x, y, text: str, len_disp: int):
        super().__init__(render, x, y)
        self._text_raw = text + (" "*len_disp)
        self._text = self._text_raw
        self._len_disp = len_disp

        self.width = self._len_disp # TODO: Make dynamic
        self.height = 1 # TODO: Make dynamic

        self.i = 0

    def update(self):
        self._text = self._text_raw[self.i: self.i+self._len_disp]
        if self.i < len(self._text_raw)-(self._len_disp):
            self.i +=1
        else:
            self.i = 0

    def render(self):
        Drawing.draw_text_label(self._ctx, self._y, self._x, self._text)
