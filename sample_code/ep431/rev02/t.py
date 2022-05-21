from __future__ import annotations

import argparse
import ast


class NV(ast.NodeVisitor):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'click' and
            node.func.attr == 'option'
        ):
            keywords = {kwd.add for kwd in node.keywords}
            if keywords >= {'type', 'default'}:
                print(f'+{node.lineno} {self.filename}')

        self.generic_visit(node)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+')
    args = parser.parse_args()

    for filename in args.filenames:
        with open(filename) as f:
            tree = ast.parse(f.read())

        visitor = NV(filename)
        visitor.visit(tree)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
