__author__ = "Paul Koch"
__maintainer__ = "Rob Knight"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from drawing import Drawing
import curses


class Text(Renderable):
    """
    Simple arbitrary Text Widget that displays text at given position.
    """

    def __init__(self, render: curses.window, x, y, text):
        super().__init__(render, x, y)
        self._text = text

    @property
    def text(self):
        return self._text

    def render(self):
        Drawing.draw_text_label(self._ctx, self._y, self._x, self._text)


class AutoScrollText(Renderable):

    def __init__(self, render: curses.window, x, y, text: str, len_disp: int):
        super().__init__(render, x, y)
        self._text_raw = text + (" "*len_disp)
        self._text = self._text_raw
        self._len_disp = len_disp
        self.i = 0

    def update(self):
        self._text = self._text_raw[self.i: self.i+self._len_disp]
        if self.i < len(self._text_raw)-(self._len_disp):
            self.i +=1
        else:
            self.i = 0
        # if len(self._text) > self._len_disp:
        #     self._text = self._text_raw[:self._len_disp]

    def render(self):
        Drawing.draw_text_label(self._ctx, self._y, self._x, self._text)
