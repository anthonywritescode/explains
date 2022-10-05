

def print_age(i: int) -> None:
    if i >= 0:  # pragma: no branch
        print(f'hello, your age is {i}')
    #     print('you are not of age yet')
    # else:


def test_print_age(capsys):
    print_age(2)

    out, err = capsys.readouterr()
    assert out == 'hello, your age is 2\n'
    assert err == ''
