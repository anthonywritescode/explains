import sys
from unittest import mock

import inline


def test_inline_with_toml_present(tmpdir, capsys):
    with tmpdir.as_cwd():
        tmpdir.join('config.toml').write('[foo]\nbar = 1\n')
        inline.main()

    out, err = capsys.readouterr()
    assert out == "{'foo': {'bar': 1}}\n"
    assert err == ''


def test_inline_when_toml_is_missing(tmpdir, capsys):
    with mock.patch.dict(sys.modules, {'toml': None}):
        with tmpdir.as_cwd():
            tmpdir.join('config.toml').write('[foo]\nbar = 1\n')
            assert inline.main() == 1

    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'need to install toml to use config.toml\n'
