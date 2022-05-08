# [bash quoting is really not that difficult! (beginner - intermediate)](https://youtu.be/VIUoHnFwEH4)

I show the small number of rules to bash quoting and why '"'"' shouldn't be that scary!

## Interactive examples

### Python

```python
import shlex
print(shlex.quote("hello ' wolrd"))
print(shlex.quote(shlex.quote("hello ' wolrd")))
```

### Bash

```bash
echo hello world
echo 'hello world'
echo "hello world"

echo 'hello $USER world'
echo 'hello !! world'

echo "hello $USER world"
echo "hello !! world"

echo 'hello " world'
echo "hello ' world"

echo 'hello ' "hello wolrd"

echo 'hello '"hello wolrd"
echo 'hello ''hello wolrd'

echo 'hello ' "'" ' world'
echo 'hello '"'"' world'

echo 'hello '\'' world'

echo "hello "'"'" world"

echo ''"'"'hello '"'"'"'"'"'"'"'"' wolrd'"'"''
echo "'"'hello '"'"'"'"'"'"'"'"' wolrd'"'"

echo `echo hi`

echo "$(echo hi)"
echo "$(echo "$(echo hello "$USER")")"
```
