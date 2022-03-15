from __future__ import annotations

import curses
import random


GREEN_PAIR = 1
YELLOW_PAIR = 2


def color_word(word: str, guess: str):
    ret = []

    letters = list(word)
    for i, (c1, c2) in enumerate(zip(word, guess)):
        if c1 == c2:
            ret.append((GREEN_PAIR, i))
            letters.remove(c1)

    for i, (c1, c2) in enumerate(zip(word, guess)):
        if c1 != c2 and c2 in letters:
            ret.append((YELLOW_PAIR, i))
            letters.remove(c2)

    return ret


def c_main(stdscr: curses._CursesWindow) -> int:
    with open('wordlist') as f:
        wordlist = f.read().splitlines()

    curses.init_pair(GREEN_PAIR, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(YELLOW_PAIR, curses.COLOR_BLACK, curses.COLOR_YELLOW)

    word = random.choice(wordlist)
    past_guesses = ['hello', 'world']

    while True:
        # DONTSHIP
        stdscr.addstr(0, 0, word)

        line = 1
        for past_guess in past_guesses:
            stdscr.addstr(line, 1, ' '.join(past_guess))

            try:
                for pair, pos in color_word(word, past_guess):
                    stdscr.chgat(line, 1 + 2 * pos, 1, curses.color_pair(pair))
            except Exception:
                raise AssertionError(word, past_guess)

            line += 2

        # 1. render everything

        # 2. input character

        char = stdscr.get_wch()
        if char == 'q':
            return 0

    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
