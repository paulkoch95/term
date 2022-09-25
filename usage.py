#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import TemplateGridLayout, ColumnLayout
app = App()
l = ColumnLayout("Test Layout", app.handle, 3, app.width)
text =  Text(app.handle, 50, 5, "data")
# exit(1)
import copy
text2 =  Text(app.handle, 80, 5, "Eins")
text3 =  Text(app.handle, 45, 5, "ZWei")
text4 =  Text(app.handle, 45, 15, "Drei")
text5 =  Text(app.handle, 45, 15, "Vier")
# text6 =  Text(app.handle, 45, 15, "Fuenf")
nested_l = ColumnLayout("Zweites Layout", app.handle, 4)
nested_l.add_widget(Text(app.handle, 0,0,"Eins"))
nested_l.add_widget(Text(app.handle, 0,0,"Zwei"))
nested_l.add_widget(Text(app.handle, 0,0,"Zwei"))
nested_l.add_widget(Text(app.handle, 0,0,"Zwei"))

l.add_widget(text2)
l.add_widget(text3)
# l.add_widget(text4)
# l.add_widget(nested_l)
# l.add_widget(text5)
# l.add_widget(text6)
l.add_widget(nested_l)
app.add_widget(l)
# l.render()
# app.add_widget(text2)

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