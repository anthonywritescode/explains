

k = 1


def test_k():
    assert k == 1


def test_k2():
    global k

    k = 2
    assert k == 2
