#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses
from dataclasses import dataclass
from enum import Enum


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


class LayoutMethod:

    def __init__(self, name):
        self._name = self.name()

    @classmethod
    def name(cls):
        return cls.__name__

class GridLayout(LayoutMethod):

    def __init__(self, name, grid, window):
        super().__init__(name)
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
            component_bb = {}
            for y, row in enumerate(parsed_grid):
                cell: ComponentPlaceholder
                for x, cell in enumerate(row):
                    if cell.type == ComponentType.NAMED_COMPONENT:
                        current_comp = cell.name
                        if y not in component_bb:
                            component_bb[y] = {current_comp}
                            # component_bb[y]["begin"] = x
            print(component_bb)
            #print(f"Height {term_height} Width {term_width}")

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
