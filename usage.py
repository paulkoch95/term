#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import App, Text, Clock, BarPlot
from layouter import TemplateGridLayout, ColumnLayout
app = App()

base_layout = ColumnLayout("Grund Layout", app.handle, 5, app.width, height=50,highlight_border=True)
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
app.add_widget(base_layout)
app.render()