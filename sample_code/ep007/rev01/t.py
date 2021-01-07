import os
from typing import NoReturn


def g() -> NoReturn:
    ...


def always_raises() -> NoReturn:
    raise AssertionError('why did you call me?')


def calls_exec() -> NoReturn:
    os.execvp('echo', ('echo', 'hi'))


def get_request():
    ...


def handle_response(arg):
    ...


def loops_forever() -> NoReturn:
    while True:
        request = get_request()
        handle_response(request)


def calls_something_with_noreturn() -> NoReturn:
    loops_forever()


def f() -> None:
    ...


def has_no_return_statements() -> None:
    print('hello world')
    # return


def explicitly_returns_none() -> None:
    print('I return None!')
    return None
