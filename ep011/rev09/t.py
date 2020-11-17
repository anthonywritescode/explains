import ast
import sys
from typing import List
from typing import Union


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.locs: List[int] = []

    def _visit_has_else(self, node: Union[ast.For, ast.While]) -> None:
        if node.orelse:
            self.locs.append(node.lineno)
        self.generic_visit(node)

    visit_For = visit_While = _visit_has_else


def main() -> int:
    for filename in sys.argv[1:]:
        with open(filename, 'rb') as f:
            contents = f.read()

        try:
            parsed = ast.parse(contents, filename=filename)
        except SyntaxError as e:
            print(f'<<skipping {filename}: {e}>>', file=sys.stderr)
            continue

        visitor = Visitor()
        visitor.visit(parsed)
        if visitor.locs:
            for loc in visitor.locs:
                print(f'{filename}:{loc}')

    return 0


if __name__ == '__main__':
    exit(main())
