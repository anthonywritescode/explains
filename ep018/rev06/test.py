from t import average


def test_average_of_numbers():
    avg = average([1, 2, 3])
    assert avg == 3
