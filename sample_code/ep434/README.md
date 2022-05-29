# [top 10 new things in python 3.11 (beginner - advanced)](https://youtu.be/w2rcZIG1Uxk)

Here's my list of things that I think are worth knowing for python 3.11

## Interactive examples

### Notes

1. faster
    - I used pyperformance to show this

2. asyncio task groups
    - originally from EdgeDB

3. exception changes:
    - arrows for expressions
    - exception groups for asyncio / task groups
    - add_note for adding information

4. typing improvements
    - Self - allows methods to return the actual class
        - useful for cloning and alternative constructors
    - variadic generics: `TypeVarTuple`, `Unpack`, `*splat`
    - LiteralString: preventing sql injection, i18n
    - `Never`, `assert_never`, `assert_type`
    - `TypedDict` / `NamedTuple` can be generic

5. tomllib
    - only a parser (for now)
        - loads: only allows str
        - load: only allows bytes
    - based on `tomli`
    - `pip install tomlw` for writer

6. contextlib.chdir
    - changes working directory and back
    - intended for single threaded usage

7. re: atomic groups and possessive quantifiers
    - atomic groups: `(?> ... )`
    - possessive quantifiers: `.++` `.*+` `.?+` `.{2}+`

8. datetime: fromisoformat
    - parses more formats
    - can include timezones

9. sys.exception
    - replacement for exc_info

10. unittest: `enterContext` `enterClassContext`
    - easier setup and teardown

11. honorable mentions
    - `PYTHONSAFEPATH` (python -P)
    - `wsgireg.types`: aliases for wsgi apps
    - singledispatch: now understands `Union`

### Bash

```bash
virtualenv venv310 -ppython3.10
virtualenv venv311 -ppython3.11

./venv310/bin/pip install pyperformance
./venv311/bin/pip install pyperformance

./venv310/bin/pyperformance run -b django_template
./venv311/bin/pyperformance run -b django_template

python3.11 t.py
python3.11 t3.py
python3.11 chdir.py
python3.11 typing.py
python3.11 -m unittest t4.py
python3.11 -c 'import sys; print(sys.path)'
python3.11 -P -c 'import sys; print(sys.path)'
python3.11 -m pydoc wsgiref.types

all-repos-grep 'def chdir' -- '*.py'
all-repos-grep 'def cwd' -- '*.py'

grep -r enterContext /usr/lib/python3.11/

git clone git@github.com:python/cpython
cd cpython/

git grep enterContext
git checkout v3.11.0b1
git grep enterContext
```
