import hello


def test_main(capsys):
    hello.main(['Anthony'])

    out, err = capsys.readouterr()
    assert out == 'Hello Sexy Person Anthony\n'
    assert err == ''
