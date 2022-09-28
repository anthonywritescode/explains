# [a python curses wordle clone from scratch! (intermediate - advanced)](https://youtu.be/dViRI1iovoc)

Today I build a working "wordle" clone in python with curses!

## Interactive examples

### Notes

```text
- 5 letter words
- 6 guesses
- green for correct guess
- yellow for correct but wrong position
- repeats aren't additionally yellow

  A A A A A

INPUT GUESS
> a a a a a (not in wordlist, press enter to confirm)

```

### Bash

```bash
ls /usr/share/dict/american-english
grep -E '^[a-z]{5}$' /usr/share/dict/american-english
LANG=C grep -E '^[a-z]{5}$' /usr/share/dict/american-english
LANG=C grep -E '^[a-z]{5}$' /usr/share/dict/american-english | shuf > wordlist
less wordlist

virtualenv venv
. venv/bin/activate
pip install pytest

pytest test_t.py
python -m t
```
