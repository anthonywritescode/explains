import sys


def average(numbers):
    return sum(numbers) / len(numbers)


def real_main():
    print('enter some numbers, type "done" when done:')
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line == 'done':
            break
        else:
            numbers.append(float(line))
    # if not numbers:
    #     print('no numbers were entered!')
    # else:
    print(f'the average is {average(numbers)}')
    return 0


def main():
    try:
        return real_main()
    except Exception as e:
        import pdb; pdb.post_mortem()
        print(f'unexpected error occured: {type(e).__name__}: {e}')
        return 1


if __name__ == '__main__':
    exit(main())
