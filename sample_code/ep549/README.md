# [how does .exe magic work? (PATHEXT) (intermediate)](https://youtu.be/6QiLrVaG0qI)

Today we talk about how executable lookup works on windows -- the specifics of `PATHEXT` and the effects of the current working directory

## Interactive examples

### Windows CMD

```batch
echo %PATHEXT%

babi
babi.exe
where babi

echo %PATH%

babi workspace\t.py
cd workspace
t

set PATHEXT=.exe
t
t.py
```
