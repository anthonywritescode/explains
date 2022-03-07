import argparse
import ast


class Visitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        ...


def _rewrite_file(filename: str) -> int:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()

    tree = ast.parse(contents, filename=filename)
    for node in ast.walk(tree):
        print(node)


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
