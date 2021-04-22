from __future__ import annotations

import curses


def c_main(stdscr: curses._CursesWindow) -> int:
    curses.mousemask(-1)
    curses.mouseinterval(0)

    pressed = False
    x, y = 0, 0

    stdscr.addstr('hello hello world')

    while True:
        stdscr.erase()
        stdscr.addstr('click anywhere!')
        if pressed:
            for y in range(y - 1, y + 2):
                stdscr.addstr(y, x - 1, 'XXX')

        c = stdscr.get_wch()
        if c == 'q':
            return 0
        elif c == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_PRESSED:
                pressed = True
            elif bstate & curses.BUTTON1_RELEASED:
                pressed = False
        else:
            raise AssertionError(c)


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
