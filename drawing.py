__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses, _curses
from curses.textpad import rectangle
from enum import Enum

class Chars(Enum):
    BLACK_RECT = "█",
    UPPER_HALF = "▀"

class Drawing:

    @classmethod
    def draw_text_label(cls, ctx: curses.window, y, x, text: str):
        ctx.addstr(y, x, text)

    @classmethod
    def draw_box(cls, ctx: curses.window, y1, x1, y2, x2):
        rectangle(ctx, y1, x1, y2, x2)

    @classmethod
    def draw_filled_box(cls, ctx: curses.window, y1, x1, y2, x2):
        pass

    @classmethod
    def h_line_staggered(cls, ctx: curses.window, y, x, len, dots_per_cell):
        for i in range(len):
            if i%dots_per_cell == 0:
                ctx.addch(y, x + i, curses.ACS_BTEE)
                cls.draw_text_label(ctx, y + 1, x + i, str(i))
            else:
                ctx.addch(y, x + i, curses.ACS_HLINE)

    @classmethod
    def v_line_staggered(cls, ctx: curses.window, y, x, len, dots_per_cell):
        for i in range(len):
            if i%dots_per_cell == 0:
                ctx.addch(y-i, x, curses.ACS_LTEE)
                cls.draw_text_label(ctx, y - i, x + 1, str(i))
            else:
                ctx.addch(y-i, x, curses.ACS_VLINE)

    @classmethod
    def block_h_line(cls, ctx, y, x, len):
        bchar = "█"
        for i in range(len):
            ctx.addch(y, x+i, bchar)

    @classmethod
    def block_v_line(cls, ctx, y, x, len):
        bchar = "█"
        for i in range(len):
            ctx.addch(y-i, x, bchar)
