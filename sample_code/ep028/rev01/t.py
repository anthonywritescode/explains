import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    import time; time.sleep(1)
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
