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

base_layout = ColumnLayout("Grund Layout", app.handle, 5, app.width, height=50,highlight_border=True)
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
# base_layout.add_widget(Clock(app.handle,0,0))
base_layout.add_widget(AutoScrollText(app.handle, 0,0,"Hallo Welt", 5))
app.add_widget(base_layout)
app.render()