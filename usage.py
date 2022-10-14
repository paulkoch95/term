#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import App
from widgets.text import Text, AutoScrollText
from widgets.clock import Clock
from widgets.plot import BarPlot
from widgets.layouter import TemplateGridLayout, ColumnLayout
app = App()

base_layout = ColumnLayout("Base Layout", app.handle, 0,20,2, app.width, height=40,highlight_border=True)
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
nested_layout = ColumnLayout("Nested", app.handle, 0,0,3, 50, highlight_border=True)
base_layout.add_widget(nested_layout)
# base_layout.add_widget(nested_layout)
# base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
nested_layout.add_widget(BarPlot(app.handle, 0,0,10,10))
nested_layout.add_widget(BarPlot(app.handle, 0,0,10,10))
nested_layout2 = ColumnLayout("Nested", app.handle, 0,0,2, 50, highlight_border=True)
nested_layout2.add_widget(BarPlot(app.handle, 0,0,10,10))
nested_layout2.add_widget(BarPlot(app.handle, 0,0,10,10))
nested_layout.add_widget(nested_layout2)
# base_layout.add_widget(Clock(app.handle,0,0))
# base_layout.add_widget(AutoScrollText(app.handle, 0,0,"Lets test a really long string here!", 15))
app.add_widget(base_layout)
app.render()