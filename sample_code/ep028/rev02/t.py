import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    while True:
        # rendering phase
        ...
        char = stdscr.get_wch()
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
