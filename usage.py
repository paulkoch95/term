#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import GridLayout

g = """ .   .       .      .
        .   name    name   .
        .   name    name   .
        .   class   .      .
        .   .       .      ."""
# g = """."""
app = App()
l = GridLayout("Test", g, app.get_window_handle())
l.resolve_grid()

exit(1)
text =  Text(app.get_window_handle(),15,5, "data")
print(text)
app.add_widget(text)
app.render()

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