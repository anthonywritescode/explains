from __future__ import annotations

import curses


def c_main(stdscr: curses._CursesWindow) -> int:
    stdscr.addstr('hello hello world')

    while True:
        c = stdscr.get_wch()
        if c == 'q':
            return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
