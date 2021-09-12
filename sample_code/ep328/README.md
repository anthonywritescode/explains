# [assign vs. shallow vs. deep copy (beginner - intermediate)](https://youtu.be/5Ufr51uPHEs)

Today I talk about referential assignment, shallow copying, and deep copying and how they're different and how to use each of them!

## Interactive examples

### Python

```python
x = [1, 2, 3]
y = x
y
x

x.append(4)
x
y

x = [[1], [2], [3]]
import copy
x.copy()

y = x.copy()
x
y

x.append([4])
x
y

x[0]
x[0].append(999)
x
y

z = copy.deepcopy(x)
x
z

x[0].append(9001)
x
z

import json
json.loads(json.dumps(x))

import pickle
pickle.loads(pickle.dumps(x))
```
