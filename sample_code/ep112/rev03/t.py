import shutil


def main() -> int:
    width, _ = shutil.get_terminal_size()
    print(' setup '.center(width, '='))
    print('...')
    print(' teardown '.center(width, '='))
    print('...')

    return 0


if __name__ == '__main__':
    exit(main())
