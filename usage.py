#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import App
from widgets.text import Text, AutoScrollText
from widgets.clock import Clock
from widgets.shapes import FilledBlock
from widgets.plot import BarPlot, ScatterGrid, TableView
from widgets.layouter import TemplateGridLayout, ColumnLayout


app = App()
# sg = ScatterGrid(app.handle, 10, 10, 5, 5)
# sg.plot([["1", "2", "3"], ["4", " ", "6"], ["", "8", "9"]])
# app.add_widget(sg)
#
# sg2 = ScatterGrid(app.handle, 0,0,10,10)
# sg2.plot([["9", "9", "9"], ["9", "9", "9"], ["9", "9", "9"]])
# sg2.position = sg.left(dim=(sg.width, sg.height))
# app.add_widget(sg2)
# app.render()
base_layout = ColumnLayout("Base Layout", app.handle, 0, 0, 4, app.width, 30, highlight_border=False)


tv = TableView(app.handle, 0,0,10,10)
tv.ingest(
    {
        "COL1": [1, "sehr langer string", "sehr langer string", "sehr langer string", "sehr langer string", "sehr langer string"],
        "COL2": {1, "etwas kurzer eintrag", 3, 4, 5, 6},
        "COL3": {1, 2, 3, 4, 5, 6},
        "COL4": {1, 2, 3, 4, 5, 6}
    }
)
base_layout.add_widget(tv)

bp = BarPlot(app.handle, 0, 0, 10, 10)
base_layout.add_widget(bp)

ascr = AutoScrollText(app.handle,0,0,"Hello Mert this is some text!", 6)
base_layout.add_widget(ascr)

app.add_widget(base_layout)
app.render()
