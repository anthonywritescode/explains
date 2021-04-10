from typing import List
from typing import Tuple
from typing import Protocol


class NamedTupleProtocol(Protocol):
    @property
    def _fields(self) -> Tuple[str, ...]: ...
def hide_api_key_repr(nt: NamedTupleProtocol, *, key: str = 'api_key') -> str: ...
def zsplit(bs: bytes) -> List[bytes]: ...
