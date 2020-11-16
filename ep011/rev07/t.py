

def while_else():
    i = 0
    while i < 10:
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
