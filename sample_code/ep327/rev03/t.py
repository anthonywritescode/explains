#!/usr/bin/env python3
import os.path
import sys


def read_link(path: str) -> str:
    read = os.readlink(path)
    return os.path.join(os.path.dirname(path), read)


def main() -> int:
    exe = sys.argv[0]
    while (
            os.path.islink(exe) and
            os.path.islink(read_link(exe))
    ):
        exe = read_link(exe)

    exe = os.path.basename(exe)
    if exe == 'uniq':
        seen = {}
        for line in sys.stdin:
            seen[line] = True
        for line in seen:
            print(line, end='')
        return 0
    else:
        raise NotImplementedError(exe)


if __name__ == '__main__':
    raise SystemExit(main())
