from typing import Any


def f(**kwargs: dict[str, Any]): pass


# not ok f(x=1, y=2)
# ok f(x={}, y={})
