import sys


def average(numbers):
    return sum(numbers) / len(numbers)


def main():
    print('enter some numbers, type "done" when done:')
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line == 'done':
            break
        else:
            numbers.append(float(line))
    if not numbers:
        print('no numbers were entered!')
    else:
        print(f'the average is {average(numbers)}')
    return 0


if __name__ == '__main__':
    exit(main())
