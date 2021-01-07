import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    while True:
        # stdscr.insstr(0, 0, 'hello world')
        # stdscr.move(0, len('hello world') + 1)
        stdscr.addstr(0, 0, 'x' * 80)
        char = stdscr.get_wch()
        break
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
