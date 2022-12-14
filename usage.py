#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from core import App, Renderable
from widgets.text import Text, AutoScrollText, ROTATION
from widgets.clock import Clock
from widgets.shapes import FilledBlock
from widgets.plot import BarPlot, ScatterGrid, TableView
from widgets.layouter import TemplateGridLayout, ColumnLayout
from utils.drawing import Drawing


"""
sg = ScatterGrid(app.handle, 10, 10, 5, 5)
sg.plot([["1", "2", "3"], ["4", " ", "6"], ["", "8", "9"]])
app.add_widget(sg)

sg2 = ScatterGrid(app.handle, 0,0,10,10)
sg2.plot([["9", "9", "9", "8"], ["9", "9", "9","8"], ["9", "9", "9","8"],["9", "9", "9","8"]])
# sg2.position = sg.left(dim=(sg2._w, sg2._h), pos=Renderable.POSITION.END)
# sg2.position = sg.top(dim=(sg2._w, sg2._h), pos=Renderable.POSITION.END)
# sg2.position = sg.right(dim=(sg2._w, sg2._h), pos=Renderable.POSITION.BEGINNING)
sg2.position = sg.bottom(dim=(sg2._w, sg2._h), pos=Renderable.POSITION.END)
# sg2._x -= sg2._w
# sg2.position = (0, 0)
app.add_widget(sg2)
app.render()
exit()
"""
def simple_pos_demo():
    app = App()

    sc = ScatterGrid(app.handle, app.center[0], app.center[1], 5, 5)
    sc.plot([["1", "2", "3"], ["4", " ", "6"], ["", "8", "9"]])

    txt = Text(app.handle, 10, 10, "Hallo Welt", rotation=ROTATION.FOURTY_FIVE_DEGREE)
    txt2 = Text(app.handle, 11, 10, "Hallo Welt", rotation=ROTATION.FOURTY_FIVE_DEGREE)


    bp = BarPlot(app.handle, 0, 0, 20, 10)
    # bp.position = sc.left(dim = (bp.width, bp.height))
    bp.position = app.center
    bp.add_bar(10)
    bp.add_bar(11)
    bp.add_bar(12)
    bp.add_bar(12)
    bp.add_bar(12)
    # bp.add_bar(12)


    # app.add_widget(sc)
    app.add_widget(bp)
    app.add_widget(txt)
    app.add_widget(txt2)
    app.render()

def datascience_demo():
    app = App()
    base_layout = ColumnLayout("Base Layout", app.handle, 0, 0, 2, app.width, 30, highlight_border=False)
    tv = TableView(app.handle, 0,0,10,10)
    tv.ingest(
        {
            "COL1": [1, "sehr langer string", "sehr langer string", "sehr langer string", "sehr langer string", "sehr langer string"],
            "COL2": {1, "etwas kurzer eintrag", 3, 4, 5, 6},
            "COL3": {1, 2, 3, 4, 5, 6},
            "COL4": {1, 2, 3, 4, 5, 6}
        }
    )

    bp = BarPlot(app.handle, 0, 0, 10, 10)
    bp.add_bar(10)
    bp.add_bar(11)
    bp.add_bar(12)
    bp.add_bar(12)
    bp.add_bar(12)
    base_layout.add_widget(bp)
    base_layout.add_widget(tv)

    app.add_widget(base_layout)
    app.render()
# simple_pos_demo()
datascience_demo()