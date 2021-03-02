# [python deque (useful interview datastructures) (intermediate)](https://youtu.be/obXt90bzgJo)

Today we talk about deque and all the useful methods it has!

## Interactive examples

### Python

```python
import collections

collections.deque
d = collections.deque()
d

d = collections.deque((1, 2, 3))
d
d.pop()

l = [1, 2, 3]
l.pop()
l
d
d.popleft()

my_queue = collections.deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.popleft()

lst = []
lst.append(1)
lst.append(2)
lst.append(3)
lst

lst.pop()
lst.pop()
lst.pop()

d
d.appendleft(4)
d

def peek(d):
    item = d.popleft()
    d.appendleft(item)
    return item

peek(d)
d

for x in d:
    print(x)

for x in reversed(d):
    print(x)

d[1]
d[-1]
d[0]

d.extend((1, 2, 3, 4))
d
d[4]
d[2:]

import itertools
itertools.islice(d, 4)
collections.deque(itertools.islice(d, 4))

d
d.rotate(3)
d
d.rotate()
d

bounded_deque = collections.deque(maxlen=3)
bounded_deque.append(1)
bounded_deque.append(2)
bounded_deque.append(3)
bounded_deque

bounded_deque.append(4)
bounded_deque

d
d.reverse()
d
```
