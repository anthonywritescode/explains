from __future__ import annotations

import curses


def c_main(stdscr: curses._CursesWindow) -> int:
    stdscr.addstr('hello world')
    stdscr.get_wch()
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
