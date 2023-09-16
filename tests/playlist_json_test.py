import importlib.machinery
import importlib.util

import pytest

loader = importlib.machinery.SourceFileLoader('_', 'bin/playlist-json')
spec = importlib.util.spec_from_loader(loader.name, loader)
mod = importlib.util.module_from_spec(spec)
loader.exec_module(mod)


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'introducing anthony explains! -- anthony explains #000',
            'introducing anthony explains! -- #000',
            id='special case meta episode',
        ),
        pytest.param(
            'python @decorators - (intermediate) anthony explains #002',
            'python @decorators - (intermediate) #002',
            id='normal explains episode',
        ),
        pytest.param(
            '(stream faq) what is your operating system? why?',
            'what is your operating system? why?',
            id='stream faq at beginning',
        ),
        pytest.param(
            'Good code changed like a ghost! (stream faq)',
            'Good code changed like a ghost!',
            id='stream faq at end',
        ),
    ),
)
def test_fixup_title(s, expected):
    assert mod._fixup_title(s) == expected
