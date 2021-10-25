# [bash shortcut: curly expansion (intermediate)](https://youtu.be/r2G0rbm7XJk)

Today I show a trick that I use a lot on stream with bash -- especially to move / backup files!

## Interactive examples

### Bash

```bash
echo {foo,bar}
echo prefix{foo,bar}suffix

babi t.py
cp t.py t.py.bak
cp t.py{,.bak}
ls
tail -n999 *

echo hello{a,b}{c,d}
echo hello{a,b}{c,d}{e,f}
echo hello{a,b}{e,f,g,h}
```
