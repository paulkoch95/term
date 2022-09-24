#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import TemplateGridLayout, ColumnLayout
app = App()
l = ColumnLayout("Test Layout", app.handle, 5)
text =  Text(app.handle, 25, 5, "data")
# exit(1)
import copy
text2 =  Text(app.handle, 5, 5, f"Type Window {type(app._window)}")
text3 =  Text(app.handle, 45, 5, "weit weg")
text4 =  Text(app.handle, 45, 15, "noch weiter weg")
text5 =  Text(app.handle, 45, 15, "test")
text6 =  Text(app.handle, 45, 15, "test3")
nested_l = ColumnLayout("Zweites Layout", app.handle, 2)
nested_l.add_widget(Text(app.handle, 0,0,"Eins"))
# nested_l.add_widget(Text(app.handle, 0,0,"Zwei"))

l.add_widget(text2)
l.add_widget(text3)
l.add_widget(text4)
l.add_widget(nested_l)
l.add_widget(text5)
# l.add_widget(nested_l)
# print(nested_l.position)
app.add_widget(l)
# l.render()
# app.add_widget(text2)
# app.add_widget(text3)
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