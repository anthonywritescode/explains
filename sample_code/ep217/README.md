# [unix commands: fold (beginner)](https://youtu.be/BVuW-kiY_X8)

Today I talk about the `fold` command and how it can be used to wrap lines!

## Interactive examples

### Bash

```bash
python -c "print(('hello hello ' * 10 + 'world\n') * 30)"
python -c "print(('hello hello ' * 10 + 'world\n') * 30)" | less
man fold

python -c "print(('hello hello ' * 10 + 'world\n') * 30)" | fold -w 40
python -c "print(('hello hello ' * 10 + 'world\n') * 30)" | fold -w 40 --spaces
python -c "print(('hello hello ' * 10 + 'world\n') * 30)" | fold -w80 | less
python -c "print(('hello hello ' * 10 + 'world\n') * 30)" | fold -w40 | less
```
