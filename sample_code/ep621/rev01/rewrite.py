#!/usr/bin/env python3
import os
import subprocess


def zsplit(s: str) -> list[str]:
    s = s.strip('\0')
    if s:
        return s.split('\0')
    else:
        return []


def main() -> int:
    out = subprocess.check_output(('git', 'ls-files', '-z'), text=True)
    for line in zsplit(out):
        if '/vscode_ext/jac/' not in line:
            os.remove(line)
        else:
            _, rest = line.split('/vscode_ext/jac/')
            os.makedirs(os.path.abspath(os.path.dirname(rest)), exist_ok=True)
            os.rename(line, rest)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
