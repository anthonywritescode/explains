# [useful interview datastructures: Counter (beginner - intermediate)](https://youtu.be/FzlJxKRPL-4)

Today I talk about collections.Counter and how it might help you implement some interview questions!

## Interactive examples

### Python

```python
from collections import Counter

c = Counter()

c
c['a'] += 1
c
dir(c)
c.update(('a', 'b'))
c

import collections
counter2 = collections.defaultdict(int)
c.most_common(1)
c.most_common(2)
c.most_common()
c.update({'a': 4, 'b': 5})
c
c.update(('a', 'a', 'b'))
c
c.update('asdfasdfasdf')
c
Counter('aasdfasdfasdf')
Counter(['aasdfasdfasdf', 'a', 'a'])

set('foo')
set('of')
set('foo'), set('ffo')

sorted('table') == sorted('bleat')
Counter('table')
Counter('bleat')
Counter('table') == Counter('bleat')
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install pytest

pytest t.py
pytest t.py -v
```
