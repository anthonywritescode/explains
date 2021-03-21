from __future__ import unicode_literals


def do_thing(s):
    if not isinstance(s, str):
        raise TypeError(s)

    print(s)


s = 'foo'
do_thing(s)
