from __future__ import annotations

import curses
import random


def _recolor() -> None:
    curses.init_pair(1, random.randrange(0, curses.COLORS), 16)


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.start_color()
    curses.use_default_colors()

    curses.curs_set(0)

    _recolor()
    stdscr.bkgd(' ', curses.color_pair(1))

    stdscr.addstr('hello world')
    stdscr.get_wch()
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
