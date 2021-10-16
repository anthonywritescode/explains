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
            'foo (beginner) anthony explains #123',
            'foo (beginner)',
            id='remove playlist name and number',
        ),
        pytest.param(
            'foo [special] (beginner) anthony explains #123',
            r'foo \[special\] (beginner)',
            id='escape special markdown characters',
        ),
        pytest.param(
            'foo  bar (beginner) anthony explains #123',
            'foo bar (beginner)',
            id='collapse repeated whitespace',
        ),
        pytest.param(
            'introducing anthony explains -- anthony explains #000',
            'introducing anthony explains',
            id='special case for first episode',
        ),
        pytest.param(
            'something `__main__` `[]` (intermediate) anthony explains #5',
            'something `__main__` `[]` (intermediate)',
            id='leave special characters alone inside backticks',
        ),
    ),
)
def test_fixup_title(s, expected):
    assert mod._fixup_title(s) == expected
