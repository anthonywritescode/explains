from __future__ import annotations

import curses


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.mousemask(-1)
    curses.mouseinterval(0)

    stdscr.addstr('hello hello world')

    while True:
        c = stdscr.get_wch()
        if c == 'q':
            return 0
        elif c == curses.KEY_MOUSE:
            stdscr.addstr(1, 0, 'mouse event')
        else:
            raise AssertionError(c)


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
