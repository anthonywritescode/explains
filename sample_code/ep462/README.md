# [what is a natural sort? (beginner - intermediate)](https://youtu.be/RaE66ycBRE0)

Today I talk about natural sorts!  what they are, and how you can implement one in python!

## Interactive examples

### Python

```python
lst = [str(i) for i in range(100)]
lst

lst.sort()
lst

lst2 = '''\
1_foo.txt
2_foo.txt
3_foo.txt
4_foo.txt
5_foo.txt
6_foo.txt
7_foo.txt
8_foo.txt
9_foo.txt
10_foo.txt
300_foo.txt
'''.splitlines()
lst2

lst2.sort()
lst2

import re

num = re.compile('([0-9]+)')
num2 = re.compile('[0-9]+')

num.split('300_foo.txt')
num2.split('300_foo.txt')

num2 = re.compile('(([0-9]+))')
num2.split('300_foo.txt')


def natural_key(s: str) -> list[int | str]:
    return [int(part) if part.isdigit() else part for part in num.split(s)]


natural_key('1_2_30_b')
natural_key('asdfasdf1_2_30_b')

'asdfasdf' < 123

lst2
lst2.sort(key=natural_key)

lst2.append('0300_foo.txt')
lst2

lst2.sort(key=natural_key)
lst2

lst2.sort(key=lambda s: (natural_key(s), s))
lst2

lst2.sort(key=lambda s: (natural_key(s), s), reverse=True)
lst2.sort(key=lambda s: (natural_key(s), s))
lst2

lst2.append('10_FOO1.txt')
lst2

lst2.sort(key=lambda s: (natural_key(s), s))
lst2

lst2.sort(key=lambda s: (natural_key(s.lower()), s.lower(), s))
lst2
```

### Bash

```bash
touch 1_foo.txt

seq 1 10
seq 1 10 | xargs --replace touch {}_foo.txt

ls
ls | cat
ls | sort
ls | sort -n

touch 300_foo.txt

ls | sort
ls | sort -n

python
```
