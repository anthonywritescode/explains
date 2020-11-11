import pprint


requirements = [
    'windows-curses;sys_platform=="win32"',
    'pytest==5.2',
    'pre-commit',
]


def main() -> int:
    pprint.pprint(sorted(requirements))


if __name__ == '__main__':
    exit(main())
