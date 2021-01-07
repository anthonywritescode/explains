import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    name = ''
    name_done = False
    while True:
        stdscr.addstr(0, 0, 'what is your name? ')
        stdscr.clrtoeol()
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1, 0, f'OHAI {name}!')

        char = stdscr.get_wch()
        if isinstance(char, str) and char.isprintable():
            name += char
        elif char == curses.KEY_BACKSPACE or char == '\x08':  # char == '\x97'
            name = name[:-1]
        elif char == '\n':
            name_done = True
        else:
            raise AssertionError(char)
    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
