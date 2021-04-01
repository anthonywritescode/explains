# [python: shlex module (beginner - intermediate)](https://youtu.be/fdTHXq6AQ7E)

Today I talk about the shlex module -- "shell lexing" -- and how it can be useful to parse / unparse unix command lines

## Interactive examples

### Python

```python
'"foo" a b c'.split()
'"foo" "a b" c'.split()

import shlex
shlex.split('"foo" "a b" c')

print(shlex.join(('foo', 'a b', 'c')))
print(shlex.join(('foo', "a' b", 'c')))

def my_shlex_join(params):
    return ' '.join(shlex.quote(arg) for arg in params)

print(my_shlex_join(('foo', "a' b", 'c')))

import pipes
pipes.quote

"echo :'("
print(shlex.quote("echo :'("))
print(shlex.join(('sh', '-c', "echo :'(")))
print(shlex.quote(shlex.join(('sh', '-c', "echo :'("))))
```

### Bash

```bash
echo "foo"'bar'

python -c 'import sys; print(sys.argv[1:])' "foo"'bar'
python -c 'import sys; print(sys.argv[1:])' "foo" 'bar'
python -c 'import sys; print(sys.argv[1:])' "foo"'"'"bar"
python -c 'import sys; print(sys.argv[1:])' "foo"'"'"bar" a b c
python -c 'import sys; print(sys.argv[1:])' "foo"'"'"bar" 'a b' c
```
