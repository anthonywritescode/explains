

def do_thing(s):
    if not isinstance(s, str):
        raise TypeError(s)

    print(s)
