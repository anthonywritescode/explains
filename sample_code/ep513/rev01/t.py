def swap(x: int, y: int) -> tuple[int, int]:
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y


x = 2
y = 3

# x, y = y, x

print(x, y)
x, y = swap(x, y)
print(x, y)
