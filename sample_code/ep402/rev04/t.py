
dct = {v: v for v in range(10)}
print(f'{dct=}')

for k, v in dct.items():
    if k == 2:
        del dct[k]

print(f'{dct=}')
