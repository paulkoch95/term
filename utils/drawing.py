__author__ = "Paul Koch"
__email__ = "paulkoch95(at)gmail.com"
__status__ = "development"

import curses, _curses
from curses.textpad import rectangle
from enum import Enum


class Chars(Enum):
    BLACK_RECT = "█",
    UPPER_HALF = "▀"

class CONNECTION_DIR(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Drawing:

    @classmethod
    def draw_text_label(cls, ctx: curses.window, y, x, text: str):
        ctx.addstr(y, x, text, )  # curses.color_pair(1))

    # curses.color_pair(1))
    @classmethod
    def draw_box(cls, ctx: curses.window, y1, x1, y2, x2):
        rectangle(ctx, y1, x1, y2, x2)

    @classmethod
    def draw_grid(cls, ctx: curses.window, y, x, cols, rows, cell_width, cell_height):
        for column in range(cols):
            for row in range(rows):
                # ctx.addch(y+(column*cell_height),x+(row*cell_width),curses.ACS_PLUS)
                uly, ulx = y+(column*cell_height), x+(row*cell_width)
                lry, lrx = y+(column*cell_height)+cell_height, x+(row*cell_width)+cell_width
                ctx.vline(uly + 1, ulx, curses.ACS_VLINE, lry - uly - 1)
                ctx.hline(uly, ulx + 1, curses.ACS_HLINE, lrx - ulx - 1)
                ctx.hline(lry, ulx + 1, curses.ACS_HLINE, lrx - ulx - 1)
                ctx.vline(uly + 1, lrx, curses.ACS_VLINE, lry - uly - 1)
                # rectangle(ctx, y+(column*cell_height), x+(row*cell_width),  y+(column*cell_height)+cell_height, x+(row*cell_width)+cell_width)

    @classmethod
    def debug_marker(cls, ctx: curses.window, y, x):
        ctx.addch(y, x, curses.ACS_DIAMOND)

    @classmethod
    def draw_hollow_box(cls, ctx: curses.window, y, x, y2, x2):
        """
        This is preliminary method. Will be replaced by "tight box" drawing algorithm.
        """
        rectangle(ctx, y, x, y2, x2)

    @classmethod
    def draw_filled_box(cls, ctx: curses.window, y1, x1, y2, x2):
        pass

    @classmethod
    def h_line_staggered(cls, ctx: curses.window, y, x, len, dots_per_cell):
        data_points = []
        intervall = len/dots_per_cell
        for i in range(len):
            if i % intervall == 0:
                ctx.addch(y, x + i, curses.ACS_BTEE)
                cls.draw_text_label(ctx, y + 1, x + i, str(i//intervall))
                data_points.append(i)
            else:
                ctx.addch(y, x + i, curses.ACS_HLINE)
        return data_points

    @classmethod
    def v_line_staggered(cls, ctx: curses.window, y, x, len, dots_per_cell):
        for i in range(len+1):
            if i % dots_per_cell == 0:
                ctx.addch(y - i, x, curses.ACS_LTEE)
                cls.draw_text_label(ctx, y - i, x + 1, str(i))
            else:
                ctx.addch(y - i, x, curses.ACS_VLINE)

    @classmethod
    def block_h_line(cls, ctx, y: int, x: int, len: int):
        bchar = "█"
        for i in range(len):
            ctx.addch(y, x + i, bchar)

    @classmethod
    def block_v_line(cls, ctx, y: int, x: int, len: int):
        bchar = "█"
        for i in range(len):
            ctx.addch(y - i, x, bchar)
