# [the python @property decorator (beginner - intermediate)](https://youtu.be/orp6bhe4i00)

In this video I explain how python implements getters and setters as well as an example where you might use them!  As a bonus I also show `@cached_property`

## Interactive examples

### Python

```python
Location
loc = Location()
loc.move_left()
loc.x
loc.y

loc
repr(loc)

Location()
Location(x=0, y=0)
loc = Location()
loc.move_left()
loc.x
loc.y
loc.loc

loc = Location()
loc.move_left()
loc.x, loc.y
loc.loc

loc.x, loc.y = (4, 3)
loc.loc

loc = Location()
loc.loc = [1000, 50]
loc

loc = Location()
loc.move_up()
loc.move_right()
loc
del loc.loc
loc

loc = Location()
loc.loc
loc.loc
del loc.loc
loc.loc
loc.loc
```

### Bash

```bash
python -i t.py
```
