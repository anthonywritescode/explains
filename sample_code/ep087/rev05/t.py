import curses


def c_main(stdscr: 'curses._CursesWindow') -> int:
    if curses.has_colors():
        curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(2, 84, 232)

        if curses.can_change_color():
            # curses.init_color(color_num, r, g, b)
            # 0x1e, 0x77, 0xd3
            curses.init_color(
                255,
                0x1e * 1000 // 0xff,
                0x77 * 1000 // 0xff,
                0xd3 * 1000 // 0xff,
            )

            curses.init_pair(3, 255, -1)

    stdscr.insstr(5, 0, f'COLORS: {curses.COLORS}')
    stdscr.insstr(6, 0, f'COLOR_PAIRS: {curses.COLOR_PAIRS}')

    name = ''
    name_done = False
    while True:
        stdscr.addstr(0, 0, 'what is your name? ', curses.color_pair(1))
        stdscr.clrtoeol()
        stdscr.addstr(' ')
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1, 0, f'OHAI {name}!', curses.color_pair(3))

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
