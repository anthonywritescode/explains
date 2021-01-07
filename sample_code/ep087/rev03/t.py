import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    if curses.has_colors():
        curses.use_default_colors()

    stdscr.insstr(5, 0, f'COLORS: {curses.COLORS}')
    stdscr.insstr(6, 0, f'COLOR_PAIRS: {curses.COLOR_PAIRS}')

    name = ''
    name_done = False
    while True:
        stdscr.addstr(0, 0, 'what is your name? ')
        stdscr.clrtoeol()
        stdscr.addstr(' ')
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1, 0, f'OHAI {name}!')

        char = stdscr.get_wch()
        if name_done:
            return 0
        elif isinstance(char, str) and char.isprintable():
            name += char
        elif char == curses.KEY_BACKSPACE or char == '\x7f':  # char == '\x97'
            name = name[:-1]
        elif char == '\n':
            name_done = True
        else:
            raise AssertionError(char)


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    exit(main())
