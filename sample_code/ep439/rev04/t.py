

def is_list_of_strings(lst: list[object]) -> bool:
    return all(isinstance(x, str) for x in lst)


def f(x: list[str] | list[int]) -> None:
    if is_list_of_strings(x):
        print(f'got commands {" ".join(x)}')
    else:
        print(f'got numbers: {" ".join(str(y) for y in x)}')
