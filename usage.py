#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import TemplateGridLayout, ColumnLayout
app = App()
third_layout = ColumnLayout("Third", app.handle, 2)
third_layout.add_widget(Text(app.handle, 0,0,"2-1"))
third_layout.add_widget(Text(app.handle, 0,0,"2-1"))
base_layout = ColumnLayout("Grund Layout", app.handle, 3, app.width)
base_layout.add_widget(Text(app.handle, 0,0,"Hallo Welt"))
base_layout.add_widget(Text(app.handle, 0,0,"Hallo Welt"))
second_layout = ColumnLayout("Second", app.handle, 3)
second_layout.add_widget(Text(app.handle, 0,0,"EINS"))
second_layout.add_widget(Text(app.handle, 0,0,"ZWEI"))
base_layout.add_widget(second_layout)
second_layout.add_widget(third_layout)
app.add_widget(base_layout)
app.render()

g = """ .   .       .      .
        .   name    name   .
        .   name    name   block
        .   class   .      .
        .   .       .      ."""
"""

l = GridLayout("Test", g, app.get_window_handle())
l.resolve_grid()
"""