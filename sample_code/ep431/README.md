# [babi+ast helped me not break sentry! (intermediate)](https://youtu.be/Fch_lt7ZXUw)

Today I show off a cool workflow I used with my text editor and an ast parser and how I used it to do a code audit!

## Interactive examples

### Bash

```bash
git clone git@github.com:getsentry/sentry --depth=1
cd sentry/

git ls-files -- '*.py' | xargs python t.py

virtualenv venv
. venv/bin/activate
pip install astpretty

astpretty /dev/stdin <<< 'a(default=None)'
astpretty /dev/stdin <<< 'a(default=None, **kw)'

git grep -l click -- '*.py' | xargs python t.py

babi +395 src/sentry/runner/commands/run.py
babi +395 src/sentry/runner/commands/run.py +440 src/sentry/runner/commands/run.py

babi $(git grep -l click -- '*.py' | xargs python t.py)
vim $(git grep -l click -- '*.py' | xargs python t.py)
\nano $(git grep -l click -- '*.py' | xargs python t.py)
```
