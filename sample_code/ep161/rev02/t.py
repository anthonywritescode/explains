def square(x: float) -> float:
    return x * x


inputs = [
    [1, 2, 3, 4, 5],
    [6, 80],
    [999, 100, 5],
    [6, 80],
    [999, 100, 5],
]

"""\
output = []
for sub_list in inputs:
    if len(sub_list) >= 3:
        for number in sub_list:
            if number % 2 == 0:
                output.append(square(number))
"""

output = [
    square(number)
    for sub_list in inputs
    if len(sub_list) >= 3
    for number in sub_list
    if number % 2 == 0
    # if number < 100
]


print(output)
