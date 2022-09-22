#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import TemplateGridLayout, ColumnLayout
app = App()
l = ColumnLayout("Test Layout", app.handle, 5)
print(l._name)
text =  Text(app.handle, 25, 5, "data")
print(app)
# exit(1)
text2 =  Text(app.handle, 5, 5, f"Type Window {type(app._window)}")
text3 =  Text(app.handle, 45, 5, "weit weg")
l.add_widget(text2)
l.add_widget(text3)
app.add_widget(l)
# l.render()
# app.add_widget(text2)
# app.add_widget(text3)
app.render()
print(text)

g = """ .   .       .      .
        .   name    name   .
        .   name    name   block
        .   class   .      .
        .   .       .      ."""
"""

l = GridLayout("Test", g, app.get_window_handle())
l.resolve_grid()
while running:
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