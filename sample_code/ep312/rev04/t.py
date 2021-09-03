import os
from typing import NoReturn


def main() -> NoReturn:
    cmd = ('eche', 'hi')
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
