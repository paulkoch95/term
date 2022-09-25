#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses
from dataclasses import dataclass
from core import Renderable
from enum import Enum
import _curses

class ComponentType(Enum):
    EMPTY_COMPONENT = 0,
    NAMED_COMPONENT = 1


@dataclass
class ComponentPlaceholder:
    type: ComponentType
    name: str = ""
    x: int = 0
    y: int = 0
    set_width: int = 0
    set_height: int = 0


class EmptyLayoutException(Exception):
    pass


class Layout:

    def __init__(self, layout_desc):
        """
        Create a new Layout Manager that handles the layouting based on the selected method.
        :param layout_desc: The Layouting Method that is used to place all widgets in a window.
        """
        self.layout = layout_desc


class LayoutMethod():

    def __init__(self, name, window):
        super().__init__(window, 0, 0)
        self._name = (self.name(), name)

    @property
    def position(self):
        return self._x, self._y
    @position.setter
    def position(self, position):
        self._x, self._y = position
        self.place_widgets()

    @classmethod
    def name(cls):
        return cls.__name__

    def place_widgets(self):
        raise NotImplementedError

class ColumnLayout(LayoutMethod, Renderable):
    def __init__(self, name, window: _curses.window, num_cols, width = 10):
        super().__init__(name, window)
        self._cols = num_cols
        self._widgets: list[Renderable] = []
        self.width = width
        self.max_h, _  = window.getmaxyx()

    def render(self):
        for r in self._widgets:
            r.render()

    def add_widget(self, widget: Renderable):
        if len(self._widgets) == self._cols: raise Exception(f'Max Num of slots reached! {len(self._widgets)}/{self._cols}')
        widget.width = int(self.width/self._cols)
        widget.height = self.max_h
        widget.position = (int(self.width/self._cols)*len(self._widgets)+1, 0)
        self._widgets.append(widget)

    def place_widgets(self):
        for i, w in enumerate(self._widgets):
            w.position = (self._x + int(self.width/self._cols)*i, self._y + 0)

    def query_max_w(self):
        pass
    def query_max_h(self):
        pass
    def query_x(self):
        pass
    def query_y(self):
        pass






class TemplateGridLayout(LayoutMethod):

    def __init__(self, name, grid, window):
        super().__init__(name, window)
        self._grid = grid
        self._window = window

    def resolve_grid(self):
        """
        Calculate the position in the grid based on the multitline grid layout given to the layouter.
        Converts Multiline Description String into ComponentPlaceholder objects containing the dimensions and coordinates of the widget that should be placed there.
        :return: list[[ComponentPlaceholder]]
        """
        def estimate_relative_position(window, parsed_grid: list[list[ComponentPlaceholder]]):
            term_height, term_width = window.getmaxyx()
            # handle empty layout
            if parsed_grid == []:
                raise EmptyLayoutException("Layout cannot be empty.")
            # performance case for single item grid
            if len(parsed_grid) == 1:
                if len(parsed_grid[0]) == 1:
                    parsed_grid[0][0].set_width = term_width
                    parsed_grid[0][0].set_height = term_height
                    return

            # component bounding box dict
            cbb = {"r": {}}
            for y, row in enumerate(parsed_grid):
                cell: ComponentPlaceholder
                cbb["r"][y] = {}
                for x, cell in enumerate(row):
                    if x == 0:
                        cbb["r"][y][cell.type] = {"begin": x}
                        continue
                    if cell.type in cbb["r"][y]:
                        # print("found reoccuring inst of ", cell.type, "row", y, "slot", x)
                        continue
                    else:
                        cbb["r"][y][cell.type] = {"begin": x}
            print(cbb)
        # pre-formatted grid layout
        pre = [block.split(" ") for block in [" ".join(s.split()) for s in self._grid.splitlines()]]
        parsed_layout = []
        for i, entry in enumerate(pre):
            row = []
            for j, c in enumerate(entry):
                    if c==".":
                        row.append(ComponentPlaceholder(type=ComponentType.EMPTY_COMPONENT))
                    else:
                        row.append(ComponentPlaceholder(type=ComponentType.NAMED_COMPONENT, name = c))
            parsed_layout.append(row)

        estimate_relative_position(self._window, parsed_layout)
        # print(*parsed_layout, sep="\n")
        return parsed_layout
