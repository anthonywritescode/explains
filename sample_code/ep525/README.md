# [all string syntaxes (beginner)](https://youtu.be/4Y4VrKa1lVs)

I've been recently teaching juice some python (over on the vods channel - @anthonywritescode-vods) and decided to record this into a standalone video!

## Interactive examples

### Python

```python
'foo'
"foo"

"foo'bar"
'foo"bar'

'foo' == "foo"

'''foo'''
"""foo"""

"""foo""" == "foo"
"""foo""" == 'foo'

'''
   hello
    hello
   world
'''

'''hello
hello
world
'''

'''\
hello
hello
'''

x = '''\
    hello
    hello
'''

print(x)

import textwrap
print(textwrap.dedent(x))

x = '''\
    hello
        hello
    hello
'''
print(textwrap.dedent(x))

print('x\ty')
print('x\ny')

print('asdfasdf\'asdfasdf')
print("asdfasdf'asdfasdf")
print("asdfasdf'asd\"fasdf")
print("""asdfasdf'asd"fasdf""")

print('hello\r\nworld')
print('hello\rha')
print('hello\aworld')
print('hello\ba')
print('hello\fa')
print('hell\fa')
print('hell\va')

print('\33[44mHELLO\033[m')
print('\33[44mHELLO\33[m')
print('\033[44mHELLO\033[m')

'\033'

print('\x1b[44mHELLO\x1b[m')

'\xb6'
'\xb1'
'\xb2'
'\xb3'
'\xb4'
'\xb5'

'\u2603'
'\U00002603'
'\U0001f643'
'\N{SNOWMAN}'
'\N{UPSIDE-DOWN FACE}'

'🙃'
'asdfasf🙃asdfasdf'

'\
asdf'

'''\
asdf
'''

r'asdfasdf'
r'asd\fasdf'

'asd\fasdf'
print('asd\fasdf')
print(r'asd\fasdf')
print('asd\\fasdf')

r'''\
hello
hello
'''

print('\.')
print('\.\tasdf')
print(r'\.\tasdf')
print('\\.\tasdf')

r'\'
'\\'
print('\\')

f'foo'
thing = 'world'
print(f'hello hello {thing}')
print(f'hello hello {(5 + 5)}')
print(f'hello hello {x:=5}')
print(f'hello hello {(x:=5)}')
print(f'hello hello {thing=}')
print(f'hello hello {5+5=}')

repr('hello')
print(f'hello hello {thing!r}')
print(f'hello hello {repr(thing)}')

x = 123.123123123
print(f'hello hello {x:.2f}')
print(f'hello hello {x:.2f} {}')
print(f'hello hello {x:.2f} {{}}')
print(f'hello hello {x:.2f} {x} {x} {{}}')

b'foo'
fr'hello hello \. {x:.2f}'
rf'hello hello \. {x:.2f}'
```

### Bash

```bash
python
python -Werror
```
