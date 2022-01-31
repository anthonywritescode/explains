# [useful interview data structures: heapq (intermediate)](https://youtu.be/sRLuocdQfEw)

Today I show another useful interview datastructure -- heapq!  I show how to use this to build a priority queue

## Interactive examples

### Python

```python
import heapq

lst = []

heapq.heappush(lst, 1)
heapq.heappush(lst, 2)
heapq.heappush(lst, 4)
heapq.heappush(lst, 10)
heapq.heappush(lst, 5)
heapq.heappush(lst, 6)

lst
heapq.heappop(lst)
lst
heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)

(1, 'foo')

lst = []
heapq.heappush(lst, (1, 'foo'))
heapq.heappush(lst, (5, 'bar'))
heapq.heappush(lst, (3, 'baz'))

heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)

from typing import NamedTuple

class QueueItem(NamedTuple):
    priority: int
    work_item: str


lst = []
heapq.heappush(lst, QueueItem(priority=1, work_item='foo'))
heapq.heappush(lst, QueueItem(priority=1, work_item='baz'))
heapq.heappush(lst, QueueItem(priority=1, work_item='womp'))

heapq.heappop(lst)
heapq.heappop(lst)
heapq.heappop(lst)
```
