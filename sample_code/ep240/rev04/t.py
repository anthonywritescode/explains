x = 2

# assert x == 1
#
# # ==>
#
# if not (x == 1):
#     raise AssertionError


def test():
    assert x == 1
    assert x == 1, f'expected 1 but got {x=}'
