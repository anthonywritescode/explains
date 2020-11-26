import ast
import sys
from typing import Any
from typing import Generator
from typing import List
from typing import Tuple
from typing import Type

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

MSG = 'FNA100 all arguments in ** are identifiers'


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def visit_Call(self, node: ast.Call) -> None:
        for keyword in node.keywords:
            if (
                    keyword.arg is None and
                    isinstance(keyword.value, ast.Dict) and
                    all(
                        isinstance(key, ast.Str)
                        for key in keyword.value.keys
                    ) and
                    all(
                        key.s.isidentifier()
                        for key in keyword.value.keys
                    )
            ):
                self.problems.append((node.lineno, node.col_offset))

        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.problems:
            yield line, col, MSG, type(self)
