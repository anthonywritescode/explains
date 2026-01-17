# [bash quoting is really not that difficult! (beginner - intermediate)](https://youtu.be/VIUoHnFwEH4)

I show the small number of rules to bash quoting and why '"'"' shouldn't be that scary!

## Interactive examples

### Python

```python
import shlex
print(shlex.quote("hello ' world"))
print(shlex.quote(shlex.quote("hello ' world")))
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

echo 'hello ' "hello world"

echo 'hello '"hello world"
echo 'hello ''hello world'

echo 'hello ' "'" ' world'
echo 'hello '"'"' world'

echo 'hello '\'' world'

echo "hello "'"'" world"

echo ''"'"'hello '"'"'"'"'"'"'"'"' world'"'"''
echo "'"'hello '"'"'"'"'"'"'"'"' world'"'"

echo `echo hi`

echo "$(echo hi)"
echo "$(echo "$(echo hello "$USER")")"
```
