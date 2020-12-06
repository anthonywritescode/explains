# [python return annotations: NoReturn vs None (intermediate)](https://youtu.be/-zH0qqDtd4w)

Today we talk about a common stumbling block in python typing -- the `NoReturn` annotation!

## Interactive examples

### Python

```python
import dis
dis.dis(has_no_return_statements)

stack = []
stack.append(print)
stack.append('hello world')
args = [stack.pop() for _ in range(1)]
func = stack.pop()
stack.append(func(*args))
stack
stack.pop()
stack

stack.append(None)
repr(stack.pop())
```

### Bash

```bash
python -i t.py
```
