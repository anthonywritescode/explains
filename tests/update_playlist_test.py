import importlib.machinery
import importlib.util

import pytest

loader = importlib.machinery.SourceFileLoader('_', 'bin/update-playlist')
spec = importlib.util.spec_from_loader(loader.name, loader)
mod = importlib.util.module_from_spec(spec)
loader.exec_module(mod)


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'foo [special] (beginner)',
            r'foo \[special\] (beginner)',
            id='escape special markdown characters',
        ),
        pytest.param(
            'something `__main__` `[]` (intermediate)',
            'something `__main__` `[]` (intermediate)',
            id='leave special characters alone inside backticks',
        ),
    ),
)
def test_escape(s, expected):
    assert mod._escape(s) == expected
