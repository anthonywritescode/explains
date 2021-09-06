import os


def greet() -> None:
    username = os.environ['USER']  # probably use getpass.getuser() instead
    print(f'hello hello, {username}')


def main() -> int:
    greet()
    return 0


def test_greet(capsys):
    greet()
    out, err = capsys.readouterr()
    assert out == 'hello hello, asottile\n'


if __name__ == '__main__':
    raise SystemExit(main())
