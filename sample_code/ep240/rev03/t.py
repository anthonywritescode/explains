x = 2

# assert x == 1
#
# # ==>
#
# if not (x == 1):
#     raise AssertionError


assert x == 1, f'expected 1 but got {x=}'

# ==>

if not (x == 1):
    raise AssertionError(f'expected 1 but got {x=}')
