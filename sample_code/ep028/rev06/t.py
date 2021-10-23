import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    while True:
        # stdscr.insstr(0, 0, 'hello world')
        # stdscr.move(0, len('hello world') + 1)
        stdscr.addstr(curses.LINES - 1, 0, 'x' * 79)
        char = stdscr.get_wch()
        break
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
