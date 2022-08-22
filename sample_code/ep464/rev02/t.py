import contextlib
# from contextlib import nullcontext as did_not_raise

import math

import pytest


did_not_raise = contextlib.nullcontext


def f(x: float) -> float:
    return math.sqrt(x)


@pytest.mark.parametrize(
    ('input_val', 'cm'),
    (
        (-5, pytest.raises(ValueError)),
        (1, did_not_raise()),
    ),
)
def test_f_errors(input_val, cm):
    with cm:
        f(input_val)


def g():
    cond = ...
    if cond:
        cm = contextlib.nullcontext()
    else:
        cm = open('/dev/null')

    with cm as f:
        ...

    with contextlib.ExitStack() as ctx:
        if not cond:
            f = ctx.enter_context(open('/dev/null'))
            print(f)
