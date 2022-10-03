#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"


from core import App, Text
from layouter import TemplateGridLayout, ColumnLayout
app = App()
l = ColumnLayout("Grund Layout", app.handle, 3, app.width)
# text =  Text(app.handle, 50, 5, "Eins")
text = ColumnLayout("Layout 2", app.handle, 2)
text.add_widget(Text(app.handle, 0,0,"Test 2-1"))
c2 = ColumnLayout("Layout3", app.handle, 2)
c2.add_widget(Text(app.handle, 0,0,"Test 2-1-2"))
c2.add_widget(Text(app.handle, 0,0,"Test 2-1-3"))
text.add_widget(c2)
text2 =  Text(app.handle, 80, 5, "Zwei")
text3 =  Text(app.handle, 45, 5, "Drei")
l.add_widget(text)
l.add_widget(text2)
l.add_widget(text3)

app.add_widget(l)

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