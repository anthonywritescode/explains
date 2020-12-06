import ast
import sys
from typing import Any
from typing import Generator
from typing import Tuple
from typing import Type

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        yield 1, 0, 'FNA100 named arguments', type(self)
