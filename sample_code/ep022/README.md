# [what is a tty? (beginner - intermediate)](https://youtu.be/SYwbEcNrcjI)

Today I explain what is meant by a "tty" in programming.  I use python's sys.std___.isatty() to show some examples as well.

## Interactive examples

### Bash

```bash
echo hi
/bin/echo hi

python t.py > /dev/null
# or under Windows PowerShell
# python t.py > $null

python t.py > foo
cat foo

python t.py > foo 2> foo2
cat foo
cat foo2

python t.py | cat
python t.py |& cat

echo 'someone else' | python t.py
```
