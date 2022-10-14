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
import abc
from typing import Union
from drawing import Drawing
import locale

locale.setlocale(locale.LC_ALL, '')


class App:

    def __init__(self):
        self._window = curses.initscr()
        # curses.start_color()
        curses.curs_set(2)
        self._height, self._width = self._window.getmaxyx()
        self._renderables = []

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
    def handle(self) -> curses.window:
        return self._window

    def render(self) -> None:
        while True:
            self._window.clear()
            # print(event)
            ctx: Renderable
            for ctx in self._renderables:
                ctx.update()
                ctx.render()
            self._window.refresh()
            time.sleep(0.25)


class Renderable:
    """
    Base Class for all objects that can be displayed on the "screen" terminal.
    """

    def __init__(self, render, x, y):
        self._ctx = render
        self._x = x
        self._y = y
        self._w = -99
        self._h = -99

    def render(self):
        """
        This Method has to be overwritten by widgets of any sort. Raises an error if not implemented.
        TODO: Default visualization incase method is not overwritten (e.g. show bounding box, print position and size)
        """
        raise NotImplementedError

    def update(self):
        """
        This Method is called by the render loop at predefined intervalls and helps to seperate logic from rendering.
        """
        pass
    
    def name(self) -> str:
        return self.__class__.__name__

    def __repr__(self):
        return (f'Name: {self.__class__.__name__} X: {self._x} Y {self._y} W {self._w} H {self._h}')

    @property
    def position(self):
        return (self._x, self._y)

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

