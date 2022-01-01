# [what is PROMPT\_COMMAND? (+aactivator) (intermediate)](https://youtu.be/GFLivv2QGI0)

Today I show prompt command and how I use it to auto-activate virtual environment

## Interactive examples

### Bash

```bash
echo $PROMPT_COMMAND
PROMPT_COMMAND='echo hi'
echo wat

unset PROMPT_COMMAND

# https://github.com/Yelp/aactivator
aactivator init

eval "$(aactivator init)"
echo $PROMPT_COMMAND

# git clone https://github.com/anthonywritescode/aoc2021
git clone git@github.com:anthonywritescode/aoc2021
cd aoc2021/
ls .activate.sh .deactivate.sh
ls .activate.sh .deactivate.sh -al

virtualenv venv
cd ..
cd aoc2021/
```
