#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses
from curses.textpad import rectangle
from curses import panel
import random
import time
import sys
import numpy as np
import abc


class App:

    def __init__(self):
        self._window = curses.initscr()
        curses.curs_set(2)
        self._height, self._width = self._window.getmaxyx()
        self._renderables  = []

    def __repr__(self):
        return f"Window {self._window}, Width: {self._width}, Height: {self._height}"

    def update(self):
        pass

    def add_widget(self, widget: 'Renderable'):
        self._renderables.append(widget)

    def get_window_handle(self):
        return self._window

    def render(self):
        while True:
            ctx: Renderable
            for ctx in self._renderables:
                ctx.render()
            self._window.refresh()
            time.sleep(0.5)


class Renderable:
    """
    Base Class for all objects that can be displayed on the "screen" terminal.
    """
    def __init__(self, render, x, y):
        self._w = render
        self._x = x
        self._y = y

    def render(self):
        """
        This Method has to be overwritten by widgets of any sort. Raises an error if not implemented.
        TODO: Default visualization incase method is not overwritten (e.g. show bounding box, print position and size)
        :return:
        """
        raise NotImplementedError

    def __repr__(self):
        return(f'X: {self._x} Y {self._y} W {-1} H {-1}')


class Text(Renderable):
    """
    Simple arbitrary Text Widget that displays text at given position.
    """
    def __init__(self, render, x, y, text):
        super().__init__(render, x, y)
        self._text = text

    @property
    def text(self):
        return self._text

    def render(self):

        self._w.addstr(self._y,self._x, self._text)
