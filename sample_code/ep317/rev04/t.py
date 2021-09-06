import os
from unittest import mock


def greet() -> None:
    username = os.environ['USER']  # probably use getpass.getuser() instead
    print(f'hello hello, {username}')


def main() -> int:
    greet()
    return 0


def test_greet(capsys):
    with mock.patch.dict(os.environ, {'USER': 'nobody3'}):
        greet()

    out, err = capsys.readouterr()
    assert out == 'hello hello, nobody3\n'


if __name__ == '__main__':
    raise SystemExit(main())
