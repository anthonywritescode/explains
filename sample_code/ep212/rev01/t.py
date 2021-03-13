

def dct_eq(first, second):
    # for k1, k2 in itertools.zip_longest(first, second):
    #     if k1 != k2:
    #         return False
    # return first == second
    return tuple(first) == tuple(second) and first == second


def dct_popitem(dct, *, last: bool = True):
    if last:
        it = iter(reversed(dct))
    else:
        it = iter(dct)

    key = next(it)
    return key, dct.pop(key)


def dct_move_to_end(dct, key):
    dct[key] = dct.pop(key)
