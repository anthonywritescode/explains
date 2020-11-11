import pprint


requirements = [
    'windows-curses;sys_platform=="win32"',
    'pytest==5.2',
    'pytest-cov',
    'pre-commit',
]


def sort_key(s: str) -> str:
    # old way using split
    if '==' in s:
        s = s.split('==', 1)[0]
    if ';' in s:
        s = s.split(';', 1)[0]
    return s


def main() -> int:
    pprint.pprint(sorted(requirements, key=sort_key))
    return 0


if __name__ == '__main__':
    exit(main())
