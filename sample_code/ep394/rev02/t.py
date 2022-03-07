from __future__ import annotations

import argparse
import ast

from tokenize_rt import Offset


def _all_annotated(node: ast.FunctionDef) -> bool:
    return True


def _no_return(node: ast.FunctionDef) -> bool:
    return True


def _rewrite_file(filename: str) -> int:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()

    found: set[Offset] = set()
    tree = ast.parse(contents, filename=filename)
    for node in ast.walk(tree):
        if (
                isinstance(node, ast.FunctionDef) and
                node.returns is None and
                _all_annotated(node) and
                _no_return(node)
        ):
            found.add(Offset(node.lineno, node.col_offset))

    print(found)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()

    ret = 0
    for filename in args.filenames:
        ret |= _rewrite_file(filename)

    return ret


if __name__ == '__main__':
    raise SystemExit(main())
