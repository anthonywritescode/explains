# [the `cut` command (beginner - intermediate)](https://youtu.be/l9T85dA6HDY)

Today I talk about the `cut` command and how it can be useful in shell pipelines!

## Interactive examples

### Bash

```bash
man cut
cut input
cut -d: -f 0 input
cut -d: -f 1 input
cut -d: -f 2 input
cut -d: -f 3 input

cut -d: -f2-3 input
cut -d: -f1-2 input
cut -d: -f2- input
cut -d: -f-2 input
cut -d: -f1,3 input

all-repos-grep . -- 'requirements-*minimal.txt'
all-repos-grep . -- 'requirements-*minimal.txt' | cut -d: -f3
all-repos-grep . -- 'requirements-*minimal.txt' | cut -d: -f3 | sort | uniq
all-repos-grep . -- 'requirements-*minimal.txt' | cut -d: -f3 | sort -u
all-repos-grep . -- 'requirements-*minimal.txt' | cut -d: -f3 | sort -u | cut -d'>' -f1 | sort -u
```
