from __future__ import annotations

import curses
import random


GREEN_PAIR = 1
YELLOW_PAIR = 2
RED_PAIR = 3
CYAN_PAIR = 4

G = '🟩'
Y = '🟨'
W = '⬜'

COLOR_PAIR_TO_CHAR = {
    GREEN_PAIR: G,
    YELLOW_PAIR: Y,
}


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
    curses.init_pair(RED_PAIR, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(CYAN_PAIR, curses.COLOR_BLACK, curses.COLOR_CYAN)

    word = random.choice(wordlist)
    past_guesses = ['']
    current_word = ''
    unget = []

    while True:
        stdscr.clear()

        # DONTSHIP
        stdscr.addstr(0, 0, word)

        # print past guesses
        line = 1
        for past_guess in past_guesses:
            stdscr.addstr(line, 1, ' '.join(past_guess))

            try:
                for pair, pos in color_word(word, past_guess):
                    stdscr.chgat(line, 1 + 2 * pos, 1, curses.color_pair(pair))
            except Exception:
                raise AssertionError(word, past_guess)

            line += 2

        # if we won!
        if len(past_guesses) == 6 or past_guesses and past_guesses[-1] == word:
            for past_guess in past_guesses:
                word_chars = [W] * 5
                for pair, pos in color_word(word, past_guess):
                    word_chars[pos] = COLOR_PAIR_TO_CHAR[pair]
                stdscr.addstr(line, 0, ''.join(word_chars))
                line += 1

            line += 1

            if past_guesses[-1] == word:
                stdscr.addstr(line, 0, 'CONGRATS!')
            else:
                stdscr.addstr(line, 0, 'BETTER LUCK NEXT TIME!')

            stdscr.addstr(line + 1, 0, '(press any key to quit)')
            stdscr.get_wch()
            return 0

        stdscr.addstr(line, 1, ' '.join(current_word))

        for i in range(5):
            stdscr.chgat(line, 1 + i * 2, 1, curses.A_UNDERLINE)

        if len(current_word) == 5:
            if current_word in wordlist:
                stdscr.addstr(
                    line, 12,
                    'press enter to accept',
                    curses.color_pair(CYAN_PAIR),
                )
                ch = stdscr.get_wch()
                if ch == '\n':
                    past_guesses.append(current_word)
                    current_word = ''
                    continue
                else:
                    unget.append(ch)
            else:
                stdscr.addstr(
                    line, 12,
                    '(word not in word list!)',
                    curses.color_pair(RED_PAIR),
                )

        stdscr.move(line, 1 + len(current_word) * 2)
        if unget:
            ch = unget.pop()
        else:
            ch = stdscr.get_wch()

        if ch == curses.KEY_BACKSPACE or ord(ch) == 8 or ord(ch) == 127:
            current_word = current_word[:-1]
        elif (
            len(current_word) < 5 and
            isinstance(ch, str) and
            ch.isascii() and
            ch.isalpha()
        ):
            current_word += ch.lower()

    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == '__main__':
    raise SystemExit(main())
