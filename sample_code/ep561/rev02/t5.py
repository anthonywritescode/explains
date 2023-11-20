import functools
from typing import Callable


def g[R, **P](f: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(f)
    def g_impl(*args: P.args, **kwargs: P.kwargs) -> R:
        return f(*args, *kwargs)
    return g_impl
