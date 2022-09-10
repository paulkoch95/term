#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

from dataclasses import dataclass
from enum import Enum


class ComponentType(Enum):
    EMPTY_COMPONENT = 0,
    NAMED_COMPONENT = 1


@dataclass
class ComponentPlaceholder:
    type: ComponentType
    name: str = ""

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

    def __init__(self, name, grid):
        super().__init__(name)
        self._grid = grid

    def resolve_grid(self):
        # pre-formatted grid layout
        pre = [block.split(" ") for block in [" ".join(s.split()) for s in self._grid.splitlines()]]
        parsed_layout = []
        for i, entry in enumerate(pre):
            row = []
            for j, c in enumerate(entry):
                    if c==".":
                        row.append(ComponentPlaceholder(type=ComponentType.EMPTY_COMPONENT))
                    else:
                        row.append(ComponentPlaceholder(type=ComponentType.NAMED_COMPONENT))
            parsed_layout.append(row)

        print(*parsed_layout, sep="\n")

        return parsed_layout
