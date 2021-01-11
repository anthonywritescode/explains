from __future__ import annotations

import argparse
import curses


def c_main(stdscr: curses._CursesWindow, tabsize: int) -> int:
    curses.set_tabsize(tabsize)

    stdscr.addstr(0, 0, 'this next line is indented with one tab!')
    stdscr.addstr(1, 0, '\tINDENTED!')
    stdscr.get_wch()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--tabsize', default=8, type=int)
    args = parser.parse_args()
    return curses.wrapper(c_main, args.tabsize)


if __name__ == '__main__':
    exit(main())
