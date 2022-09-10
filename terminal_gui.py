import curses
from curses.textpad import rectangle
from curses import panel
import random
import time
import sys
import numpy as np
import abc

__author__ = "Paul Koch"

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

    def __init__(self, render, y):
        self._w = render
        self.y = y

    def render(self):
        self._w.addstr(self.y,0,"Test String")


app = App()
text =  Renderable(app.get_window_handle(),5)
text2 = Renderable(app.get_window_handle(), 10)
text3 = Renderable(app.get_window_handle(), 15)
app.add_widget(text)
app.add_widget(text2)
app.add_widget(text3)
app.render()
# text = Renderable(app)
# app.add_widget(text)
# app.render()

"""while running:
    max_y, max_x = stdscr.getmaxyx()
    data_x = np.arange(max_x-5)
    data_y = np.sin(data_x / 2) * 10
    stdscr.addstr(0,0,f'MAX_X {max_x}; MAX_Y {max_y}, type {type(stdscr)}')
    for n, i in enumerate(data_y):
        stdscr.addch(int(i)+10,n,"*")

        stdscr.refresh()
        time.sleep(.005)
    time.sleep(.5)#
"""