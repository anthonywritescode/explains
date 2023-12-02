# [pesky reDOS and python 3.11 (intermediate)](https://youtu.be/ECbls57_3jE)

Today we talk about an all-too-common problem with regular expressions: reDOS!  we also show a few ways to solve this with some nifty regex features

## Interactive examples

### Python

```python
import re
reg = re.compile('^hello (a|b+)+ world$')
reg.match('hello ababbbaba world')
reg.match('hello ababbbaba')

reg.match('hello ' + 'b' * 1024)
reg.match('hello ' + 'b' * 100)

reg.match('hello ' + 'b' * 20)
reg.match('hello ' + 'b' * 50)
reg.match('hello ' + 'b' * 50 + ' world')

reg = re.compile('^hello (a|(?>b+))+ world$')
reg.match('hello ' + 'b' * 50)
reg.match('hello ' + 'b' * 500)
reg.match('hello ' + 'b' * 5000)
reg.match('hello ' + 'b' * 500 + ' world')

reg = re.compile('^hello (a|b++)+ world$')
reg.match('hello ' + 'b' * 500)

reg = re.compile('^hello (a|(?=(?P<p1>b+))(?P=p1))+ world$')
reg.match('hello ' + 'b' * 500)
reg.match('hello ' + 'b' * 500 + ' world')
```

### Bash

```bash
python3.11
```
