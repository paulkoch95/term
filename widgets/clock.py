__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import Renderable
from drawing import Drawing
import curses
import time


class Clock(Renderable):

    def __init__(self, render: curses.window, x, y):
        super().__init__(render, x, y)
        self.time = str(0)

    def update(self):
        self.time = str(time.strftime('%H:%M:%S'))

    def render(self):
        Drawing.draw_text_label(self._ctx, self._y, self._x, self.time + "█")