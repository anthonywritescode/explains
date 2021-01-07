import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    name = ''
    while True:
        stdscr.addstr(0, 0, 'what is your name? ')
        stdscr.addstr(name)
        char = stdscr.get_wch()
        raise AssertionError(char)
        break
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
