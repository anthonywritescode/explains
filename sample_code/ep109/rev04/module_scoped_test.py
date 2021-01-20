from unittest import mock

import module_scoped


def test_inline_with_toml_present(tmpdir, capsys):
    with tmpdir.as_cwd():
        tmpdir.join('config.toml').write('[foo]\nbar = 1\n')
        module_scoped.main()

    out, err = capsys.readouterr()
    assert out == "{'foo': {'bar': 1}}\n"
    assert err == ''


def test_inline_when_toml_is_missing(tmpdir, capsys):
    with mock.patch.object(module_scoped, 'toml', None):
        with tmpdir.as_cwd():
            tmpdir.join('config.toml').write('[foo]\nbar = 1\n')
            assert module_scoped.main() == 1

    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'need to install toml to use config.toml\n'
