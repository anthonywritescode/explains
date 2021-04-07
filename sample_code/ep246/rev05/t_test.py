from t import hello


def test_hello(capfd):
    hello('anthony')
    stdout, stderr = capfd.readouterr()
    hello('daniel')
    stdout, stderr = capfd.readouterr()
    assert stdout == 'hello hello daniel\n'
