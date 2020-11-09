import hello

import pytest


def test_main(capsys):
    hello.main(['Anthony'])

    out, err = capsys.readouterr()
    assert out == 'Hello Sexy Person Anthony\n'
    assert err == ''


def test_main_error_with_empty_string(capsys):
    with pytest.raises(SystemExit) as excinfo:
        hello.main([''])

    retv, = excinfo.value.args
    assert retv == 1

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must not be empty!\n"
