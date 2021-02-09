import subprocess
import types

import pytest


@pytest.fixture
def git_dir(tmpdir):
    d = tmpdir.join('git')
    subprocess.check_call(('git', 'init', str(d)))
    commit_cmd = ('git', '-C', str(d), 'commit', '--allow-empty', '-m', 'init')
    subprocess.check_call(commit_cmd)
    rev_cmd = ('git', 'rev-parse', 'HEAD')
    rev = subprocess.check_output(rev_cmd).strip().decode()

    yield types.SimpleNamespace(directory=d, rev=rev)


def test(git_dir):
    ...
