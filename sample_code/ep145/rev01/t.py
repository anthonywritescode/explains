from typing import Any

import functools
import subprocess


# check_call(cmd: Sequence[str], ... stdout: int = ..., stderr: ...

def _check_call(*cmd: str, **kwargs: Any) -> None:
    subprocess.check_call(cmd, **kwargs)


def decorator(func):
    @functools.wraps(func)
    def decorator_inner(*args: Any, **kwargs: Any) -> Any:
        ...
        ret = func(*args, **kwargs)
        ...
        return ret
    return decorator_inner


# subprocess.check_call(('echo', 'hi'))
_check_call('echo', 'hi', stdout='foo')
