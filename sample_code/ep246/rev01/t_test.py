from t import hello


def test_hello(capsys):
    hello('anthony')
    stdout, stderr = capsys.readouterr()
    assert stdout == 'hello hello anthony\n'
