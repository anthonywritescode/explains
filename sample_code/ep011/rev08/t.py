
# def str_find_char(s: str, c: str) -> int:
#     for i in range(len(s)):
#     if s[i] == c:
#         ...


def str_find_char(s: str, c: str) -> int:
    for i, s_c in enumerate(s):
        if c == s_c:
            idx = i
            break
    else:
        idx = -1

    return idx


def while_else():
    i = 0
    while i < 10:
        if i == 5:
            print('I found five!')
            break
        print(i)
        i += 1
    else:
        print('while-else ran!')


def for_else():
    for i in range(10):
        if i == 5:
            print('I found five!')
            break
        print(i)
    else:
        print('else ran!')


def main():
    while_else()

    print('=' * 79)

    broken = False
    for i in range(10):
        if i == 50:
            print('I found five!')
            broken = True
            break
        print(i)

    if not broken:
        print('else ran!')


if __name__ == '__main__':
    exit(main())
