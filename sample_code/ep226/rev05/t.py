from __future__ import unicode_literals


def do_thing(s):
    if not isinstance(s, str):
        raise TypeError(s)

    print(s)


s = str('foo')  # python2: unicode -> str, python3: str -> str (noop)
do_thing(s)
