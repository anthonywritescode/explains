# [makefile basics (beginner - intermediate)](https://youtu.be/20GC9mYoFGs)

Today I go over the basics of makefiles, how to use them as a build system, and what `.PHONY` is.

## Interactive examples

### Bash

```bash
make --version

babi main.c
babi lib.h
babi lib.c

tail -n999 *

babi Makefile

make main.o
make main.o

make
./main

make clean

make
./main

make clean all
make --help
make -j8
```
