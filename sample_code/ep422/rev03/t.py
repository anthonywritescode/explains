from __future__ import annotations

import curses
import random
import time


def _recolor() -> None:
    curses.init_pair(1, random.randrange(0, curses.COLORS), 16)


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.start_color()
    curses.use_default_colors()

    curses.curs_set(0)

    stdscr.nodelay(True)

    _recolor()
    stdscr.bkgd(' ', curses.color_pair(1))

    s = 'hello world'

    stdscr.addstr(s)

    x = y = 0
    dx = dy = 1

    while True:
        time.sleep(.1)

        try:
            wch = stdscr.get_wch()
        except curses.error:
            pass
        else:
            if wch == curses.KEY_RESIZE:
                curses.update_lines_cols()
                x = min(curses.COLS - len(s), x)
                y = min(curses.LINES - 1, y)
            else:
                return 0

        stdscr.move(y, 0)
        stdscr.clrtoeol()

        if x == curses.COLS - len(s):
            dx = -1
            _recolor()
        elif x == 0:
            dx = 1
            _recolor()

        if y == curses.LINES - 1:
            dy = -1
            _recolor()
        elif y == 0:
            dy = 1
            _recolor()

        x += dx
        y += dy

        try:
            stdscr.addstr(y, x, s)
        except curses.error:
            pass

        stdscr.refresh()

    stdscr.get_wch()
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
