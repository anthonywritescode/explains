import string
from typing import List


class C:
    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, attr: str) -> int:
        if attr in string.ascii_lowercase:
            return self.x
        else:
            raise AttributeError(attr)

    def __dir__(self) -> List[str]:
        lst = list(super().__dir__())
        lst.extend(string.ascii_lowercase)
        return lst
