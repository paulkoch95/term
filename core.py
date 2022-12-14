#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses
from enum import Enum
import time
from utils.drawing import Drawing
import locale
import logging
locale.setlocale(locale.LC_ALL, '')


class LogStream(object):
    def __init__(self):
        self.logs = []

    def write(self, str):
        self.logs.append(str)

    def flush(self):
        pass

    def __str__(self):
        return " _ ".join(self.logs)


log_stream = LogStream()
logging.basicConfig(stream=log_stream, level=logging.DEBUG)
term_logger = logging.getLogger('term')


class App:

    def __init__(self):
        self._window = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.curs_set(2)
        self._height, self._width = self._window.getmaxyx()
        self._renderables = []
        self.debug: dict = {}

    def __repr__(self):
        return f"Window {self._window}, Width: {self._width}, Height: {self._height}"

    def add_widget(self, widget: 'Renderable') -> None:
        from widgets import layouter
        if isinstance(widget, layouter.LayoutMethod):
            widget.place_widgets()
        self._renderables.append(widget)

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    @property
    def center(self)-> tuple[int, int]:
        return self._width//2, self._height//2

    @property
    def handle(self) -> curses.window:
        return self._window

    def render_debug_data(self) -> None:
        """
        Renders a dict of entries for debug purposes. Eases debugging for "print" users due to curses messing up
        conventional printing using print()
        """
        for idx, (k, v) in enumerate(self.debug.items()):
            Drawing.draw_text_label(self._window, self.height - (len(self.debug.keys())) + idx, 0, f"{k}: {v}")

    def render(self) -> None:
        """
        Base Render Class for any renderable object. Calls render method on all its childs --> one App holds all
        drawable items.
        """
        while True:
            self._window.clear()
            ctx: Renderable
            for ctx in self._renderables:
                ctx.update()
                ctx.render()

            self.debug["Widget Count"] = str(len(self._renderables)) + " : " + str([type(i) for i in self._renderables])
            self.debug["Color"] = "Terminal supports colors" if curses.has_colors() else "No color support."
            self.debug["Time"] = str(time.time())
            self.debug["Errors"] = str(log_stream.logs)

            self.render_debug_data()

            self._window.refresh()

            time.sleep(0.25)


class Renderable:
    """
    Base Class for all objects that can be displayed on the "screen" terminal.
    """

    class POSITION(Enum):
        BEGINNING = 0
        MIDDLE = 1
        END = 2

    def __init__(self, render, x, y, w=None, h=None):
        self._ctx = render
        self._x = x
        self._y = y
        self._w = w if w else -99
        self._h = h if h else -99

    def render(self):
        """
        This Method has to be overwritten by widgets of any sort. Raises an error if not implemented.
        TODO: Default visualization incase method is not overwritten (e.g. show bounding box, print position and size)
        """
        raise NotImplementedError

    def update(self):
        """
        This Method is called by the render loop at predefined intervals and helps to seperate logic from rendering.
        """
        pass

    def name(self) -> str:
        return self.__class__.__name__

    def __repr__(self):
        return f'Name: {self.__class__.__name__} X: {self._x} Y {self._y} W {self._w} H {self._h}'

    @property
    def position(self):
        return self._x, self._y

    @position.setter
    def position(self, position):
        self._x, self._y = position

    @property
    def width(self):
        return self._w

    @property
    def height(self):
        return self._h

    @width.setter
    def width(self, width):
        self._w = width

    @height.setter
    def height(self, height):
        self._h = height

    def left(self, pos: POSITION = POSITION.BEGINNING, dim: tuple[int, int] = None):
        return self._x-dim[0], self._y+(pos.value * self._h//3)

    def top(self, pos: POSITION = POSITION.BEGINNING, dim: tuple[int, int] = None):
        return self._x+(pos.value*self._w//3), self._y-dim[1]

    def right(self, pos: POSITION = POSITION.BEGINNING, dim: tuple[int, int] = None):
        return self._x+self._w, self._y+(pos.value * self._h//3)

    def bottom(self, pos: POSITION = POSITION.BEGINNING, dim: tuple[int, int] = None):
        return self._x+(pos.value * self._w//3), self._y+self._h


