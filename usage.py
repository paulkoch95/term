#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import App
from widgets.text import Text, AutoScrollText
from widgets.clock import Clock
from widgets.shapes import FilledBlock
from widgets.plot import BarPlot
from widgets.layouter import TemplateGridLayout, ColumnLayout
app = App()

base_layout = ColumnLayout("Base Layout", app.handle, 0,0,2, app.width,10,highlight_border=True)
base_layout.add_widget(BarPlot(app.handle, 0, 0, 10, 10))
base_layout.add_widget(FilledBlock(app.handle, 0, 0, 5, 5 ))
app.add_widget(base_layout)
app.render()